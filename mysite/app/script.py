from transcript import (
  upload_audio,
  start_generation_transcript,
  get_completed_transcript,
  get_phrase_timestamps,
  get_durations,
)

from video_helper import turn_prompts_to_images, create_video


AUDIO_FILE_PATH = "./the_road_less_traveled.mp3"
VIDEO_RESULT_PATH = "output_durations_script_complete.mp4"

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

  durations = get_durations(phrases.keys())
  print("GOT DURATIONS, durations")
  print(durations)
  print()
  
  print("GETTING GENERATED IMAGES FROM PHRASES")
  # TODO start API calls and get results in parallel
  # TODO instead of values output two lists
  imgs = turn_prompts_to_images(phrases.values())
  
  print("GENERATED IMAGES, len imgs")
  print(len(imgs))

  if len(imgs):
    print("DOWNLOADING IMAGES FROM REPLICATE AND CONVERTING TO NP ARRAYS")
    vid = create_video(imgs, durations, AUDIO_FILE_PATH, VIDEO_RESULT_PATH)
    print("VIDEO GENERATED")
    print(vid)
    
  else:
    print("DIDN'T HAVE ANY IMAGES")


if __name__ == "__main__":
  main()
