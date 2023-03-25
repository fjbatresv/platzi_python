firstName = 'Javier'
lastName = 'Batres'

# Concatenacion simple
fullName = firstName + ' ' + lastName
print(fullName)

# Uso de comillas dobles para evitar errors
quote = "I'm Javier"
print(quote)

quote2 = 'She said "Hello"'
print(quote2)

# format
template = "Hola mi nombre es {} y mi apellido es {}".format(firstName, lastName)
print(template)

# fFormat

template = f"Hola mi nombre es {firstName} y mi apellido es {lastName}"
print(template)

# Challenge
age = input('Cual es tu edad?')
template = f"Hola mi nombres es {firstName} {lastName} y tengo {age} años"

print(template)