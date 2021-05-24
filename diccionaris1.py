diccionarios = {
    'nombre': 'Carlos',
    'edad': 22,
    'Cursos': ['Python', 'Django', 'JavaScript'],
}

# print(diccionarios['nombre'])
# print(diccionarios['edad'])
# print(diccionarios['Cursos'])

# print(diccionarios['Cursos'][0])
# print(diccionarios['Cursos'][1])
# print(diccionarios['Cursos'][2])

for key in diccionarios:
    print(key, ':', diccionarios[key] )