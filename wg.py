def isWordGuessed(secretWord, lettersGuessed):
    found = int(0)
    for i in secretWord:
        found = int(0)
        for j in lettersGuessed:
            if i==j :
                found=int(1)
        if found==0:
            break
    if found==1:
        return True
    else:
        return False
