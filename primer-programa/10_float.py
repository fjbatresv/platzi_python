x = 3.3
y = 1.1 + 2.2 # Genera mas decimales de precisión

print(x)
print(y)

print(x == y)

# Forma de comparacion "brusca"
y_str = format(y, '.2g')
print(y_str)
print(y_str == str(x))

print('*' * 10)

# Forma de comparacion matematica
print(y, x)

tolerance = 0.00001
print(abs(x - y) < tolerance)