import random

num = random.randint(1,20)

name = input("Hello! What is your name? ")
print(f'Well, {name}, I am thinking of a number between 1 and 20.')
count = 1
while True:
    n = int(input("Take a guess. "))
    if n == num:
        print(f'Good job, {name}! You guessed my number in {count} guesses!')
        break;
    elif n < num:
        print(f'Your guess is too low.')
        count += 1
    else :
        print(f'Your guess is too big.')
        count += 1