for k in range(1, 10):
    for o in range(0, 10):
        for t in range(1, 10):
            if (k * 200 + o * 20 + t * 2) == t * 100 + o * 10 + k * 1:
                print(k, o, t, '+', k, o, t, '=', t, o, k)
else:
    print(' КОТ + КОТ = ТОК: no solution')
