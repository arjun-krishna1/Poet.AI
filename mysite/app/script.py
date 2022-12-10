from secret_keys import ASSEMBLY_AI_KEY, REPLICATE_KEY

from transcript import upload_audio, start_generation_transcript, get_completed_transcript, get_phrase_timestamps

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
  print("UPLOADING AUDIO")
  url = upload_audio(AUDIO_FILE_PATH)
  print(f"STARTING TRANSCRIPTION, url {url}")
  transcript_id = start_generation_transcript(url)
  print(f"GETTING TRANSCRIPTION, id {transcript_id}")
  text, words = get_completed_transcript(transcript_id)
  print("GOT TRANSCRIPTION, text")
  print(text)
  print()
  print("GETTING PHRASE TIMESTAMPS")
  phrases = get_phrase_timestamps(words)
  print("GOT PHRASES, phrases")
  print(phrases)
  print()

  phrases_processed = phrases.values()

  model = replicate.models.get("stability-ai/stable-diffusion")
  version = model.versions.get("6359a0cab3ca6e4d3320c33d79096161208e9024d174b2311e5a21b6c7e1131c")
  
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
