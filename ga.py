def getAvailableLetters(lettersGuessed):
    avail = "abcdefghijklmnopqrstuvwxyz"
    new=""
    count = len(lettersGuessed)
    for i in lettersGuessed:
        found = int(0)
        for j in avail:           
            if i!=j:
                new = new + j
        avail = new
        new = ""               
              
    print(avail)
    return avail
