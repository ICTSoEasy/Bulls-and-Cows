#Bulls and Cows

import random

def generateNumber():
    digits = ['0','1','2','3','4','5','6','7','8','9'] #List the digits we will be using
    sample = random.sample(digits,4)
    results = ''.join(sample)
    return results

def checkLength(tocheck):
    if len(tocheck) == 4: #Check the length
        return True
    else:
        print('Sorry, this entry is not four digits.')
        return False

def checkInt(tocheck):
    try:
        intEntry = int(tocheck) #Convert to integer
    except:
        print('Sorry, this entry consists of something other than digits')
        return False #Error so it wasn't an integer
    return True #No error so must be

def checkUnique(tocheck):
    for char in tocheck:
        if tocheck.count(char) != 1:
            print('Sorry, this entry has duplicate entries')
            return False
    return True

def checkBulls(toCheck,randomNumber):
    numBulls = 0
    for i in range(4):
        if toCheck[i] == randomNumber[i]:
            numBulls+=1
    return numBulls

def mainProgram():
    numGuesses = 0
    randomNumber = generateNumber()
    while True: #Python's answer to the repeat loop
        #print(randomNumber) #Comment/uncomment to hide/show the number we're trying to guess!
        entry = input('Input \'exit\' or your 4-digit attempt: ') #Get the user's input
        numGuesses += 1
        if entry == 'exit': #They've chosen to exit
            print('The random number was',randomNumber)
            print('Quitting. Bye.')
            break #Leave the loop
        if entry == randomNumber: #They got it right
            print('Correct, well done!')
            print('You took',numGuesses,'guesses.')
            break #Leave the loop
        if checkLength(entry) and checkInt(entry) and checkUnique(entry):
            numBulls = checkBulls(entry,randomNumber)
            numCows = checkCows(entry,randomNumber,numBulls)
            print('You have found',numBulls,'bulls.')
            print('You have found',numCows,'cows.')
        else:
            print('Please try again') #Invalid entry, prompt for repeat
            numGuesses -= 1