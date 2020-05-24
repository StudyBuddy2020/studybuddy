'''Here I made a hangman code with python. I was wondering a better way to do 2 tasks in general for all python coding:

Firstly, I was wondering how I could make a better split method so the payer would not have to put each letter individually for the word.

Secondly, how do I create multiple windows to play the program in. I am currently using the terminal at the bottom but I wondered if there was anything near JoptionPane like there is in Java, which allows you to create and configure pages and take proper inputs.  

In every other sense this works so its fun to play, but I would love to be able to use more object oriented coding with python.'''

print("Welcome to Hangman!!")

numletters = int(input("How many letters are in your word? "))
category = input("What is the category? ")


showing = []
word = []
final = []
i = 0
b = numletters
while i< b:
    letters = input("Input one letter at a time: ")
    showing.append(letters)
    word.append(" -- ")
    final.append(letters)
    i = i+1
numStrikes = int(input("How many strikes? ")) 

lettersleft = numletters
strike = 0
attempt = 1
strikesLeft = numStrikes - strike

while strikesLeft > 0 and lettersleft>0:
    print(''.join(word)) 
    guess = input("Guessing time! There are " + str(numletters) + " letters and the category is " + category + " and you have " + str(strikesLeft) + " strikes left: ")
    
    b = 0
    n = 0
    while b < numletters:
        if guess == showing[b]:
            word[b] = showing[b]
            b = b+1
            n = 1
            attempt = attempt + 1
            lettersleft = lettersleft-1
        else:
            b = b+1

        if b == numletters and n == 0:
            print("Sorry, incorrect")
            attempt = attempt + 1
            strike = strike + 1
            strikesLeft = strikesLeft - 1 
            b = 0
            break
    if strikesLeft == 0:
        print("Sorry, you lose! The word was:")
        print(''.join(final)) 

    if lettersleft == 0:
        print(''.join(word)) 
        print("You win!!!")       
        break