# В этом задании Вам понадобится написать функцию find_substr,  которая принимает на вход два аргумента: подстроку (любой длины) и строку, в которой нужно ее искать, и возвращает кортеж, представляющий собой пару [start, stop) первой позиции, где найдено слово.

def find_substr(substring: str, string: str) -> tuple | None:
    '''Finds first substring in string.'''
    for i in range(len(string)):
        candidate = string[i:i + len(substring)]
        if candidate == substring:
            return (i, i + len(substring))

    return

def find_substr2(substring: str, string: str) -> tuple | None:
    if not substring:
        return (0, 0)

    sub_len = len(substring)
    for i in range(len(string) - sub_len + 1):
        candidate = string[i:i + sub_len]
        if candidate == substring:
            return (i, i + sub_len)

    return

def find_substr_short(substring: str, string: str) -> tuple | None:
    start = string.find(substring)
    return (start, start + len(substring)) if start != -1 else None

print(find_substr("мы", "Летом мы хотим отдыхать на море"))
print(find_substr("иа", "маленькая машина"))

        

