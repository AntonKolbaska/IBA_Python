from random import *

cost_later = 0
p = randrange(1, 99)
cost = [(randrange(1, 1000)) for i in range(randrange(3, 10))]
print('Year purchase:', *['{0:2.2f}$'.format(j) for j in cost], sep='\n')
print(f'Depreciation: {p}%')
for i in cost:
    cost_later += i
    cost_later *= p / 100
print(f'Residual value :', '{0:2.2f}$'.format(cost_later))