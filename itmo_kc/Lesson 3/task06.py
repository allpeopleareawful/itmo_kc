# Напишите функцию sum_as_ints, которая принимает на вход список из строк, пытается привести их к целому числу через int(element) и считает сумму. Список может содержать любые данные, но если они не приводятся через int(element), то программа должна их отбросить.

def sum_as_ints(list1: list) -> int:
    '''Sums int elements in list.'''
    sum = 0
    for element in list1:
        try:
            sum += int(element)
        except ValueError:
            print('В массиве оказалось не целочисленное число')

    return sum

print(sum_as_ints(['3.14', '2.15', '2,2', "q", "a"]))