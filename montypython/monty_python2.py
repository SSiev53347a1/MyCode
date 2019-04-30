#!/usr/bin/env python3

round = 0
while(True):
    round = round + 1
    print('Finish the movie title, "Monty Python\'s The Life of ________"')
    answer = input()
    if (answer == 'Brian' or answer == 'brian'):
        print('Correct')
        break
    elif (answer == 'shrubbery'):
        print('You gave the super secret answer!')
    elif (round==3):
        print('Sorry, the answer was Brian.')
        break
    else:
        print('Sorry, Try again!')

