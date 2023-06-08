from bruh import Tube
from random import randrange, choice
import logging

# get input and create tubes
letters = ['a', 'b', 'c', 'd']
let_count = [0, 0, 0, 0]
while True:
    diff = input('1: Easy\n2: Medium\n3: Hard\n')
    if diff == '1':
        num = 5
        break
    elif diff == '2':
        num = 6
        letters.append('e')
        let_count.append(0)
        break
    elif diff == '3':
        num = 7
        letters.append('e')
        letters.append('f')
        let_count.append(0)
        let_count.append(0)
        break
total = num * num - num
tubes = Tube(num, num)

letter = []
for x in letters:
    for y in range(num):
        letter.append(x)
# fill tubes
for times in range(total):
    value = choice(letter)
    letter.remove(value)
    while True:
        try:
            key = randrange(num)
            tubes.add(value, key)
            break
        except Exception:
            pass
    # output
    print(tubes, '\n')

