# This is my number guesser game.
import random

guessesTaken = 0

print('Welcome to the Number Guesser Game!')

number = random.randint(1,100)
print('I am thinking of a number between 1 and 100.')

while guessesTaken < 10:
    print('Try me, bro! Cause it is HIGH NOON!')
    guess = input()
    guess = int(guess)
    guessesTaken = guessesTaken + 1
    if guess < number:
        print('You know what grinds my gears? WHEN SMART PEOPLE GET THIS WRONG!')
        print('COME ON! The answer is right in front of you! JUST DO IT!')
        print('Too low.')
    if guess > number:
        print('Does it hurt when I touch you because you got it wrong? Because I think you need medical assistance.')
        print('I have a few concerns.')
        print('Too high.')
    if guess == number:
        break
    
if guess == number:
    guessesTaken = str(guessesTaken)
    print('Conglaturations! You guessed my number in '+ guessesTaken + ' guesses!')
    print('Made by Iain Thorpe and Edward Gallegos.')
    print('Thanks to Baymax, Jesse Mccree, Shia LaBeouf, Family Guy, Ghostbusters, Crash Bandicoot, that random meme, and Cooking Mama for their memes.')
if guess !=number:
    number = str(number)
    print('YOU FAILED! To guess ' + number)
    print('Try again!')
