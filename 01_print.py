#print("2" - 2) Python no puede restar un string y un número, por eso da error, porque python es de tipado FUERTE.

#Este es un print con comillas sencillas.
print('Hola mundo')

#Este des un print con numero entero.
print(5)

#Este es un print con doble comilla.
print("Hola mundo")

#Print con salto de linea.
print("1. Hola mundo\n2. Este es otro hola mundo")

#Este es un print con triple comilla.
print("""
Selecciona una opcion para continuar:
1. Opcion 1
2. Opcion 2
3. Opcion 3
""")
#esta es una opcion para imprimir con salto de linea
print("Selecciona una opcion para continuar:\n1. Opcion 1\n2. Opcion 2\n3. Opcion 3")

#esta es una opcion para imprimir con multiples print
print("Selecciona una opcion para continuar")
print("1. Opcion 1")
print("2. Opcion 2")
print("3. Opcion 3")

#sep es el separador entre los elementos.
print("apple", "banana", "cherry", sep=", ") 
#end es el final del print, por defecto es un salto de linea(\n), pero se puede cambiar a cualquier cosa.
print("Esto va junto", end=": ")
print("por culpa del end")

