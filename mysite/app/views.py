from django.shortcuts import render

from django.conf import settings
from django.core.files.storage import FileSystemStorage

import os

from .transcript import (
  upload_audio,
  start_generation_transcript, get_completed_transcript,
  get_phrase_timestamps,
  get_durations,
)

from .video_helper import turn_prompts_to_images, create_video

VIDEO_EXT = ".webserver.mp4"

def index(request):
  if request.method == "POST" and request.FILES["myfile"]:
    myfile = request.FILES["myfile"]

    # SAVE UPLOADED FILE
    fs = FileSystemStorage()
    filename = fs.save(myfile.name, myfile)
    uploaded_file_url = fs.url(filename)
    absolute_file_path = fs.path(filename)

    # START PROCESSING AUDIO
    t_url = upload_audio(absolute_file_path)
    t_id = start_generation_transcript(t_url)
    _, words = get_completed_transcript(t_id)

    print(_, words)

    phrases = get_phrase_timestamps(words)
    durations = get_durations(phrases)

    # START GENERATING VIDEO
    imgs = turn_prompts_to_images(phrases.values())
    video_filename = absolute_file_path + VIDEO_EXT
    
    # SAVE VIDEO AND SHOW TO USER
    create_video(imgs, durations, absolute_file_path, video_filename)
    video_url = uploaded_file_url + VIDEO_EXT

    return render(request, "app/index.html", {
      "video_url": video_url,
    })

  return render(request, "app/index.html")

