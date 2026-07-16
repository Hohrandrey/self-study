my_dict = {
    'math_grades': [10, 7, 36, 14, 25], 'physics_grades': [14, 28, 7, 10, 36, 5],
    'chemistry_grades': [10, 14, 19, 20, 21], 'geography_grades': [10, 15, 19, 34],
}

n_d = {}
for key, value in my_dict.items():
    n_d[key] = [element for element in value if element<=20]

print(n_d)