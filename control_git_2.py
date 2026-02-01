max_1 = 0
max_2 = 0
max_3 = 0
max_4 = 0
with  open('111.txt', 'r') as f:
    for i in f:
        L = i.split()
        print(L)
        if int(L[2]) == 8:
            max_1 = max(max_1, int(L[3]) + int(L[4]))
        if int(L[2]) == 9:
            max_2 = max(max_2, int(L[3]) + int(L[4]))
        if int(L[2]) == 10:
            max_3 = max(max_3, int(L[3]) + int(L[4]))
        if int(L[2]) == 11:
            max_4 = max(max_4, int(L[3]) + int(L[4]))

print('у восьмых классов - ', max_1)
print('у девятых классов - ', max_2)
print('у десятых классов - ', max_3)
if  max_4 == max(max_4, int(L[3]) + int(L[4])):
            print(L[0], L[1])
print('у одиннадцатых классов - ', max_4)
print(max(L[3]))