from transcript import (
  upload_audio,
  start_generation_transcript,
  get_completed_transcript,
  get_phrase_timestamps,
  get_durations,
)

from video_helper import turn_prompts_to_images, create_video

from gpt3_handler import (
  get_gpt3_phrases, get_gpt3_phrase_timestamps, get_gpt3_stable_diffusion_prompt
)


AUDIO_FILE_PATH = "./the_road_less_traveled.mp3"
VIDEO_RESULT_PATH = "output_openai.mp4"

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
  print("GETTING PHRASES GPT3")
  phrases = get_gpt3_phrases(text)
  print("GOT PHRASES, phrases")
  print(phrases)
  print()
  print("GET TIMESTAMPS FROM GPT3 PHRASES")
  timestamps = get_gpt3_phrase_timestamps(phrases, words)
  print("GOT TIMESTAMPS, timestamps")
  print(timestamps)
  print("GETTING DURATIONS")
  durations = get_durations(timestamps)
  print("GOT DURATIONS, durations")
  print(durations)
  print()

  print("MAKING PHRASES INTO BETTER PROMPTS")
  prompts = [get_gpt3_stable_diffusion_prompt(p) for p in phrases]
  print("GOT PROMPTS")
  print(prompts)
  print()
  
  print("GETTING GENERATED IMAGES FROM PHRASES")
  # TODO start API calls and get results in parallel
  imgs = turn_prompts_to_images(prompts)
  
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
