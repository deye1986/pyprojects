# pyroulette in development. dave ikin 2021
# roulette simulator

from sys import exit
from random import choice

def roulette():
    numbers = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,
               19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36]
    
    x = choice(numbers)
    print(f' {x} wins.')
    
    again = input('Again? y/n')
    if again == 'y' or again == 'Y':
        roulette()
    else: exit()


roulette()
