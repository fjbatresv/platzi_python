if True:
    print('deberia ejecutarse')

if False:
    print('No se debe ejecutar')

pet = input('¿Cuál es tu mascota favorita?')

if pet == 'perro':
    print('Que lindo')
elif pet == 'gato':
    print('Duerme mucho')
else:
    print('Suerte con tu mascota')

stock = int(input('Digita el stock=> '))

if stock >= 100 and stock <= 1000:
    print('Stock correcto')
else:
    print('Stock invalido')