
# Welcome to Elijah Lategans Python-mini-toolkit!!!


import helpers

def display_menu():
    print("!-----------------------------------------!")
    print('MENU')
    print('1)Even or Odd Checker')
    print('2)Grade Calculator')
    print('3)Motivation Generator')
    print('4)Number guessing game!')
    print('5)Exit program')
    print('!-----------------------------------------!')

def menu():
    while True:
        display_menu()
        option = int(input('Please choose an option(1-5)'))
        print('!-----------------------------------------!')
        if option == 1:
            helpers.checker()
        elif option == 2:
            helpers.grade_calculator()
        elif option == 3:
            helpers.motivation()
        elif option == 4:
            helpers.guess()
        elif option == 5:
            print('Thank you for using my minitoolkit!')
            break

menu()


