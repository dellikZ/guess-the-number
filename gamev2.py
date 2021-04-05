from random import randint

def valid(func):
    def wrapper(*args, **kwargs):
        while True:
            try:
                func(*args, **kwargs)
            except TypeError:
                print('Please do not break my program.')
                continue
            except ValueError:
                print('Please do not break my program.')
                continue
            else:
                break
    return wrapper


def welcome():
    print('Welcome to the second version of my Guess the Number game!')
    print('I really hope that you will find it interesting.')

def option():
    print('Press Y to play or N to exit.')
    choice = str(input())
    if choice == 'Y' or choice == 'y':
        print("Let's play!")
    elif choice == 'N' or choice == 'n':
        input('Press ENTER to exit.')
        exit()
    else:
        invalid = True
        while invalid == True:
            print('Please pick a valid option:')
            choice = str(input())
            if choice in ['Y', 'y', 'N', 'n']:
                invalid = False



@valid
def guess():
    pc_num = randint(1, 20)
    print('The computer generated a number in the [1, 20] range.\nGuess it!\n')
    player_num = int(input())
    guessed_it = False
    while guessed_it == False:
        if player_num < pc_num and player_num in range(1, 21):
            player_num = int(input('The number is bigger than what you picked. Try again:\n'))
        if player_num > pc_num and player_num in range(1, 21):
            player_num = int(input('The number is smaller than what you picked. Try again:\n'))
        if player_num == pc_num:
            print(f'Awesome! You guessed it! The number was {pc_num}!')
            guessed_it = True
        if player_num not in range(1, 21):
            condition = True
            while condition == True:
                print('Please enter a number in the given range:\n')
                player_num = int(input())
                if player_num in range(1, 21):
                    condition = False

def play_again():
    print('Do you want to play again?')
    print('Type Y or N:\n')
    choice = str(input())
    if choice in ['Y', 'y']:
        while choice in ['Y', 'y']:
            guess()
            choice = str(input('Play again? [Y/N]:\n'))
    if choice in ['N', 'n']:
        input('Press ENTER to exit.')
    if choice not in ['Y', 'y', 'N', 'n']:
        invalid = True
        while invalid == True:
            print('Please choose a valid option\n')
            choice = str(input())



welcome()
option()
guess()
play_again()