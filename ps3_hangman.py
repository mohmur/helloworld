# 6.00 Problem Set 3
# 
# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string

WORDLIST_FILENAME = "d:/python/words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

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
    #if secretWord==lettersGuessed:
     #   return True
    #else:
     #   return False
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...



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
    
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    

def hangman(secretWord):
    length = len( secretWord )
    guess = int(8)
    guessedword=""
    found=list(secretWord)
    for k in range(0,length):
        found[k] = '_'
    
    print("Welcome to the game Hangman.. ")
    print("I am thinking of a letter that is ", length ," letters long ")
    #print( length )
    print("-----------------------------")
  
    while guess > 0 and found!=secretWord:
        print("You have  ", guess ,"guesses left ")
        av=getAvailableLetters(guessedword)
        print(" Available letters: ", av )
        
        g=input("Please guess a letter : ")
        k=check(guessedword,g) 
        if k==0:            
            guessedword = guessedword + g
            nfound = getGuessedWord(secretWord,guessedword)
            if found == nfound:
                print("OOPs that letter is not in my word : ", nfound )
            else:
                print("Good Guess:", nfound)
            found = nfound
            guess = guess-1
        else:
            print("OOPs! you have already guessed that : ", found )

    if isWordGuessed(secretWord, guessedword):
        print("Congratulations, You Won!!")
    else:
        print("Sorry You ran out of guess the word is ", secretWord)
                          
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE...






# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

def check( word , c ):
    found = int(0) 
    for i in word:
        if i==c:
            found=int(1)
    return found

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
