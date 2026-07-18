translation_dict = {'G':'C', 'C':'G', 'T':'A', 'A':'U'}
st = ''
for elem in input():
    st += translation_dict[elem]
print(st)
