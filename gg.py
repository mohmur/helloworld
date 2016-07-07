def getGuessedWord(secretWord, lettersGuessed):
    length = len( secretWord )
    print(length)
    find = ""
    found=list(secretWord)
    for k in range(0,length):
        found[k] = '_'
    for j in lettersGuessed:
            c=int(0)
            for i in secretWord:
                if j==i and found[c] == '_':
                    found[c] = i
                c = c + 1
    return(found)
