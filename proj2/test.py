Lyrics = ["I want to to be like this", "I say hi to this"]
Titles = ["Like", "Say"]

enter = str(input("Enter:\n"))

found = []
count = 0
for lyric in Lyrics:
  found.append(lyric.count(enter))

print(found)


