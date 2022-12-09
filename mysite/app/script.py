from secret_keys import ASSEMBLY_AI_KEY

import requests
import re

from time import sleep

FILE_PATH = "./the_road_less_traveled.mp3"

def read_file(filename, chunk_size=5242880):
  with open(filename, "rb") as _file:
    while True:
      data = _file.read(chunk_size)
      if not data:
        break
      yield data

headers = {"authorization": ASSEMBLY_AI_KEY}
upload_response = requests.post("https://api.assemblyai.com/v2/upload",
  headers=headers,
  data=read_file(FILE_PATH))

upload_url = upload_response.json().get("upload_url")
print(f"UPLOADED AUDIO {upload_url}")

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
print(f"POSTED TRANSCRIPT REQUEST {transcript_id}")

MAX_ATTEMPTS=10

WAIT_ORIG=0.5*60
WAIT_STEP=0.25*60

sleep(WAIT_ORIG)

COMPLETE_MSG="completed"
# TODO handle error
endpoint = f"https://api.assemblyai.com/v2/transcript/{transcript_id}"
headers = {
    "authorization": ASSEMBLY_AI_KEY,
}

print("ABOUT TO START TRYING TO GET RESULT")
success = False
for i in range(MAX_ATTEMPTS):
  response_new = requests.get(endpoint, headers=headers)
  response_new_json = response_new.json()
  status = response_new_json.get("status")
  print(f"TRY {i} OF API CALL, STATUS {status}")
  print()
  if response_new_json.get("status") == COMPLETE_MSG:
    print("completed")
    success = True
    response_fin = response_new_json
    break
  else:
    sleep(WAIT_STEP)

if success:
  print(response_fin)
  transcript = response_fin.get("text")
  SPLIT_REGEX = ";|\."
  main_phrases = re.split(SPLIT_REGEX, transcript)
  main_phrases_processed = list(filter(None, main_phrases))
  print(main_phrases_processed)
else:
  print("FAILED, LAST RESPONSE")
  print(response_new_json)
