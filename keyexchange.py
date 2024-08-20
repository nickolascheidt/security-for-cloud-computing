import random

p = 1041607122029938459843911326429539139964006065005940226363139
g = 10

A = 105008283869277434967871522668292359874644989537271965222162

b = random.randint(10**39, p-1)
B = pow(g,b,p)

print("values are\nb:", b, "\nB:", B)

v = pow(A,b,p)

print("key used to send messages to Alice: ", v)