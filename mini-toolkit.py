# Welcome to Elijah Lategans Python-mini-toolkit!!!
# The exclamation mark with the dotted line is just for decoration


import random
import time

def checker():
    number = int(input('Enter a number please:'))
    if number %2==0:
        print('Please wait for an answer')
        time.sleep(3)
        print(f'{number} is a even number')
        print('!-----------------------------------------!')
    else:
        print('Please wait for an answer')
        time.sleep(3)
        print(f'{number} is a odd number')
        print('!-----------------------------------------!')



def grade_calculator():
    while True:
        grade = int(input('Please go ahead and enter your grade:'))
        if grade > 100 or grade < 0:
            print('Please enter your grade between 1-100')
            print('!-----------------------------------------!')
        else:
            break
 
    if grade >= 90 and grade <= 100:
        print('Checking please wait')
        time.sleep(3)
        print('Grade: A')
        print('!-----------------------------------------!')
    elif grade >= 80 and grade <= 89:
        print('Checking please wait')
        time.sleep(3)
        print('Grade: B')
        print('!-----------------------------------------!')
    elif grade >= 70 and grade <= 79:
        print('Checking please wait')
        time.sleep(3)
        print('Grade: C')
        print('!-----------------------------------------!')
    elif grade >= 60 and grade <= 69:
        print('Checking please wait')
        time.sleep(3)
        print('Grade: D')
        print('!-----------------------------------------!')
    elif grade <=60:
        print('Checking please wait')
        time.sleep(3)
        print('Grade: F')
        print('!-----------------------------------------!')



def motivation():
    generator = [
        'You got this!',
        'Give it your all!',
        'Mistakes means that you are learning',
        'Don`t be to hard on yourself',
        'Discipline over Motivation!',
        'It`s not whether you get knocked down, its whether you get up',
        'Just start!',
        'Life has no remote so get up and change it yourself',
        'Action speak louder than word!'
    ]   

    while True:
        print(random.choice(generator))
        print('!-----------------------------------------!')
        another = input('Would you like me to generate another one?(y/n)')
        if another != 'y':
            print('!-----------------------------------------!')
            break

def guess():
    number = random.randint(1, 10)

    turns = 5

    print('Are you ready!!!')
    print('Game will start in!!')
    print('3')
    time.sleep(1)
    print('2')
    time.sleep(1)
    print('1')

    print('You have 5 guesses so use them wisely!')

    while True:
        choice = int(input('Choose a number between 1-100!'))
        if choice > 100 or choice < 0:
            print('Choose a number between 1-100, lets try again!')

        if choice < number:
            print('You are too low! try again')
            turns-=1
            print(f'You have {turns} guesses left')
            print('!-----------------------------------------!')
        elif choice > number:
            print('You are too high! try again')
            turns-=1
            print(f'You have {turns} guesses left')
            print('!-----------------------------------------!')
        else:
            print('Congratulations!! you guessed it correct!!')
            time.sleep(2)
            print('Thank you for playing!!')
            print('!-----------------------------------------!')
            break

        if turns == 0:
            print('Sorry, looks like you ran out of turns, better luck next time!')
            print('!-----------------------------------------!')
            break



while True:
    print('MENU')
    print('1)Even or Odd Checker')
    print('2)Grade Calculator')
    print('3)Motivation Generator')
    print('4)Number guessing game!')
    print('5)Exit program')
    print('!-----------------------------------------!')

    option = int(input('Please choose an option(1-4)'))
    print('!-----------------------------------------!')
    if option == 1:
        checker()
    elif option == 2:
        grade_calculator()
    elif option == 3:
        motivation()
    elif option == 4:
        guess()
    elif option == 5:
        print('Thank you for using my minitoolkit!')
        break

