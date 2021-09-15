def square (a, b):
    if a < b:
        size_square.append(a)
        return square(a, b - a)
    elif b == a:
        size_square.append(a)
        return a
    elif a < b:
        size_square.append(b)
        return square(a - b, b)
a = int(input('a: '))
b = int(input('b: '))
size_square = []
square (a, b)
print ('Edge length: ' + ''.join(str(size_square)))
print ('Quadrate number: ' + str(len(size_square)))