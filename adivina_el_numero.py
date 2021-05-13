import random

def run():
    numero_aleatorio = random.randint(1, 100)
    numero_a_elegir = int(input('Elige un numero del 1 al 100: '))
    while numero_aleatorio != numero_a_elegir:
        if numero_a_elegir < numero_aleatorio:
            print('Busca un numero mas grande')
        else:
            print('Busca un numero mas pequeño')
        numero_a_elegir = int(input('Elige otro numero: '))
    print('¡¡Ganaste!!')



if __name__ == '__main__':
    run()