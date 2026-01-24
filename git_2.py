f = open('travels.txt', 'r', encoding='utf-8-sig')
gruz_1 = 0
massa_1 = 0
gruz_2 = 0
massa_2 = 0
gruz_3 = 0
massa_3 = 0
gruz = 0
for i in f:
    L = i.split()
    print(L)
    if int(L[0]) == 1:
        gruz_1 += 1
        massa_1 += int(L[6])
        gruz = '1.10'
    if int(L[0]) == 2:
        gruz_2 += 1
        massa_2 += int(L[6])
        gruz = '2.10'
    if int(L[0]) == 3:
        gruz_2 += 1
        massa_2 += int(L[6])
        gruz = '3.10'

if (gruz_1 > gruz_2) and (gruz_1 > gruz_3):
    print('В этот день было больше всего груза ', gruz, 'Вот его суммарный объем ', massa_1)

if (gruz_2 > gruz_1) and (gruz_2 > gruz_3):
    print('В этот день было больше всего груза ', gruz, 'Вот его суммарный объем ', massa_2)

if (gruz_3 > gruz_1) and (gruz_3 > gruz_2):
    print('В этот день было больше всего груза ', gruz, 'Вот его суммарный объем ', massa_3)