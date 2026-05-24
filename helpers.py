import random #needed to generate a random motivational quote from a list 
import time 

def checker():
    while True: 
        #ask the user to enter a number
        #Repeats the program so the user continously enter numbers
        number = int(input('Enter a number please:'))

        if number %2==0: #checks if the number is even or odd
            print('Please wait for an answer')
            time.sleep(2)
            print(f'{number} is a even number')
            print('!-----------------------------------------!')
        else:
            print('Please wait for an answer')                          
            time.sleep(2)
            print(f'{number} is a odd number')
            print('!-----------------------------------------!')

        while True:  
            #will keep asking a user to enter a number until they choose "n"
            again = input('Want to try again?(y/n)')
            if again == 'y':
                break                  
            elif again == 'n':
                print('Goodbye!')
                break
            else:
                print('Please enter y/n')
        
        if again == 'n':
            break



def grade_calculator():
    while True:
        grade = int(input('Please go ahead and enter your grade:')) #if a user enters a number below 0 or above 100 it will ask bring the user back here

        if grade >= 90 and grade <= 100:
            print('Checking please wait')
            time.sleep(3)
            print('Grade: A')
            print('!-----------------------------------------!')
            break
        elif grade >= 80 and grade <= 89:
            print('Checking please wait')
            time.sleep(3)
            print('Grade: B')
            print('!-----------------------------------------!')
            break
        elif grade >= 70 and grade <= 79:
            print('Checking please wait')
            time.sleep(3)
            print('Grade: C')
            print('!-----------------------------------------!')
            break
        elif grade >= 60 and grade <= 69:
            print('Checking please wait')
            time.sleep(3)
            print('Grade: D')
            print('!-----------------------------------------!')
            break
        elif grade < 60:
            print('Checking please wait')
            time.sleep(3)
            print('Grade: F')
            print('!-----------------------------------------!')
            break
        elif grade > 100 or grade < 0:
            print('Please enter grade 1-100') #Makes sure that the user only enters a number between 1-100
        else:
            break



def motivation():
    generator = [  #stores all the motivational quotes
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

    while True: #Will keep asking the user if they would like another quote to be generated until the user enters "n"
        print(random.choice(generator)) #Chooses a motivational quote at random from the generator and displays it
        print('!-----------------------------------------!')
        another = input('Would you like me to generate another one?(y/n)') 
        if another != 'y':
            print('EXIT')
            print('!-----------------------------------------!')
            break


def guess():
    number = random.randint(1, 100) #Generates a number between 1-100

    turns = 0

    print('Are you ready!!!')
    print('Game will start in!!')
    print('3')
    time.sleep(1)
    print('2')
    time.sleep(1)
    print('1')

    while True:
        #Used to keep asking the user to enter a number until they have ran out of turns or have guessed it correct
        choice = int(input('Choose a number between 1-100!'))

        if choice < number:
            print('You are too low! try again')
            turns+=1 #After every turn the variable turn is incremented by 1
        elif choice > number:
            print('You are too high! try again')
            turns+=1
        else:
            print('Congratulations!! you guessed it correct!!')
            time.sleep(2)
            print('Thank you for playing!!')
            print('!-----------------------------------------!')
            break

        if turns == 5: #Once turns have been incremented till 5 the loop breaks and ends the game 
            print('Sorry, looks like you ran out of turns, better luck next time!')
            print('!-----------------------------------------!')
            break

