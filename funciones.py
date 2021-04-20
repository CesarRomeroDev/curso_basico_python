# def imprimir_mensaje():
#    print('mensaje especial')
#    print('¡estoy aprendiendo a usar funcione!')  


#imprimir_mensaje()
#imprimir_mensaje()
#imprimir_mensaje()

def imprimir_mensaje(mensaje):
    print('hola')
    print('como estas?')
    print(mensaje)
    print('adios')


opcion = int(input('Elige una opcion (1, 2, 3): '))
if opcion == 1:
    imprimir_mensaje('elegiste la opcion 1')
elif opcion == 2:
    imprimir_mensaje('elegiste la opcion 2')
elif opcion == 3:
    imprimir_mensaje('elegiste la opcion 3')
else:
    print('Selecciona la opcion incorrecta')