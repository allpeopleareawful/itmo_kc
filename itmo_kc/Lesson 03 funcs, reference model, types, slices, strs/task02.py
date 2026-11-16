# Напишите функцию zip_, которая принимает на вход два списка и «сшивает» их следующим образом, например: Списки [1, 5, 3, 8, 35] и [2, 7, 9] превратятся в [(1, 2), (5, 7), (3, 9)], т. е. сначала берутся первые элементы первого и второго списков и собираются в кортеж, затем вторые элементы первого и второго списков и собираются в кортеж и т. д., пока не дошли до конца самого короткого списка. 

# def zip_(list1: list, list2:list) -> list:
#     list3 = []
#     for i in range(len(int(list1 > list2) * list1 + int(list2 > list1) * list2)):
#             try:
#                 list3.append((list1[i],list2[i]))
#             except:
#                  return list3
            
#     return list3

# def zip_(list1: list, list2: list) -> list:
#     list3 = []
#     for i in range(min(len(list1), len(list2))):
#         list3.append((list1[i], list2[i]))
        
#     return list3

def zip_(list1: list, list2: list) -> list:
    '''returns a list of tuples zipped up to the shortest input list.'''

    return [(list1[i], list2[i]) for i in range(min(len(list1), len(list2)))]

# a, b = [1, 8, 14, 21, 45], [2, 10, 9, 35]
# a, b = [1, 5, 3, 8, 35], [2, 7, 9]
a, b = [], [1, 3, 5, 7]
print(zip_(a,b))