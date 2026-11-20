tasks = {
    1: ['Полить цветы', 'Забрать посылку'],
    0: ['Покормить кота', 'Покормить кота'],
    2: ['Почитать книгу по программированию'],
    3: ['Ответить на письмо двоюродной сестры']
}

new_tasks = {}

for priority in tasks:
    new_tasks[priority] = list(set(tasks[priority]))



print(new_tasks)

