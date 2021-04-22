menu = """
  Vienvenido al Jego
         de 
PIEDRA , PAPEL O TIGERA.

Selecciona una Opcion y Juega contra la maquina.

Piedra ✊

Papel ✋
     O
Tijera ✌ """
print(menu)
opcion_1 = 'piedra', 'papel', 'tijera'
opcion_2 = 'piedra', 'papel', 'tijera'

opcion_1 = input('escribe una primera opción: ')
opcion_2 = input('escribe una segunda opción: ')

if opcion_1 == 'piedra' and opcion_2 == 'piedra':
    print('EMPATE')
elif opcion_1 == 'papel' and opcion_2 == 'papel':
    print('EMPATE')
elif opcion_1 == 'tijera' and opcion_2 == 'tijera':
    print('EMPATE')
elif opcion_1 == 'piedra' and opcion_2 == 'papel' or opcion_1 == 'papel' and opcion_2 == 'piedra':
    print('!!!Ganador PAPEL¡¡¡')
elif opcion_1 == 'piedra' and opcion_2 == 'tijera' or opcion_1 == 'tijera' and opcion_2 == 'piedra':
    print('!!!Ganador PIEDRA¡¡¡')
elif opcion_1 == 'papel' and opcion_2 == 'tijera' or opcion_1 == 'tijera' and opcion_2 == 'papel':
    print('!!!Ganador TIJERA¡¡¡')
else:
    print('¡¡Escribe una opción correcta!!')