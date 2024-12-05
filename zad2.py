from math import sqrt
squared = []
numbers = (input().split())
for i in numbers:
    i = float(i)
    squared.append(sqrt(i))
print(squared)