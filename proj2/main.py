# ---------------------------------------------------
# This program reads from an input text file, processes
# the text lines to count the number of characters in the text,
# and prompts user to enter keywords to count the number of
# times that a keyword appears in.
#
# The input file name is "songs.txt"
#
# Author : Abby Kelly
# Date : 09/19/2023
# ---------------------------------------------------
from functions import *

songTitles = []  # list to store all the songs' titles
songLyrics = []  # list to store all the songs' lyrics

inputFilename = 'proj2/songs.txt' # input file

# -----------------
# Read in the input file
# Store in the arrays/lists called songTitles and songLyrics
# -----------------
count = 0   # to keep track of the number of songs
titleFlag = 1  # a flag to indicate that we are ready to read in the title of the next song
lyricsSoFar = ""  # the temporary variable to hold all the lines of lyrics read in so far for a song
with open(inputFilename, "r") as infile:
   for line in infile:
      if (line == "END\n"):
         songLyrics.append(lyricsSoFar)  # add the large string of lyrics into the array 
         lyricsSoFar = ""  # reset it to an empty string
         count = count + 1  # increment the count, ready for the next song
         titleFlag = 1   # reset the flag, ready for the next song's title
      elif (titleFlag == 1):
         # print(line)
         songTitles.append(line)  # add the new song's title to the array
         titleFlag = 0   # set the flag to 0, ready to read in the lyrics of the song
      else:
         lyricsSoFar = lyricsSoFar + " " + line  # collect the lyrics into a large string
   # end for
# end with
infile.close()


# Welcomes user and explains parameters
print("Welcome to the Text Analysis Program!")
print("This program finds the songs that a search key is found in, using the input file 'songs.txt'")

keyInput = 0
while keyInput != -1: # constant loop until user enters -1 to end
   keyInput = input("Please enter a search key(or -1 to exit):\n")
   if keyInput == str(-1): # logic to check if end while loop condition is met
      break # break out of while
   else:
      print("You entered: " + keyInput) # Tells user what word they entered
      print("Please select where you would like to search (1, 2, or 3):\n1) Within a song's title\n2) Within a song's lyrics\n3) Within both the title and lyrics")
      selectionInput = input() 
      if selectionInput == str(1): # search in songs title
         results = optionOne(keyInput, songTitles) # calls function from functions.py
         if len(results) == 0: # checks if result dictionary is empty 
            print("There are no song titles containing this search key.")
         for key, value in results.items(): # retrieves both key and value values from the dictionary to print
            print(f"{key}: Appears {value} times")
         continue # go back to start of while to continue
      elif selectionInput == str(2): # search in songs lyrics
         results = optionTwo(keyInput, songLyrics, songTitles) # calls function from functions.py
         if len(results) == 0: # checks if result dictionary is empty 
            print("There are no song lyrics containing this search key.")
         for key, value in results.items(): # retrieves both key and value values from the dictionary to print
            print(f"{key}: Appears {value} times")
         continue
      elif selectionInput == str(3): # search both in titles and lyrics
         titles = optionOne(keyInput, songTitles) # calls both previous functions from functions.py
         lyrics = optionTwo(keyInput, songLyrics, songTitles)
         output = {x: titles.get(x, 0) + lyrics.get(x, 0) for x in set(titles).union(lyrics)} # adds values of both dictionaries together to "search in both"
         if len(output) == 0: # checks if result dictionary is empty 
            print("There are no song titles or lyrics containing this search key.")
         for key, value in output.items(): # retrieves both key and value values from the dictionary to print
            print(f"{key}: Appears {value} times")
         continue
      else:
         print("Sorry this input is invalid") # if user enters any out of 1, 2, or 3
         continue

# print out exit message
print("Thank you for using the Text Analyzer!")