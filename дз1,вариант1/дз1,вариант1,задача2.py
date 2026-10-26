m = 0
st = input()
answer = ''
while st != 'STOP':
    l = len(set(st.lower()))
    if l>m: answer = st
    st = input()
print(answer, l)
