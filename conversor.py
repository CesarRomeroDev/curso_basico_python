pesos = input("¿Cuantos pesos mexicanos tienes?: ")
pesos = float(pesos)
valor_dolar = 20.09
dolares = pesos / valor_dolar
dolares = round(dolares, 2)
dolares = str(dolares)
print("Tienes $" + dolares + " dolares")