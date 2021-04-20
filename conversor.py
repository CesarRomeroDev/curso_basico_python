def conversor(pais, valor_dolar):
    pesos = input('¿cunatos pesos ' + pais + 'tienes: ')
    pesos = float(pesos)
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tienes $" + dolares + " dolares")

menu = """
Bienvenido al conversor de monedas 💰💹💵💲

1 - Pesos Colombianos
2 - Pesos Argrntinos
3 - Pesos Mexicanos

introduce un numero: """

opcion = int(input(menu))

if opcion == 1:
    conversor('colombianos ', 3875)
elif opcion == 2:
    conversor('argentinos ', 65 )
elif opcion == 3:
    conversor('mexicanos ', 19.93 )
else:
    print('ingresa una opción correcta por favor. ')

