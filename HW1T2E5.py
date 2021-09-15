from random import *

num = [0]
total = 0
print('Length: ', end=' ')
for _ in range(int(input())):
    random_num = randrange(-99, 100)
    if random_num != 0:
        num.append(random_num)
num.reverse()
print(num)
for i in range(1, len(num)):
    if num[i] < 0 < num[i - 1] or num[i] > 0 > num[i - 1]:
        total += 1

print(f'Changes: {total}')