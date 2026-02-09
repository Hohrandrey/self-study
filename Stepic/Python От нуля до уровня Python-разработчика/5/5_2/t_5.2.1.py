from dataclasses import dataclass


@dataclass
class User:
    name: str
    age: int


name1 = input()
age1 =  int(input())
name2 = input()
age2 =  int(input())


u1 = User(name1, age1)
u2 = User(name2, age2)

print(u1 == u2)
