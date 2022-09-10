import random

def check_input(display):
    while True:
        guess = input('Input a letter: ')
        if guess == '' or len(guess) >= 2:
            print("Please, input a single letter\n")
            print("".join(display))
            continue
        elif guess.isupper() or guess.isalpha() == False:
            print("Please, enter a lowercase letter from the English alphabet.\n")
            print("".join(display))
            continue
        else:
            break
    return guess

def printing(g,w,d):
    c_index = []
    for i, letter in enumerate(w):
        if letter == g:
            c_index.append(i)
    for j in c_index:
        d[j] = g
    print('')
    print("".join(d))
    return d

def main_calculus(display,word):
    n_of_attempts = 8
    final = []
    guess_list = []
    checking_set = set(word)    
    
    while n_of_attempts > 0:
        guess = check_input(display)
        if guess in guess_list:
            print("You've already guessed this letter.\n")
            print("".join(display))
            continue

        elif guess in final:
            n_of_attempts -= 1
            print(f"No improvements. # {n_of_attempts} attempts\n")
            print("".join(display))
            guess_list.append(guess)
            continue

        elif guess in checking_set:
            final = printing(guess,word,display)
            guess_list.append(guess)
            if "".join(final) == word:
                return True 

        elif guess not in checking_set:
            n_of_attempts -= 1
            print(f"That letter doesn't appear in the word.  # {n_of_attempts} attempts\n")
            print("".join(display))
            guess_list.append(guess)
            continue
    return False

def playing_the_game():
    lost = 0
    won = 0
    print(f"H A N G M A N  # 8 attempts\n") 
    while True:
        menu = input('Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit:')
        
        if menu == 'play':
            words = ['python', 'java', 'swift', 'javascript']
            word = random.choice(words)
            display = list("-"*len(word))
            print('')
            print("".join(display))
            if main_calculus(display,word) == True:
                print(f"You guessed the word {word}!\nYou survived!")
                won += 1
                continue
            else:
                print("You lost!")
                lost =+ 1
                continue
        elif menu == 'results':
            print(f"You won: {won} times.\nYou lost: {lost} times.")
            continue
        elif menu == 'exit':
            break
    
playing_the_game()