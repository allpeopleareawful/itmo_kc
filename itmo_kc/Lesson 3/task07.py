# Напишите реализацию reversed_, в которой не будет проблемы из прошлого пункта.

# Оба варианта проверочного кода должны выдать Все хорошо.

def reversed_(array):
    tmp = array.copy()
    rv = []
    while tmp:
        rv.append(tmp.pop())
    return rv

def reversed2(array):
    rv = []
    for i in range(len(array)):
        rv.append(array[(-i - 1) + len(array)])

    return rv

def reversed3(array):
    return array[::-1]
    

if reversed_(reversed_([1, 2, 3])) == [1, 2, 3]:
    print("Все хорошо")
else:
    raise RuntimeError("Ошибка, после обращения дважды не получается исходный массив!")

arr = [1, 2, 3]
if reversed_(reversed_(arr)) == arr:
    print("Все хорошо")
else:
    raise RuntimeError("Ошибка, после обращения дважды не получается исходный массив!")