tasks = {
    1: ['Полить цветы', 'Забрать посылку'],
    0: ['Покормить кота'],
    2: ['Почитать книгу по программированию'],
    3: ['Ответить на письмо двоюродной сестры']
}

answer = []

for priority in tasks:
    if priority > 2: continue

    for doing in tasks[priority]:
        if 'кот' in doing:
            answer.append(doing)

    if len(answer) == 2: break


print(answer)

