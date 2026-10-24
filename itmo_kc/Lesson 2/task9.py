tasks = {
    1: ['Полить цветы', 'Забрать посылку'],
    0: ['Покормить кота'],
    2: ['Почитать книгу по программированию'],
    3: ['Ответить на письмо двоюродной сестры']
}

doings = []

for task in tasks:
    for doing in tasks[task]:
        doings.append(doing)

print(doings)

