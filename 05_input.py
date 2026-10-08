#La funcion input() permite al usuario ingresar datos desde el teclado. Cuando se llama a esta función, el programa se detiene y espera a que el usuario escriba algo y presione Enter. El valor ingresado se devuelve como una cadena de texto (string).

from os import system
system("clear")
  # Limpiar la pantalla de la terminal (opcional, depende del sistema operativo y del entorno de ejecución).
nombre = input("¿Cuál es tu nombre? \n")
print(f"Hola, {nombre}! Bienvenido al programa.")

edad = int(input("¿Cuál es tu edad? \n"))
# edad = int(edad) Convertir la cadena a un número entero
print(type(edad))  # Esto mostrará que la edad es un número entero (int).``

edad_futura = edad + 1

print(f"En un año, tendrás {edad_futura} años.")  # Esto concatenará la cadena de texto con el número 1, no sumará los valores numéricos.

altura = float(input("¿Cuál es tu altura en metros? Usar medida en metros \n"))
print(f"Tu altura es {altura} metros.")  # Esto mostrará la altura ingresada.

