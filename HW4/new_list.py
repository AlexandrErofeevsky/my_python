#1 for
from math import sqrt
x = [2,9,16,25]
y = []
for i in range(len(x)):
    y.append(sqrt(x[i]))
print(y)    

#2 map
print(list(map(sqrt,x)))

#3 generator
c=[sqrt(x[i]) for i in range(len(x))]
print(c)
