import openai

from .secret_keys import GPT_KEY

openai.api_key = GPT_KEY


def get_gpt3_phrases(text):
  prompt=f"""Text: {text}
  Separate the given text into coherent phrases, keep exact characters as the original text and separate onto new lines: 
  """
  response = openai.Completion.create(
    model="text-davinci-003",
    prompt=prompt,
    temperature=0.7,
    max_tokens=1000,
    top_p=1.0,
    frequency_penalty=0.0,
    presence_penalty=0.0,
  )
  choice = response.get("choices")[0]
  final_text = choice.get("text")
  text_split = final_text.split("\n")
  text_split_proc = list(filter(None, text_split))
  return text_split_proc

def get_gpt3_phrase_timestamps(phrases, words):
  word_loc = 0

  timestamps = []

  word_start_idx = 0
  # go through all the phrases generated by openai
  for i in range(len(phrases) - 1):
    last_word = phrases[i].split()[-1]
    next_first_word = phrases[i + 1].split()[0]

    # find the next occurence where the last word of this phrase
    # and the next word of the next phrase occur
    # go through words until we find two elements beside each other
    # that are last_word and next_first_word
    while word_loc < len(words) - 1:
      # TODO handle when this occurs within the phrase as well, not just at the end
      if words[word_loc].get("text") == last_word and words[word_loc + 1].get("text") == next_first_word:
        this_phrase_stamp = (
          words[word_start_idx].get("start"),
          words[word_loc].get("end")
        )
        timestamps.append(this_phrase_stamp)
        # save the next phrases start
        word_start_idx = word_loc + 1
        break
      else:
        word_loc += 1

  last_stamp = (
    words[word_start_idx].get("start"),
    words[-1].get("end")
  )
  timestamps.append(last_stamp)
  
  return timestamps

def get_gpt3_stable_diffusion_prompt(phrase):
  prompt=f"""Q: What is CLIP+Diffusion AI Art Generation?
A: CLIP+Diffusion AI Art Generation is a method of creating art using artificial intelligence. This method involves using a neural network to generate images, and then using a diffusion process to create variations on those images.

Q: How should you write the text prompt for a art generation software to get ideal output for character art?
A: You should write a descriptive prompt that the computer can “understand”. A good way to look at it is like Alt (Alternative) text in HTML. It’s quite literal, descriptive, and to the point, so the machine doesn’t have to do so much guess work.

Q: Write a text prompt for a AI art generation software that would create an image that visualizes the phrase "{phrase}"
A:"""
  response = openai.Completion.create(
    model="text-davinci-003",
    prompt=prompt,
    temperature=0.7,
    max_tokens=1000,
    top_p=1.0,
    frequency_penalty=0.0,
    presence_penalty=0.0,
  )
  choice = response.get("choices")[0]
  final_text = choice.get("text")
  return final_text

