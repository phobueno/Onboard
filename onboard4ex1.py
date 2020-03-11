import random
a = [random.randrange(1, 50, 1) for i in range(7)]
b = [random.randrange(1, 100, 1) for i in range(7)]
c = []

for x in a:
    for y in b:
        if(x == y):
            c.append(y)
print(c)
