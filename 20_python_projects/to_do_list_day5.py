#enumerate #fstrings
todos = []
while True:
    user_action = input('Type add, show, edit, complete or exit:')
    user_action = user_action.strip()

    match user_action:
        case 'add':
            todo = input('enter a todo; ')
            todos.append(todo)
        case 'show' | 'display': #bitwise or operator
            for index, item in enumerate(todos):
                row = f"{index}-{item}" #use of f-string
               #item = item.title()
                print(row)
        case 'edit':
            number = int(input('Number of the todo to edit: '))
            number = number - 1
            new_todo = input('Enter a new todo; ')
            todos[number] = new_todo
        case 'complete':
            number = int(input('Number of the todo to complete: '))
            todos.pop(number)
        case 'exit':
            break
        case _:              #for wrong commands
            print("wee mzee")
print('bye')

#code experiments
waiting_list = ['sem', 'ben', 'john']
                                        #output should be
                                        #1.Ben
                                        #2.John
                                        #3.Sen
waiting_list.sort()
for index, item in enumerate(waiting_list):
    row = f"{index+1}.{item.capitalize()}"
    print(row)