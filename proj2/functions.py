def optionOne(keyInput, songTitles):
  output = dict()
  for i in range(0, len(songTitles)-1):
    if keyInput.lower() in songTitles[i].lower():
      result = songTitles[i].lower().count(keyInput.lower())
      output[songTitles[i].strip()] = result
  return output
  

def optionTwo(keyInput, songLyrics, songTitles):
  output = dict()
  for i in range(0, len(songLyrics)-1): 
    if keyInput.lower() in songLyrics[i].lower():
      result = songLyrics[i].lower().count(keyInput.lower())
      output[songTitles[i].strip()] = result
  return output
