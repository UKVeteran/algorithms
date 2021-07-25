from math import factorial

sum(1 for x in range(2,10) if not (factorial(x-1)+1)%x)