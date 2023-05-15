todos = []
while True:
    user_action = input('Type add, show or exit:')
    user_action = user_action.strip()

    match user_action:
        case 'add':
            todo = input('enter a todo; ')
            todos.append(todo)
        case 'show' | 'display': #bitwise or operator
            for item in todos:
               #item = item.title()
                print(item)
        case 'exit':
            break
        case _:              #for wrong commands
            print("wee mzee")
print('bye')


#Coding Exercise 1
#ECreate a program that does the following:

#1. Prompts the user to input the country they are from.

#2. If the user enters the word USA, the program prints out Hello.

#3. If the user enters the word  India, the program prints out Namaste.

#4. If the user enters the word Germany, the program prints out Hallo.
while True:
    Country_of_origin = input('Which country are you from?')
    match Country_of_origin:
        case 'USA':
            print('Hello')
        case 'India':
            print('Namaste')
        case 'Germany':
            print('Hallo')
        case _:
            print('wee mzee')