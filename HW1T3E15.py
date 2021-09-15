from random import *

print('Size: ', end=' ')
numbers = [randrange(0, 100) for _ in range(int(input()))]
print('Input arr: ', numbers)
numbers_mod = [numbers[i] for i in range(len(numbers)) if i == 0 or i % 3 != 0]
print('Output arr: ', numbers_mod)