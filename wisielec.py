from time import sleep
from random import *
import sys


def tries_names():
    if tries > 1 or tries == 0:
        print("{} tries left.".format(tries))
    else:
        print("{} try left.".format(tries))    


def drawing_hangman(tries):
    if tries == 0:
        print('''
______
|    |
|    O
|   /|\\
|   / \\
|    
----------
        ''')
    if tries == 1:    
        print('''
______
|    |
|    O
|   /|\\
|   / 
|    
----------
        ''')
    if tries == 2:    
        print('''
______
|    |
|    O
|   /|\\
|    
|    
----------
        ''')
    if tries == 3:
        print('''
______
|    |
|    O
|   /|
|   
|    
----------
        ''')
    if tries == 4:    
        print('''
______
|    |
|    O
|    |
|   
|    
----------
        ''')
    if tries == 5:    
        print('''
______
|    |
|    O
|   
|    
|    
----------
        ''')
    if tries == 6:    
        print('''
______
|    |
|    
|   
|    
|    
----------
        ''')
    if tries == 7:    
        print('''
______
|    
|    
|   
|    
|    
----------
        ''')
    if tries == 8:    
        print('''       
|    
|    
|   
|    
|    
----------
        ''')
    if tries == 9:    
        print('''         
----------
''')
    


word_list = ['zebra', 'car', 'cat', 'dog', 'tree', 'python', 'java', 'programming', 'letter', 'computer', 'science']
word = choice(word_list)

under_lines = list(word)

for under_line in range(len(under_lines)):
    under_lines[under_line] = '_'

tries = 10
all_tries = []
word_tries = []
print("Hangman Game")
while True:
    
    if tries > 0:
        
        print(" ".join(under_lines))
        
        if '_' not in under_lines:
            print(f"You guessed the word which was {word.upper()}!")
            sys.exit()
        guess = input("Type in the letter >>> ")

        if guess.lower() == word:
            print(f"You guessed the word which was {word.upper()}!")
            sys.exit()
        if guess.isalpha():            
            if len(guess.lower()) == len(word):
                if guess not in word_tries:
                    print("It's not the correct word!")
                    tries -= 1
                    drawing_hangman(tries)
                    word_tries.append(guess)
                    tries_names()

                else:
                    print("You have already typed in this word! It's not correct!")
            elif len(guess.lower()) == 1:
                if guess.lower() in under_lines or guess in all_tries :
                    print("You have already typed in this letter!")
                elif guess.lower() in word:
                    msg_send = True
                    for num, char in enumerate(word):
                        if char == guess.lower():
                            if msg_send:
                                print("You guessed it!")
                                msg_send = False
                            under_lines[num] = guess.lower()

                            
                else:
                    print("You didn't guess it!")
                    all_tries.append(guess.lower())
                    tries -= 1
                    tries_names()
                    drawing_hangman(tries)

            elif len(guess) > 1:
                print(f'Enter ONE letter or a {len(word)} letter word! -> Your word is {len(guess)} letters long')
                sleep(1)
        else: 
            print("Enter a letter")
            sleep(1)
    else:
        print(f"You run out of tries! U lost! The word was {word.upper()}")
        sys.exit()
                        
