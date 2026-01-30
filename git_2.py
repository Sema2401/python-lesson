f = open('travels.txt', 'r', encoding='utf-8-sig')
gruz_1 = 0
massa_1 = 0
gruz_2 = 0
massa_2 = 0
gruz_3 = 0
massa_3 = 0
gruz = 0
lipki = 0
S = 0
punkti_1 = 1
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

    if L[2] == "Липки":
        lipki += int(L[6])

    if int(L[0]) == 1:
        S += int(L[4])

    for i in L:
        A = set(L[2])
print(A)

if (gruz_1 > gruz_2) and (gruz_1 > gruz_3):
    print('В этот день было больше всего груза ', gruz, 'Вот его суммарный объем ', massa_1)

if (gruz_2 > gruz_1) and (gruz_2 > gruz_3):
    print('В этот день было больше всего груза ', gruz, 'Вот его суммарный объем ', massa_2)

if (gruz_3 > gruz_1) and (gruz_3 > gruz_2):
    print('В этот день было больше всего груза ', gruz, 'Вот его суммарный объем ', massa_3)

print('Из поседка Липки было отправлено вот столько груза - ', lipki)
print('Суммарное расстояние за 1 октября - ', S)
print(punkti_1)