# В этом задании потребуется написать функцию process_string, которая приводит строку[1:] к нижнему регистру и заменяет все слова 'intern' на 'junior'.

def process_string(string: str) -> str:
    result = string[1:].lower().replace('intern', 'junior')

    return result

print(process_string('IIntern reads a lot of books'))
