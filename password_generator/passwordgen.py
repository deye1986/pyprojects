# Pypassword picker. Dave Ikin
# outputs password to terminal.
# minimum password security could be bruteforce about 10 years for a 11 character, about
# quarter of a million years for one with fourteen

from random import choice, randrange
from string import punctuation
from sys import exit

def pwordpicker():
    '''Make a password with a minimum 11 character length'''
    
    adjectives = ['smelly', 'fatty', 'handsome', 'orange', 'yellow', 'stinky', 'brave']
    nouns = ['apple', 'microsoft', 'panda', 'google', 'nike', 'reebok', 'dragon', 'hammer']

    print('Welcome to Password Picker! David Ikin 2020.')
    print('It could take a password cracker over eleven years to crack these!')
    print('and they will be easy to remember......')

    
    for num in range(1):
        adjective = choice(adjectives)
        noun = choice(nouns)
        number = randrange(0, 10)
        special_char = choice(punctuation)

        password = str(number) + adjective + special_char + noun 
        print(f'Your new password is ***> {password} <***')

        
        exit()
        
        

pwordpicker()