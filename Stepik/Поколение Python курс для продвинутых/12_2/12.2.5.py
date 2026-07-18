from random import shuffle

def get_secret_friend(students):
    res = {}
    students = list(students)
    shuffle(students)
    res[students[-1]] = students[0]
    for i in range(1, len(students)):
        res[students[i-1]] = students[i]
    return res

students = ('Светлана', 'Аркадий', 'Борис')
for name, friend in get_secret_friend(students).items():
    print(name, '-', friend)