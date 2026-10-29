# В этом задании необходимо написать функцию check_string, которая сначала проверяет строку на наличие лишних символов пробела слева и справа. Если есть лишние пробелы, то тогда мы считаем строку неверной. Затем проверяет, что только первое слово начинается с большой буквы, а остальные с маленькой, и в конце проводит проверку, что последний символ является точкой.

def check_string(string: str) -> bool:
    if string.strip() != string:
        return False
    elif not (string[0].isupper() and string[1:].islower()):
        return False
    elif not (string[-1] == '.'):
        return False
    else:
        return True

def check_string2(string: str) -> bool:
    # 1. Проверяем на пустую строку и лишние пробелы по краям
    if not string or string.strip() != string:
        return False
    
    # 2. Проверяем, что последний символ — точка
    if not string.endswith('.'):
        return False
    
    # 3. Проверяем регистр: первая буква заглавная, остальные строчные
    # Отрезаем точку в конце, чтобы корректно обрабатывать одиночные буквы (например, "А.")
    content = string[:-1]
    return content[0].isupper() and (len(content) == 1 or content[1:].islower())

print(check_string2('В этом году будет особенно теплое море.'))
print(check_string2('В этом году будет особенно теплое Mоре.'))
print(check_string2('В этом году будет особенно теплое море'))
print(check_string2(' В этом году будет особенно теплое море'))