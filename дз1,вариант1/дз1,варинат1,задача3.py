sp = input()
if sp == '[]': sp1 = []
else:
    sp1 = []
    count = 1
    sp = [int(i) for i in sp[1:-1].split(', ')]
    el = sp[0]
    for n in sp[1:]:
        if n == el:
            count += 1
        else:
            sp1.append((el, count))
            el = n
            count = 1
    sp1.append((el, count))
print(sp1)

sp2 = []
if sp1 != []: 
    for x in sp1:
        sp2 += [x[0]] * x[1]
print(sp2)
