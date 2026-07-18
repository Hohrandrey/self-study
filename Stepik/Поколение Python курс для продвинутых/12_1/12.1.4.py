from random import randrange


def generate_lottery_ticket():
    st = set()
    while len(st) < 7:
        st.add(str(randrange(1, 50)))
    return ' '.join(sorted(list(st), key=int))

print(generate_lottery_ticket())
print(generate_lottery_ticket())
print(generate_lottery_ticket())
