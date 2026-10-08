#Condicional if, permite ejecutar un bloque de código solo si se cumple una condición específica.

from os import system
system("clear")  #Limpia la pantalla de la consola

#Ejemplo 1, if basico.

edad = 18

if edad >= 18:  #Si la edad es mayor o igual a 18, se ejecuta el bloque de código
    print("Eres mayor de edad")  #Se imprime el mensaje si la condición es verdadera

#Ejemplo 2, if con else

numero = 10

if numero > 0:  #Si el número es mayor que 0, se ejecuta el bloque de código
    print("El número es positivo")  #Se imprime el mensaje si la condición es verdadera
else:  #Si la condición no se cumple, se ejecuta el bloque de código del else
    print("El número es negativo o cero")  #Se imprime el mensaje si la condición es falsa  


#ejemplo 3, if anidados

edad = 20
licencia = True

if edad >= 18:  #Si la edad es mayor o igual a 18, se ejecuta el bloque de código
    if licencia:  #Si la persona tiene licencia, se ejecuta el bloque de código
        print("Puedes conducir")  #Se imprime el mensaje si ambas condiciones son verdaderas
    else:  #Si la persona no tiene licencia, se ejecuta el bloque de código del else
        print("No puedes conducir, necesitas una licencia")  #Se imprime el mensaje si la primera condición es verdadera y la segunda es falsa
else:  #Si la edad es menor que 18, se ejecuta el bloque de código del else
    print("No puedes conducir, eres menor de edad")  #Se imprime el mensaje si la primera condición es falsa       


#ejemplo 4, if con elif

nota = int(input("Ingrese su nota: \n"))  #Se solicita al usuario que ingrese su nota y se convierte a entero

if nota >= 90:  #Si la nota es mayor o igual a 90, se ejecuta el bloque de código
    print("Excelente")  #Se imprime el mensaje si la condición es verdadera
elif nota >= 80:  #Si la nota es mayor o igual a 80,
    print("Muy bien")  #Se imprime el mensaje si la condición es verdadera
elif nota >= 70:  #Si la nota es mayor o igual a 70,
    print("Bien")  #Se imprime el mensaje si la condición es verdadera
else:  #Si ninguna de las condiciones anteriores se cumple, se ejecuta el bloque de código del else
    print("Necesitas mejorar")  #Se imprime el mensaje si todas las condiciones son falsas    