if __name__ == "__main__":
  test_resp =  {
    "text": "The rose that grew from the concrete did you hear about the rose that grew from a crack in the concrete? Proving nature's law is wrong it learned to walk without having feet funny it seems but by keeping its dreams it learned to breathe fresh air long live the rose that grew from concrete when no one else ever cared.",
    "words": [
          {
                  "text": "The",
                  "start": 810,
                  "end": 926,
                  "confidence": 1.0,
                  "speaker": "A"
          },
          {
                  "text": "rose",
                  "start": 948,
                  "end": 1322,
                  "confidence": 0.60131,
                  "speaker": "A"
          },
          {
                  "text": "that",
                  "start": 1386,
                  "end": 1662,
                  "confidence": 0.92,
                  "speaker": "A"
          },
          {
                  "text": "grew",
                  "start": 1716,
                  "end": 2042,
                  "confidence": 0.7634,
                  "speaker": "A"
          },
          {
                  "text": "from",
                  "start": 2106,
                  "end": 2334,
                  "confidence": 0.99951,
                  "speaker": "A"
          },
          {
                  "text": "the",
                  "start": 2372,
                  "end": 2526,
                  "confidence": 1.0,
                  "speaker": "A"
          },
          {
                  "text": "concrete",
                  "start": 2548,
                  "end": 3550,
                  "confidence": 0.5792,
                  "speaker": "A"
          },
          {
                  "text": "did",
                  "start": 4210,
                  "end": 4574,
                  "confidence": 0.70879,
                  "speaker": "A"
          },
          {
                  "text": "you",
                  "start": 4612,
                  "end": 4814,
                  "confidence": 1.0,
                  "speaker": "A"
          },
          {
                  "text": "hear",
                  "start": 4852,
                  "end": 5342,
                  "confidence": 0.99992,
                  "speaker": "A"
          },
          {
                  "text": "about",
                  "start": 5476,
                  "end": 5822,
                  "confidence": 0.99988,
                  "speaker": "A"
          },
          {
                  "text": "the",
                  "start": 5876,
                  "end": 6046,
                  "confidence": 1.0,
                  "speaker": "A"
          },
          {
                  "text": "rose",
                  "start": 6068,
                  "end": 6394,
                  "confidence": 0.81918,
                  "speaker": "A"
          },
          {
                  "text": "that",
                  "start": 6442,
                  "end": 6654,
                  "confidence": 1.0,
                  "speaker": "A"
          },
          {
                  "text": "grew",
                  "start": 6692,
                  "end": 7050,
                  "confidence": 0.73762,
                  "speaker": "A"
          },
          {
                  "text": "from",
                  "start": 7130,
                  "end": 7374,
                  "confidence": 0.99941,
                  "speaker": "A"
          },
          {
                  "text": "a",
                  "start": 7412,
                  "end": 7566,
                  "confidence": 0.99,
                  "speaker": "A"
          },
          {
                  "text": "crack",
                  "start": 7588,
                  "end": 7866,
                  "confidence": 0.99807,
                  "speaker": "A"
          },
          {
                  "text": "in",
                  "start": 7898,
                  "end": 8046,
                  "confidence": 0.96156,
                  "speaker": "A"
          },
          {
                  "text": "the",
                  "start": 8068,
                  "end": 8206,
                  "confidence": 0.99,
                  "speaker": "A"
          },
          {
                  "text": "concrete?",
                  "start": 8228,
                  "end": 9230,
                  "confidence": 0.98766,
                  "speaker": "A"
          },
          {
                  "text": "Proving",
                  "start": 9890,
                  "end": 10474,
                  "confidence": 0.99708,
                  "speaker": "A"
          },
          {
                  "text": "nature's",
                  "start": 10522,
                  "end": 10986,
                  "confidence": 0.87059,
                  "speaker": "A"
          },
          {
                  "text": "law",
                  "start": 11018,
                  "end": 11454,
                  "confidence": 0.97737,
                  "speaker": "A"
          },
          {
                  "text": "is",
                  "start": 11572,
                  "end": 11902,
                  "confidence": 0.99841,
                  "speaker": "A"
          },
          {
                  "text": "wrong",
                  "start": 11956,
                  "end": 12318,
                  "confidence": 0.99992,
                  "speaker": "A"
          },
          {
                  "text": "it",
                  "start": 12404,
                  "end": 12654,
                  "confidence": 0.99869,
                  "speaker": "A"
          },
          {
                  "text": "learned",
                  "start": 12692,
                  "end": 12938,
                  "confidence": 0.98836,
                  "speaker": "A"
          },
          {
                  "text": "to",
                  "start": 12954,
                  "end": 13134,
                  "confidence": 0.97,
                  "speaker": "A"
          },
          {
                  "text": "walk",
                  "start": 13172,
                  "end": 13566,
                  "confidence": 0.99911,
                  "speaker": "A"
          },
          {
                  "text": "without",
                  "start": 13668,
                  "end": 14030,
                  "confidence": 0.99992,
                  "speaker": "A"
          },
          {
                  "text": "having",
                  "start": 14100,
                  "end": 14430,
                  "confidence": 0.99979,
                  "speaker": "A"
          },
          {
                  "text": "feet",
                  "start": 14500,
                  "end": 15230,
                  "confidence": 0.99,
                  "speaker": "A"
          },
          {
                  "text": "funny",
                  "start": 16610,
                  "end": 17146,
                  "confidence": 0.96017,
                  "speaker": "A"
          },
          {
                  "text": "it",
                  "start": 17178,
                  "end": 17326,
                  "confidence": 0.99912,
                  "speaker": "A"
          },
          {
                  "text": "seems",
                  "start": 17348,
                  "end": 18014,
                  "confidence": 0.49951,
                  "speaker": "A"
          },
          {
                  "text": "but",
                  "start": 18212,
                  "end": 18622,
                  "confidence": 0.99911,
                  "speaker": "A"
          },
          {
                  "text": "by",
                  "start": 18676,
                  "end": 18846,
                  "confidence": 0.99991,
                  "speaker": "A"
          },
          {
                  "text": "keeping",
                  "start": 18868,
                  "end": 19226,
                  "confidence": 0.81643,
                  "speaker": "A"
          },
          {
                  "text": "its",
                  "start": 19258,
                  "end": 19454,
                  "confidence": 0.98059,
                  "speaker": "A"
          },
          {
                  "text": "dreams",
                  "start": 19492,
                  "end": 20026,
                  "confidence": 0.5347,
                  "speaker": "A"
          },
          {
                  "text": "it",
                  "start": 20138,
                  "end": 20414,
                  "confidence": 0.99756,
                  "speaker": "A"
          },
          {
                  "text": "learned",
                  "start": 20452,
                  "end": 20778,
                  "confidence": 0.97463,
                  "speaker": "A"
          },
          {
                  "text": "to",
                  "start": 20794,
                  "end": 20974,
                  "confidence": 1.0,
                  "speaker": "A"
          },
          {
                  "text": "breathe",
                  "start": 21012,
                  "end": 21386,
                  "confidence": 0.99397,
                  "speaker": "A"
          },
          {
                  "text": "fresh",
                  "start": 21418,
                  "end": 21674,
                  "confidence": 0.99417,
                  "speaker": "A"
          },
          {
                  "text": "air",
                  "start": 21722,
                  "end": 22320,
                  "confidence": 0.99109,
                  "speaker": "A"
          },
          {
                  "text": "long",
                  "start": 23410,
                  "end": 24014,
                  "confidence": 0.99672,
                  "speaker": "A"
          },
          {
                  "text": "live",
                  "start": 24132,
                  "end": 24462,
                  "confidence": 0.81055,
                  "speaker": "A"
          },
          {
                  "text": "the",
                  "start": 24516,
                  "end": 24686,
                  "confidence": 0.96,
                  "speaker": "A"
          },
          {
                  "text": "rose",
                  "start": 24708,
                  "end": 25170,
                  "confidence": 0.28646,
                  "speaker": "A"
          },
          {
                  "text": "that",
                  "start": 25290,
                  "end": 25622,
                  "confidence": 0.95,
                  "speaker": "A"
          },
          {
                  "text": "grew",
                  "start": 25676,
                  "end": 25906,
                  "confidence": 0.99908,
                  "speaker": "A"
          },
          {
                  "text": "from",
                  "start": 25938,
                  "end": 26182,
                  "confidence": 0.99956,
                  "speaker": "A"
          },
          {
                  "text": "concrete",
                  "start": 26236,
                  "end": 26882,
                  "confidence": 0.90611,
                  "speaker": "A"
          },
          {
                  "text": "when",
                  "start": 26946,
                  "end": 27174,
                  "confidence": 0.99565,
                  "speaker": "A"
          },
          {
                  "text": "no",
                  "start": 27212,
                  "end": 27414,
                  "confidence": 0.99988,
                  "speaker": "A"
          },
          {
                  "text": "one",
                  "start": 27452,
                  "end": 27750,
                  "confidence": 0.99,
                  "speaker": "A"
          },
          {
                  "text": "else",
                  "start": 27820,
                  "end": 28198,
                  "confidence": 0.9998,
                  "speaker": "A"
          },
          {
                  "text": "ever",
                  "start": 28284,
                  "end": 28534,
                  "confidence": 0.99981,
                  "speaker": "A"
          },
          {
                  "text": "cared.",
                  "start": 28572,
                  "end": 28850,
                  "confidence": 0.44333,
                  "speaker": "A"
          }
        ],
      }

  phrases = get_gpt3_phrases(test_resp.get("text"))
  print(phrases)
  timestamps = get_gpt3_phrase_timestamps(phrases, test_resp.get("words"))
  print(timestamps)
  print([get_gpt3_stable_diffusion_prompt(p) for p in phrases])
