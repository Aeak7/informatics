# ---------------------------------------------------
# This program reads from an input text file, processes
# the text lines to count the number of characters in the text,
# and prompts user to enter keywords to count the number of
# text lines that a keyword appears in.
#
# The input file name is "songs.txt"
#
# Author : Leen-Kiat Soh
# Date : 09/14/2023
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

print("Welcome to the Text Analysis Program!")
print("This program finds the songs that a search key is found in, using the input file 'songs.txt'")

keyInput = 0
keyInputLower = 0
result = dict()
titleCount = 0
foundTitles = []
foundLyrics = []
counter = []
while keyInput != -1:
   keyInput = input("Please enter a search key(or -1 to exit):\n")
   keyInputLower = keyInput.lower()
   if keyInput == str(-1):
      break;
   else:
      print("You entered: " + keyInput)
      print("Please select where you would like to search (1, 2, or 3):\n1) Within a song's title\n2) Within a song's lyrics\n3) Within both the title and lyrics")
      selectionInput = input()
      if selectionInput == str(1): # songs title
         print("option 1")
         for title in songTitles:
            if (keyInput or keyInputLower) in title:
               result[title] = title.count(keyInput or keyInputLower)
         print(result)
         continue;
      elif selectionInput == str(2): # songs lyrics
         print("option 2")
         for lyric in songLyrics:
            if (keyInput or keyInputLower) in lyric:
               foundLyrics.append(lyric)
      elif selectionInput == str(3): # both
         print("option 3")
         for title in songTitles:
            if (keyInput or keyInputLower) in title:
               foundTitles.append(title)
         for lyric in songLyrics:
            if (keyInput or keyInputLower) in lyric:
               foundLyrics.append(lyric)
      else:
         print("Sorry this input is invalid")
         continue;



# -----------------
# Example processing of how to use the array to generate statistics
# Note: This is to be deleted as it is not part of the assignment
# -----------------
# lengthTitle = 0
# for i in range(0,count):  # going through each item of the array
#    print("title: " + str(songTitles[i]) + " Length of Lyrics: " + str(len(songLyrics[i])))

# -----------------
# Analyze the data
# -----------------
# Enter code here
# -----------------

# print out exit message
print("Thank you for using the Text Analyzer!")
       



