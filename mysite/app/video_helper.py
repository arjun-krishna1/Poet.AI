from secret_keys import REPLICATE_KEY

import replicate

from PIL import Image

from moviepy.video.io.ImageSequenceClip import ImageSequenceClip
from moviepy.audio.io.AudioFileClip import AudioFileClip

import requests
from numpy import asarray

client = replicate.Client(api_token=REPLICATE_KEY)
model = client.models.get("stability-ai/stable-diffusion")
version = model.versions.get("6359a0cab3ca6e4d3320c33d79096161208e9024d174b2311e5a21b6c7e1131c")
NEG_PROMPT="text letters numbers"

def turn_prompts_to_images(prompts):
  # TODO this should be in parallel
  img_links = [version.predict(prompt=p, negative_prompt=NEG_PROMPT)[0] for p in prompts]
  frames = [
    asarray(Image.open(requests.get(url, stream=True).raw))
    for url in img_links
  ]

  return frames


def create_video(frames, durations, audio_fp, video_fp):
  clip = ImageSequenceClip(frames, durations=durations)
  audio = AudioFileClip(audio_fp)
  clip_audio = clip.set_audio(audio)
  return clip_audio.write_videofile(video_fp, fps=1)
