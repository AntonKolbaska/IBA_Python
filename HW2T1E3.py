from random import randrange

numbers = [randrange(-9, 10) for _ in range(int(input('Size: ')))]
print('Input arr:', numbers)

print('Negative summ:', sum([i for i in numbers if i < 0]))

if numbers.count(0) > 1:
    item = [j for j in range(len(numbers)) if numbers[j] == 0]
    print('Summ zero-2-zero:', sum(numbers[item[0]:item[1]]))
else:
    print('No 2 zeroes:', 0)