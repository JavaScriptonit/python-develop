import random

a = random.randint(1,3)

x = int(input())

if a == x:
    print('Right number')
else:
    print(f'Fail. Not right number! The number is {a}')