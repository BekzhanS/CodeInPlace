"""
This game will ask a user to try to guess celebrity height in meters
User will have 3 guesses in order to come up with an answer
"""
import random
NUMBER_GUESS = 3    # Player will have this number of guesses
HEIGHT_TOL = 0.05  # 5 cm handicap to player's guess
def main():
    # use dictionary with names/heights pairs
    celeb_height = {}
    with open('celeb_height.txt') as f:
        for line in f:
            (key, val) = line.split(",")
            celeb_height[key] = float(val)
    # create a list with celebrity names to choose randomly later on by index
    list_of_names = list(celeb_height.keys())
    # print intro
    print('Try to guess celebrity height in meters. You will have '+str(NUMBER_GUESS)+' guesses.')
    print()
    count_guess = 0
    selected_name = random.choice(list_of_names)    # randomly select celebrity from a list
    height_val = celeb_height.get(selected_name)   # ask dict to get height for selected name

    while count_guess < NUMBER_GUESS:
        user_guess = float(input('What is height of '+ str(selected_name) + ' in m?: '))
        if (height_val - HEIGHT_TOL) <= user_guess <= (height_val + HEIGHT_TOL):
            print('You won! Exact height of ' + str(selected_name) + ' is ' + str(height_val) + 'm')
            count_guess = NUMBER_GUESS
        else:
            count_guess += 1
            print('You have ' + str(NUMBER_GUESS - count_guess) + ' guesses left')
            print()
    print('Game is over')

if __name__ == '__main__':
    main()