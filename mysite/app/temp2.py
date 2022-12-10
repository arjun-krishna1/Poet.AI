from PIL import Image

from moviepy.video.io.ImageSequenceClip import ImageSequenceClip
from moviepy.audio.io.AudioFileClip import AudioFileClip

import requests
from numpy import asarray


img_links = ['https://replicate.delivery/pbxt/CPu7BbTKj0ZwCJSKJ02mjpzCrqQEXoq1iT1zQWqJulx2zJCE/out-0.png', 'https://replicate.delivery/pbxt/kGPgnIBTL9aAPZ27t4m9Y9xKfefC0RQumYhIBtVa2uldfciAB/out-0.png', 'https://replicate.delivery/pbxt/N6r2iuWO2SIzERTCBHLsHksU9JIKr520o1mhVAHVg4NB0JCE/out-0.png', 'https://replicate.delivery/pbxt/LhbNGSMk6B4QCBmDs27YSiexbJRwLFD1ehv9uShZ9tRTQnIQA/out-0.png', 'https://replicate.delivery/pbxt/n1VezZcmv6xTUKMUoCOPCuQJYp6dc0PieKjnauqfxTEFhORgA/out-0.png', 'https://replicate.delivery/pbxt/iWRsVaDjEZrcB1k6VwK7Pu3D8rBCy14fNeOA0jINfZMlhORgA/out-0.png', 'https://replicate.delivery/pbxt/imwbQG3uSNqMHlEidcyc38VdxfTt5l2C2OsxO3XZis4joTEIA/out-0.png', 'https://replicate.delivery/pbxt/pOayNWddzr7wMlKVfB9fKM5SyQMvHu8KzzE55kFhJrVdRnIQA/out-0.png', 'https://replicate.delivery/pbxt/EseEJhjE6swgJivRdNTsvgmKXs8JD8Ifduo1vFyymhD8RnIQA/out-0.png', 'https://replicate.delivery/pbxt/T0P3kponfd2ejUQIZW3vFDv8rpXT9XrwZ5Uktt3lNoRVSnIQA/out-0.png', 'https://replicate.delivery/pbxt/5crfPwQCrX3ldSptd7EA2MKltej9eh5oJP6OIwQAz5xIlORgA/out-0.png', 'https://replicate.delivery/pbxt/NixU7eOVLTzaBCOEggXBtkfQhQuMXigCpCw4BV0LEohySnIQA/out-0.png']

frames = [
    asarray(Image.open(requests.get(url, stream=True).raw))
    for url in img_links
]

durations = [9.134, 6.576, 1.744, 1.2346, 3.946, 1.940, 0.720, 5.888, 0.880, 1.666, 3.290, 10.010]

clip = ImageSequenceClip(frames, durations=durations)

audio = AudioFileClip("./the_road_less_traveled.mp3")
clip_audio = clip.set_audio(audio)

clip_audio.write_videofile("output_durations_FILE.mp4", fps=1)


