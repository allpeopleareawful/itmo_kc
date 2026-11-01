tasks = {
    1: ['Полить цветы', 'Забрать посылку'],
    0: ['Покормить кота'],
    2: ['Почитать книгу по программированию'],
    3: ['Ответить на письмо двоюродной сестры']
}

answer = []

for task in tasks:
    for doing in tasks[task]:
        if 'кот' in doing:
            answer.append(doing)

print(answer)

