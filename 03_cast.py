# Transformar tipos de un valor a otro

print("Manuel" + str(19))

print("5" + str(5)) #Esto imprime 55, porque el 5 es un string y no un numero, por eso se concatena.
print(int("5") + 5) #Esto imprime 10, porque el 5 es un string y se transforma a un numero entero, por eso se suma.

print(type(2.5))

print(int(2.5)) #Esto imprime 2, porque el 2.5 es un float y se transforma a un numero entero, por eso se redondea hacia abajo.

print(float(5)) #Esto imprime 5.0, porque el 5 es un entero y se transforma a un numero flotante.

print(round(2.51)) #Esto imprime 2, porque el 2.5 es un float y se redondea hacia abajo.

#imprimir booleanos
print(bool(1)) #Esto imprime True, porque el 1 es un entero y se
print(bool(0)) #Esto imprime False, porque el 0 es un entero y se transforma a un booleano.
print(bool(-1)) #Esto imprime True, porque el -1 es un entero y se transforma a un booleano.

print(bool("Hola mundo")) #Esto imprime True, porque el "Hola mundo" es un string y se transforma a un booleano.
print(bool("")) #Esto imprime False, porque el "" es un string vacio y se transforma a un booleano.
print(bool(" ")) #Esto imprime True, porque el " " es un string con un espacio y se transforma a un booleano.