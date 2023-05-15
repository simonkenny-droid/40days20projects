todos = []
while True:
    user_action = input('Type add, show, edit or exit:')
    user_action = user_action.strip()

    match user_action:
        case 'add':
            todo = input('enter a todo; ')
            todos.append(todo)
        case 'show' | 'display': #bitwise or operator
            for item in todos:
               #item = item.title()
                print(item)
        case 'edit':
            number = int(input('Number of the todo to edit: '))
            number = number - 1
            new_todo = input('Enter a new todo; ')
            todos[number] = new_todo

        case 'exit':
            break
        case _:              #for wrong commands
            print("wee mzee")
print('bye')


#code experiments

#bonus material; data mutability
filenames = ['1.Raw Data.txt', '2.Reports.txt', '3.Presentations.txt']

for filename in filenames:
    filename = filename.replace('.', '-', 1)
    print(filename)

#tuples;immutable vesion of a list;use round paranthesis insteadof square
filenames = ('1.Raw Data.txt', '2.Reports.txt', '3.Presentations.txt')
print(type(filenames))