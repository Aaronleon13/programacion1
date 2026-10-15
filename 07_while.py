#Ciclo While es una estructura de control que permite ejecutar
#un bloque de código mientras se cumpla una condición. La sintaxis básica es:


contador = 0  # Inicializamos un contador

while contador < 5:  # Mientras el contador sea menor que 5
    print("El contador es:", contador)  # Imprimimos el valor del contador
    contador += 1  # Incrementamos el contador en 1
    #contador = contador + 1 Otra forma de incrementar el contador



respuesta = ""  # Inicializamos la variable respuesta

while respuesta != "salir":  # Mientras la respuesta no sea "salir"
    respuesta = input("Para parar con el programa, escribe salir: ")  # Solicitamos nuevamente la respuesta

    if respuesta == "salir":  # Si la respuesta es "salir"
        print("Has decidido salir del programa.")  # Informamos que el usuario ha decidido salir
    else:  # Si la respuesta no es "salir"  
        print("Has decidido continuar.")  # Informamos que el usuario ha decidido continuar
