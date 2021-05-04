def palindromo(palabra):
    palabra = palabra.lower()           #pasar la palabra a minusculas
    palabra = palabra.replace(' ', '')  #reemplazar los espacios por la nada
    palabra_inversa = palabra[ : :-1]   #palabra de inicio a fin pero imprime la palabra inversa -1
    if  palabra == palabra_inversa:
        return True
    else:
        return False
                                        #Siempre hay que dejar dos espacios entre las funciones e entripoint(buenasPr)

palabra = input("""
        ¡¡Bienvenido a las Palabras POLINDROMOS!!
AquÍ podras poner palabras que se leen al DERECHO y al REVÉS
                   Así que ¡¡INICIEMOS!!
Escribe una Palabra: """)


def run():                              # Siempre hay que tener una funcion PRINCIPAL para correr nuestro codigo
    es_palindromo = palindromo(palabra)
    if es_palindromo == True:
        print('Es palindromo')
    else:
        print('No es palindromo')
                                        #Siempre hay que dejar dos espacios entre las funciones e entripoint(buenasPr)

if __name__ == '__main__':              # Entripoint PUNTO DE ESTRADA DE UN PROGRAMA de python(Buena Practica)
    run()                               # Invocación de la funcion run() la cual es nuestra función principal