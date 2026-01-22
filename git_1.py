f = open('perepis.txt', 'r' )
k = 0
a = int(input('укажите от какого года рождения будем считать '))
b = int(input('укажите до какого года рождения будем считать '))
for i in f:
    L = i.split()
    print(L[0])
    s = int(L[3].split('.')[2])
    if s < 1978:
        k+=1
    if s > a and s < b:
        print(L[0], L[3])
print('меньше 1978 года вот столько человек - ', k)