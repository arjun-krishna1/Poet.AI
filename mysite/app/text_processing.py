def get_phrase_timestamps(words):
  res = {}
  start = words[0].get("start")
  new = False
  this_phrase = ""
  for i in range(len(words)):
    if new:
      start = words[i].get("start")
      new = False

    if words[i].get("text").isalpha():
      this_phrase += words[i].get("text") + " "
    else:
      this_phrase += words[i].get("text")
      end = words[i].get("end")
      this_key = (start, end)
      res[this_key] = this_phrase
      this_phrase = ""
      new = True
  return res
