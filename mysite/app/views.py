from django.shortcuts import render

from django.conf import settings
from django.core.files.storage import FileSystemStorage

from .transcript import (
  upload_audio,
  start_generation_transcript, get_completed_transcript,
  get_durations,
)
from .video_helper import turn_prompts_to_images, create_video
from .gpt3_handler import (
  get_gpt3_phrases,
  get_gpt3_phrase_timestamps,
  get_gpt3_stable_diffusion_prompt
)

VIDEO_EXT = ".webserver.mp4"
EXAMPLE_VID_URL = "/media/donot_stand_at_my_graveandcry_XFjM4dl.mp3.webserver.mp4"

def index(request):
  if request.method == "POST" and request.FILES["myfile"]:
    myfile = request.FILES["myfile"]

    # SAVE UPLOADED FILE
    fs = FileSystemStorage()
    filename = fs.save(myfile.name, myfile)
    uploaded_file_url = fs.url(filename)
    absolute_file_path = fs.path(filename)

    print("SAVED AUDIO")
    # START PROCESSING AUDIO
    t_url = upload_audio(absolute_file_path)
    t_id = start_generation_transcript(t_url)
    text, words = get_completed_transcript(t_id)

    print("GENERATED TRANSCRIPT")
    print(text)

    phrases = get_gpt3_phrases(text)
    
    print("GENERATED PHRASES")
    print(phrases)

    timestamps = get_gpt3_phrase_timestamps(phrases, words)
    print(timestamps)
    durations = get_durations(timestamps)

    prompts = [get_gpt3_stable_diffusion_prompt(p) for p in phrases]

    print("GENERATED PROMPTS")

    # START GENERATING VIDEO
    imgs = turn_prompts_to_images(prompts)
    video_filename = absolute_file_path + VIDEO_EXT
    
    # SAVE VIDEO AND SHOW TO USER
    print(len(imgs))
    print(len(durations))
    create_video(imgs[:len(durations)], durations, absolute_file_path, video_filename)
    video_url = uploaded_file_url + VIDEO_EXT
    print(video_url)
    return render(request, "app/index.html", {
      "video_url": video_url,
      "is_generated": True,
    })

  return render(request, "app/index.html", {
    "video_url": EXAMPLE_VID_URL,
    "is_generated": False,
  })

