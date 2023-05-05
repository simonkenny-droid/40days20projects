user_prompt = 'Enter a todo; '

todos = []
while True:
    todo = input(user_prompt)
    print(todo.capitalize()) # prints out the name once with the first letter capitalized.
    todos.append(todo)
    print(todos)

    
