
# Instructions
def instructions():
    print('_________________________________________________________________________')
    print()
    print('              HI, WELCOME TO THE MASTERMIND COMPUTER GAME!               ')
    print('_________________________________________________________________________')
    print()
    print('-------------------------------HOW TO PLAY?------------------------------')
    print()
    print('1. This is an on-screen version of the board game.')
    print()
    print('2. There are a total of 4 colours in this game, which are: ')
    print('   B = Blue , G = Green , R = Red , Y = Yellow')
    print()
    print('3. The colours will be put in a random order.')
    print()
    print('4. Guess the colours by entering the first letter of the colours.')
    print('   You must also use "uppercase letters" when entering the colours.')
    print()
    print('5. You must guess the 4 colours in the correct position.')
    print('   You can choose the same colours more than once.')
    print('   For example: BBGY')
    print()
    print('6. The program will then show:')
    print('   i)  How many correct colours and in the correct position.')
    print('   ii) How many correct colours but in the wrong position.')
    print()
    print('8. You only have 10 attempts to enter the 4 correct colours in')
    print('   the correct position.')
    print()
    print('9. GOOD LUCK!')
    print()

    # Ask if the user wants to start the game
    while True:
        start_game = input('Do you want to start the game? [Y/N]: ')
        print()

        # If the user enters Y
        if start_game == 'y' or start_game == 'Y':
            player_name = input('Plese enter your name: ')
            print()
            print('The game will start now. Good luck,', player_name,'!')
            print()
            print('Generating the colours now...')
            print()
            #break
            game()
        # If the user enters N
        elif start_game == 'n' or start_game == 'N':
            print('All right, see you next time.')
            quit()
        # If the user enters anything other than Y or N
        else:
            print('Error! Please select Y or N: ')
            print()


# Generate 4 random colours using the library
# There are a total of 4 colours in this game
import random
colours_list = ['B', 'G', 'R', 'Y']
random_list = random.choices(colours_list, k=4)
attempt = []

# Start game
def game():
    choice_list = []
    while True:
        # The user will choose the colours for each position
        choice_1 = input('Enter the first colour: ').upper()
        print()
        if choice_1 != 'B' and choice_1 != 'G' and choice_1 != 'R' and choice_1 != 'Y':
            print('ERROR! Your choice is not in the list.')
            print()
            game()
        choice_2 = input('Enter the second colour: ').upper()
        print()
        if choice_2 != 'B' and choice_2 != 'G' and choice_2 != 'R' and choice_2 != 'Y':
            print('ERROR! Your choice is not in the list.')
            print()
            game()
        choice_3 = input('Enter the third colour: ').upper()
        print()
        if choice_3 != 'B' and choice_3 != 'G' and choice_3 != 'R' and choice_3 != 'Y':
            print('ERROR! Your choice is not in the list.')
            print()
            game()
        choice_4 = input('Enter the last colour: ').upper()
        print()
        if choice_4 != 'B' and choice_4 != 'G' and choice_4 != 'R' and choice_4 != 'Y':
            print('ERROR! Your choice is not in the list.')
            print()
            game()

        # Store the user's choice into the choice_list()
        choice_list.insert(0, choice_1)
        choice_list.insert(1, choice_2)
        choice_list.insert(2, choice_3)
        choice_list.insert(3, choice_4)

        idx = 0

        # Result list
        res_wrong_place = []
        res_correct_place = []

        for i in random_list:
            if i == choice_list[idx]:
                res_correct_place.append(idx)
            elif i in choice_list and i != choice_list[idx]:
                res_wrong_place.append(idx)
            idx = idx + 1

        print("Correct color but in the wrong place:\n",len(res_wrong_place))
        print("Correct color and in the correct place:\n",len(res_correct_place))
        print()
        attempt.append('try')

        if len(res_correct_place) == 4:
            print('Congratulations! You took', len(attempt), 'attempt(s)!')
            print()

            try_again = input('Would you like to play again? [Y/N]: ')
            print()


            # If the user enters Y
            if try_again == 'y' or try_again == 'Y':
                attempt.clear()
                instructions()

            # If the user enters N
            elif try_again == 'n' or try_again == 'N':
                print('All right, see you next time.')
                quit()
            # If the user enters anything other than Y or N
            else:
                print('Error! Please select Y or N: ')
        else:
            if len(attempt)  ==  10 :
                print('GAME OVER! You have reached the maximum attempts.')
                #print()
                print('The correct order is: ', random_list)
                #print()

                # If the user enters Y
                try_again = input('Would you like to play again? [Y/N]: ')
                print()
                if try_again == 'y' or try_again == 'Y':
                    attempt.clear()
                    instructions()
                 # If the user enters N
                elif try_again == 'n' or try_again == 'N':
                    print('All right, see you next time.')
                    quit()
                # If the user enters anything other than Y or N
                else:
                    print('Error! Please select Y or N: ')
            game()

instructions()
game()
