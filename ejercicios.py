#print('Hola Mundo')    #ejercicio 1

# saludar = 'Hola Mundo'  #ejercicio 2
# print(saludar)

# nombre = input('escribe tu nombre: ')  #ejercicio 3
# print('!!hola ' + nombre + '¡¡')

# suma = int(3 + 2)                         #ejercicio 4
# multiplicacion = int(2 * 5)
# print(((suma) / (multiplicacion)) ** 2)

    # horas_trabajadas = int(input('Horas Trabajadas: '))                          #ejercicio 5
    # if horas_trabajadas == 1:
    #     print('Tu pago corresponde a $100.00 pesos por una hora laborada')
    # elif horas_trabajadas == 2:
    #     print('Tu pago corresponde a $200.00 pesos por dos hora laborada')
    # else:
    #     print('Introduce el numero de horas trabajadas correctamente')

# horas = float(input('Horas trabajadas: '))        #ejercicio 5
# coste = float(input('paga por hora: '))
# pago = horas * coste
# print('tu pago es: ' + str(pago))

# n = int(input("Introduce un número entero: "))       #ejercicio 6
# suma = n * (n + 1) / 2
# print("La suma de los primeros números enteros desde 1 hasta " + str(n) + " es " + str(suma))

kg = float(input('Tu peso en kg es: '))
mts = float(input('Tu altura en mts es: '))
imc = round((kg) / (mts) **2,2)
print('Tu indice de masa corporal es: imc ' + str((imc)))