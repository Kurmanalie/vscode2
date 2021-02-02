import random
def rand_numlist(a):
    k = []
    i = 0
    while i < a:
        k.append(random.randint(1,1000))
        i+=1
    print(k)

a = int(input())
rand_numlist(a)