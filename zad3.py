b = []
numbers = [float(x) for x in input("Въведете числа, разделени с интервали: ").split()]
absolute_values = [(lambda x: x if x >= 0 else -x)]
for i in absolute_values:
    b.append(i)
    
print(b)
