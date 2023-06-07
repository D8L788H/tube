from bruh import Tube
from random import randrange
from random import choice

# get input and create tubes
values = ['a', 'b', 'c', 'd']
while True:
    diff = input('1: Easy\n2: Medium\n3: Hard\n')
    if diff == '1':
        num = 5
        total = 20
        break
    elif diff == '2':
        num = 6
        total = 30
        values.append('e')
        break
    elif diff == '3':
        num = 7
        total = 42
        values.append('e')
        values.append('f')
        break
tubes = Tube(num, num)

# fill tubes

length = [0]*num
letter = []
for times in range(total):
    # get a random letter from the values list, if the number of same
    # letters exceeds the column number, that letters gets removed
    # from the values list.
    x = choice(values)
    letter.append(x)
    if letter.count(x) == num:
        values.remove(x)

    # get a random value for the position and add 1 to that position, if the
    # value of that position exceeds the num (length of the column), it gets
    # a new random value
    y = randrange(num)
    length[y] += 1
    if length[y] >= num:
        while True:
            new_y = randrange(num)
            if new_y != y:
                y = new_y
                break
        length[y] += 1
        
    # add the random values to the tubes using add method
    tubes.add(x, y, 1)
    # haaya ene deed taliin method add hiih ystoigoosoo 1 ymuu 2oor baga useg add hiigeed baih ym
    # yagaad gedgiig n uneheer oilgodgue

print()
print(tubes)
