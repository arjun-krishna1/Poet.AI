from secret_keys import ASSEMBLY_AI_KEY, REPLICATE_KEY

import replicate

from PIL import Image
from moviepy.video.io.ImageSequenceClip import ImageSequenceClip
from moviepy.audio.io.AudioFileClip import AudioFileClip

import requests
import re
from time import sleep
from numpy import asarray


AUDIO_FILE_PATH = "./the_road_less_traveled.mp3"

def read_file(filename, chunk_size=5242880):
  with open(filename, "rb") as _file:
    while True:
      data = _file.read(chunk_size)
      if not data:
        break
      yield data

def main():
  headers = {"authorization": ASSEMBLY_AI_KEY}
  upload_response = requests.post("https://api.assemblyai.com/v2/upload",
    headers=headers,
    data=read_file(AUDIO_FILE_PATH))

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

  WAIT_ORIG=0.20*60
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

  if not success:
    print("FAILED, LAST RESPONSE")
    print(response_new_json)
  else:
    print(response_fin)
    transcript = response_fin.get("text")
    SPLIT_REGEX = "(;|\.)"
    phrases = re.split(SPLIT_REGEX, transcript)
    phrases_processed = list(filter(None, phrases))
    print(phrases_processed)

    model = replicate.models.get("stability-ai/stable-diffusion")
    version = model.versions.get("6359a0cab3ca6e4d3320c33d79096161208e9024d174b2311e5a21b6c7e1131c")
    
    print()
    print('ABOUT TO CALL REPLICATE API')
    NEG_PROMPT="text letters numbers"
    img_links = [version.predict(prompt=p, negative_prompt=NEG_PROMPT)[0] for p in phrases_processed]
    print('GENERATED IMAGES, imgs')
    print(img_links)

    if len(img_links):
      print("DOWNLOADING IMAGES FROM REPLICATE AND CONVERTING TO NP ARRAYS")
      # Loop through each image URL and convert it to a video frame
      frames = [
        asarray(Image.open(requests.get(url, stream=True).raw))
        for url in img_links
      ]

      print("CREATING IMAGE SEQUENCE CLIP FROM FRAMES")
      # Create the video clip
      clip = ImageSequenceClip(frames, fps=1)

      print("LOADING AND SETTING THE AUDIO")
      # Load the audio file
      audio = AudioFileClip(AUDIO_FILE_PATH)
      clip_audio = clip.set_audio(audio)

      print("WRITING CLIP TO A VIDEO FILE")
      # Create an empty video file
      video_file = "output_w_audio.mp4"
      # Save the video to the specified file
      clip_audio.write_videofile(video_file)
    else:
      print("DIDN'T HAVE ANY IMAGES")


if __name__ == "__main__":
  main()
