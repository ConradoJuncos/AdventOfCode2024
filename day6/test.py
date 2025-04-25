import random
import time

r = random.random()

cont = 0
t1 = time.time()
while True:
    cont += 1
    ra = random.random()
    if ra == r:
        print(cont)
        break
    if cont % 100000000 == 0:
        t2 = time.time()
        print(t2 - t1)
        print(ra)
