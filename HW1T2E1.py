from random import randrange

num_ticket = randrange(100000, 1000000)
print('Ticket number: ', num_ticket)
if num_ticket % 7 == 0:
    print('Lucky')
    print(f'2 lucky tickets cannot be in a row cause {num_ticket + 1} // 7 = {(num_ticket + 1) / 7} and {num_ticket - 1} // 7 = {(num_ticket - 1) / 7}')

else:
    print('Nope')