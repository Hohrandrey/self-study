st = set()
for i in range(int(input())):
    st.add(input())

if input() in st:
    print('REPEAT')
else:
    print('OK')