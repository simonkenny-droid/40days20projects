#Coding Exercise 1
#Write a Python program following the steps below:

#1. Create a variable (any name) and store a string in the variable.

#2. Then, print out the type of the variable.

widget = 'button'
print(type(widget))

#Coding Exercise 2
#Write a Python program that gets input from the user and prints out that input.

user_input = input("Please enter some text: ")
print("You entered: " + user_input)

#Coding Exercise 3
#Create a list of four strings and associate the list with a variable

my_list = ["apple", "banana", "orange", "grape"]
print('your list is ' + str(my_list))



my_list = ["apple", "banana", "orange", "grape"]
list_str = ", ".join(my_list)
print(f"Your list is: {list_str}")

#Q2. Should a function argument be a variable or a value?

#A2: It can be either way, depending on the scenario.

#It is OK to provide the value (e.g., a string) directly as an argument:

#user_input = input("Enter a value:")



#But it is also OK to provide the variable associated with the value:
#message = "Enter a value:"
#user_input = input(message)

#Create a program that prompts the user to input their name once. Then, the program prints out the name once with the first letter capitalized.

user_name = input('what is your name? ')
print(user_name.capitalize())

#Create a program that prompts the user to input their name once. Then, the program repeatedly prints out the name with the first letter capitalized.

name = input('your name is; ')
#while True:
print(name.capitalize())


# Create a program that prompts the user to input their name repeatedly. Then, the program repeatedly prints out the name with the first letter capitalized.



while True:
    the_names = input('insert name here; ')
    print(the_names.capitalize())