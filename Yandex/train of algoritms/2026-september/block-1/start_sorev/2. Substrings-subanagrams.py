"""
from itertools import *

s = input()
t = input()
su = 0

perm = []
for i in range(1, len(t)+1):
    perm.extend([''.join(p) for p in permutations(t, i)])
perm = set(perm)
print(perm)

for otr in perm:
    for x in range(len(t)+1):
        #print(otr, s[x:x+len(otr)])
        if s[x:x+len(otr)] == otr:
            su += 1

print(su)
"""
s = input()
t = input()

t_count = {}
for ch in t:
    t_count[ch] = t_count.get(ch, 0) + 1

print(t_count)

n = len(s)
total = 0
left = 0
current_count = {}

for right in range(n):
    char = s[right]
    current_count[char] = current_count.get(char, 0) + 1

    while current_count[char] > t_count.get(char, 0):
        current_count[s[left]] -= 1
        left += 1

    total += (right - left + 1)

print(total)