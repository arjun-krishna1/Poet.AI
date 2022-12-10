from .secret_keys import ASSEMBLY_AI_KEY

import requests
import re

from time import sleep

"""
Handlers for Assembly AI transcription API
Example script in ./script.py
"""

def read_file(filename, chunk_size=5242880):
  with open(filename, "rb") as _file:
    while True:
      data = _file.read(chunk_size)
      if not data:
        break
      yield data

def upload_audio(fpath: str) -> str:
  """
  Takes the filepath of an audio recording
  And uploads to Assembly AI CDN
  """
  headers = {"authorization": ASSEMBLY_AI_KEY}
  upload_response = requests.post("https://api.assemblyai.com/v2/upload",
    headers=headers,
    data=read_file(fpath))
  upload_url = upload_response.json().get("upload_url")
  return upload_url

def start_generation_transcript(upload_url: str) -> str:
  """
  Takes the url of an audio file
  Starts transcription on Assembly AI
  Returns the transcript_id
  """
  endpoint = "https://api.assemblyai.com/v2/transcript"
  json = {
    "audio_url": upload_url
  }
  headers = {
    "authorization": ASSEMBLY_AI_KEY,
    "content-type": "application/json"
  }
  response = requests.post(endpoint, json=json, headers=headers)
  response_json = response.json()

  transcript_id = response_json.get("id")
  return transcript_id

def get_completed_transcript(transcript_id: str) -> str:
  """
  Takes the transcript id of an Assembly AI transcription job
  Loops til transcription is over
  Processes result and returns list of phrases in audio
  """
  MAX_ATTEMPTS=10
  WAIT_STEP=0.1*60
  COMPLETE_MSG="completed"

  # TODO handle error response
  endpoint = f"https://api.assemblyai.com/v2/transcript/{transcript_id}"
  headers = {
      "authorization": ASSEMBLY_AI_KEY,
  }

  success = False
  for i in range(MAX_ATTEMPTS):
    response_new = requests.get(endpoint, headers=headers)
    response_new_json = response_new.json()
    status = response_new_json.get("status")

    if status == COMPLETE_MSG:
      success = True
      response_fin = response_new_json
      break
    else:
      sleep(WAIT_STEP)

  if success:
    transcript = response_fin.get("text")
    SPLIT_REGEX = ";|\."
    main_phrases = re.split(SPLIT_REGEX, transcript)
    main_phrases_processed = list(filter(None, main_phrases))
    return main_phrases_processed
  else:
    return []