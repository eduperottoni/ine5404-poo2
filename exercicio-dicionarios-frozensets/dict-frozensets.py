
import random

dict = {}
for i in range(0,10):
    
    tmp_list = []
    cont = 0
    while cont < 30:
        number = random.randint(0,100)
        if number not in tmp_list:
            cont += 1
            tmp_list.append(number)
    frozenset1 = frozenset(tmp_list)

    tmp_sum = 0
    for i in frozenset1:
        tmp_sum += i
    dict[frozenset1] = tmp_sum

print(dict)



