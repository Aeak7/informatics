def printResults(songTitles):
  # for i in range(0, len(songTitles)):
  #   print(str(songTitles[i]) + "Amount: " + str(foundTitles[i]))
  inlen = len(songTitles)
  print("inlen value: " + inlen)


def reportResults(opt, result, foundLyrics, foundTitles):
    print("-----------------------------------------------")
    print("ANALYSIS RESULTS" )
    print("-----------------------------------------------")
    if opt=="1":
        print("Number of finds in song titles: " + len(result))
        print("--  --  --  --  --  --  --  --  --  --  --  ---")
        if len(result) > 0:
            print("Song titles where found")
            knt = 0  # Auxiliary counter.  Used for formating purposes
            for i in result:
                knt = knt + 1
                print (str(knt) +"). ", i, end = ' ')  #Print song title with number in front
    elif opt=="2":       
        print("Number of finds in song lyrics: " + len(foundLyrics))
        print("--  --  --  --  --  --  --  --  --  --  --  ---")
        for j in foundLyrics:
            print (j, end = ' ')
            print ("==============================================")
    else:  # both titles and lyrics.  Default if no argument or invalid option
        print("Number of finds in song titles: " + len(foundTitles))
        print("--  --  --  --  --  --  --  --  --  --  --  ---")
        for i in foundTitles:
            print (i, end = ' ')
        print("-----------------------------------------------")           
        print("Number of finds in song lyrics: " + len(foundLyrics))
        print("--  --  --  --  --  --  --  --  --  --  --  ---")
        for j in foundLyrics:
            print (j, end = ' ')
            print ("==============================================")
    print ("-----------------------------------------------")
    print (" ")
    return()