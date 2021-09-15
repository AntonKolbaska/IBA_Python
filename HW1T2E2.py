from random import *

p = (randrange(1, 10))
print('Income DAY 1: ', '${0:5.3f}'.format(p))
q = randrange(10, 100)
print('Expected value: ', '${0:4.3f}'.format(q))
count = 1
while p < q:
    p += p * 0.03
    count += 1
print('Days need: ', count)