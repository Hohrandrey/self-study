st1 = input()
st2 = input()

def is_anagram(s1: str, s2: str) -> bool:
    return sorted(list(s1)) == sorted(list(s2))

print(is_anagram(st1, st2))