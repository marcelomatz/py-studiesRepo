# NÃO TERMINADO

def show_op(todo_list):
    print()
    print('Tarefas')
    print(todo_list)
    print()


if __name__ == '__main__':
    todo_list = []
    redo_list = []

    while True:
        todo = input(
            'Digite uma tarefa ou o comando que você deseja | undo, redo, ls: ')

        if todo = 'ls':
            show_op(todo)
            continue
        elif todo == 'undo':
            ...
            continue
        elif todo == 'redo':
            do_redo()
            ...
            continue

        do_add(todo, todo_list)
