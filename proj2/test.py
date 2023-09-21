lyrics = ["I want to to be like this", "I say hi to this"]
titles = ["Like this", "Say hi this"]

enter = str(input("Enter:\n"))

found = []
count = 0
for lyric in lyrics:
  if enter in lyric:
    count = lyric.count(enter)
  #   newLyric = lyric.split()
  #   for lyric in newLyric:
  #     if enter == lyric:
  #       found.append(lyric)
  #       count += 1
  # else:
  #   print("no")

print(found)
print(count)


