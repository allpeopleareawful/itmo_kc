# много другого кода, который тоже печатает
# ...

# код функции для отладочной печати

def print_array(list1: list) -> None:
    print('###')
    print(list1)
    print('###')

# Код коллеги

def math_task(data):
    answer = []
    # возводим в третью степень
    for elem in data:
        answer += [elem ** 3]
    print_array(answer)
    # берем остаток от деления на 7
    for i in range(len(answer)):
        answer[i] = answer[i] % 7
    print_array(answer)
    # прибавляем к остатку изначальный массив
    for i in range(len(answer)):
        answer[i] = answer[i] + data[i]
    # возвращаем результат
    print_array(answer)
    return answer

math_task(test_data)
# print(math_task([1, 4, 5, 9])) # пример для самопроверки
    