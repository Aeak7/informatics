# runs if option 1 is selected, loops though range of titles
# makes sure all results are lowercase to prevent case-sensitivity
# places and returns title and number of occurrences in a dictionary
def optionOne(keyInput, songTitles):
  output = dict()
  for i in range(0, len(songTitles)-1):
    if keyInput.lower() in songTitles[i].lower():
      result = songTitles[i].lower().count(keyInput.lower())
      output[songTitles[i].strip()] = result
  return output
  
# runs if option 2 is selected, loops though range of lyrics
# makes sure all results are lowercase to prevent case-sensitivity
# places and returns title and number of occurrences in a dictionary
def optionTwo(keyInput, songLyrics, songTitles):
  output = dict()
  for i in range(0, len(songLyrics)-1): 
    if keyInput.lower() in songLyrics[i].lower():
      result = songLyrics[i].lower().count(keyInput.lower())
      output[songTitles[i].strip()] = result
  return output
