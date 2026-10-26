import numpy as np

def slide_average(l: list, k: int):
    n = len(l)
    if k <= 0 or k > n: return 'ERROR'
    answer = []                         
    s = sum(l[:k])                      # O(k)
    answer.append(s//k)             
    for i in range(k, n):               # O(n - k)
        s = s - l[i - k] + l[i]         
        answer.append(s//k)          
    return answer                       # сложность всей функции -- O(n)


def np_slide_average(l: list, k: int) -> list:
    l = np.array(l, dtype=float)                #O(n)
    answer = []
    n = len(l)

    if k <= 0 or k > n: return 'ERROR'

    for i in range(n - k + 1):             #O(n-k+1)
        window = l[i:i+k]                     
        answer.append(window.mean())       #O(k)
    ###ОБЩАЯ СЛОЖНОСТЬ ЦИКЛА--O((n-k+1) * (k+1)) ~ O(n*k - k**2 + n + 1) ~ O(n**2), т.к. k <= n

    return answer                          #В итоге: O(n) + O(n**2) ~ O(n**2)

print(slide_average([2, 4, 6, 8, 10], 3))