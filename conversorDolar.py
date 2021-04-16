dolar = input("¿Cuantos dolares estadounidenses tienes?: ")
dolar = float(dolar)
valor_pesos_mexico =  0.050
pesos = dolar / valor_pesos_mexico
pesos = round(pesos, 3)
pesos = str(pesos)
print("Tienes $" + pesos + " pesos")