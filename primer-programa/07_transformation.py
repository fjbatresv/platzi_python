name = 'Javier'
print(type(name))
# Cambio dinamico a int
name = 12
print(type(name))
# Cambio dinamico a boolean
name = True
print(type(name))

# int a str
age = 28
print('Tipo de age: ', type(age))

# Transformacion explicita
print("Mi edad es " + str(age))

# Transformacion implicita
print(f"Mi edad es {age}")


def getAge():
    age = input("Escribe tu edad => ")
    print(type(age))
    try:
        age = int(age)
        return age
    except:
        print('Esa no es una edad valida')
        return getAge()


age = getAge()

print(f"Tu edad en 10 años será {10 + int(age)}")
