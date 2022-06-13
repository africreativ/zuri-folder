import random

options = ['r', 'p', 's']
outcomes = ['R - Rock', 'P - Paper', 'S - Scissors']


print('Lets play a game of Rock-Paper-Scissors')

while True:
    while True:
        print('Pls enter one of the 3 options below')
        for item in outcomes:
            print(item)
        cpu = input('Enter a letter: ').lower()

        if cpu in options:
            break

        print(' Worng selection!')
        continue

    player = random.choice(options)

    print(f'Player {cpu} : CPU {player}')

    if cpu == ('r') and player == ('p'):
        print('You lost!')
    elif cpu == ('p') and player == ('r'):
        print('You won!')
    elif cpu == ('r') and player == ('s'):
        print('You won!')
    elif cpu == ('s') and player == ('r'):
        print('You lost!')
    elif cpu == ('p') and player == ('s'):
        print('You lost!')
    elif cpu == ('s') and player == ('p'):
        print('You won!')
    else:
        print('We have a tie. Lets play again')
        continue

    break
