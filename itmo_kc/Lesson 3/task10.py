# В этом задании вам потребуется написать функцию fifth_element, которая возвращает в виде списка, каждый пятый элемент исходного списка в обратном порядке, начиная с пятого с конца.

def fifth_element(some_list: list) -> list | None:
    '''Returns each fifth element from list (reversed).'''
    return some_list[-5::-5]

print(fifth_element(['e',6,8,'A','>','^','S','$','R','C',6,'+','#',9,'/',1,'T','!','%','K',7,'-','O','*','<',2,'h',4,'g']))
print(fifth_element(['e',6,8,'A',]))