numbers = [float(x) for x in input("Въведете числа, разделени с интервали: ").split()]
absolute_values = [(lambda x: x if x >= 0 else -x)(x) for x in numbers]
print("Абсолютни стойности:", absolute_values)
