# contador = 0
# print('2 elevado a ' + str(contador) + ' es igual a: ' + str(2** contador))
# contador = 1
# print('2 elevado a ' + str(contador) + ' es igual a: ' + str(2** contador))
# contador = 3
# print('2 elevado a ' + str(contador) + ' es igual a: ' + str(2** contador))
# contador = 4
# print('2 elevado a ' + str(contador) + ' es igual a: ' + str(2** contador))
# contador = 5
# print('2 elevado a ' + str(contador) + ' es igual a: ' + str(2** contador))
# contador = 6
# print('2 elevado a ' + str(contador) + ' es igual a: ' + str(2** contador))

def run():
    LIMITE = 1000000         # constante ya que nunca va a cambiar su valor y se escribe eb mayusculas.

    contador = 0
    potencia_2 = 2**contador
    while potencia_2 < LIMITE:
        print('2 elevado a ' + str(contador) + ' es igual a: ' + str(potencia_2))
        contador = contador + 1
        potencia_2 = 2**contador


if __name__ == '__main__':
    run()


# def run():
#     i= 0
#     while i < 10: 
#         i = i + 1
#         print(i)


# if __name__ == '__main__':
#     run()