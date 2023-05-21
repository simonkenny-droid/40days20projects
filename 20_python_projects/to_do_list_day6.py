#text files #file paths
while True:
    user_action = input('Type add, show, edit, complete or exit:')
    user_action = user_action.strip()

    match user_action:
        case 'add':
            todo = input('enter a todo; ') + "\n" #breakline

            file = open('files/todos.txt', 'r')
            todos = file.readlines()
            file.close()

            todos.append(todo)

            file = open('files/todos.txt', 'w')
            file.writelines(todos)
            file.close()
        case 'show' | 'display': #bitwise or operator
            file = open('files/todos.txt', 'r')
            todos = file.readlines()
            file.close()

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

#bonus example; create files for lists
contents = ["sex sex sex.",
            "with wit wiy with",
            "gfhhh vffd bmkkk."]

filenames = ["doc.txt", "report.txt", "presentation.txt"]

for content, filename in zip(contents, filenames):
    file = open(f"files/{filename}", 'w')
    file.write(content)