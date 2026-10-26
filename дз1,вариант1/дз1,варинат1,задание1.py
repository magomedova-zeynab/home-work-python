def f(k, x):
    if x == 1: return k + 1
    return k - 1

n, m, x = [int(i) for i in input().split()]

matrica = []                        # создаём матрицу
for i in range(n):
    matrica += [[0]*m]
matrica[0][0] = 1

i = 0
j = 0
napr = 0      # 0 - вправо, 1 - вниз, 2 - влево, 3 - наверх (остатки при : на 4)

if x == 1:             
    matrica[0] = [int(i) for i in range(1, m+1)]  # заполняем 1-ую строку
else:
    matrica[0] = [int(i) for i in range(m*n, m*n - m, -1)]
    
for i in range(1, n):                           # заполняем m-ый столбец
    matrica[i][m-1] = f(matrica[i-1][m-1], x)
    
for j in range(m-2, -1, -1):                    # заполняем n-ую строку
    matrica[n-1][j] = f(matrica[n-1][j+1], x)

for i in range(n-2, 0, -1):                      # заполняем 1-ый столбец
    matrica[i][0] = f(matrica[i+1][0], x)


i, j = 1, 0
while True:
    if matrica[i][j] == m*n and x == 1 or matrica[i][j] == 1 and x != 1: break
    
    if napr == 0:
        stroka = matrica[i]
        while True:
            j += 1
            stroka[j] = f(stroka[j-1], x)
            if stroka[j+1] != 0:            #  проверяем, заполнена ли  
                break                       #       следующая ячейка
            
    if napr == 1:
        while True:
            i += 1
            matrica[i][j] = f(matrica[i-1][j], x)
            if matrica[i+1][j] != 0:
                break
            
    if napr == 2:
        stroka = matrica[i]
        while True:
            j -= 1
            stroka[j] = f(stroka[j+1], x)
            if stroka[j-1] != 0:
                break
            
    if napr == 3:
        while True:
            i -= 1
            matrica[i][j] = f(matrica[i+1][j], x)
            if matrica[i-1][j] != 0:
                break
    
    napr = (napr + 1) % 4         # меняем направление

for i in matrica: print(i)

        
