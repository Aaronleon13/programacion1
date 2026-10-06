name = "Aaron"
edad = 35
estatura = 1.80

print(name)
print(type(name))
print(edad)
print(type(edad))
print(estatura)
print(type(estatura))


# Cuidado con cambiar los valores de las variables, porque si se cambia el tipo de dato de una variable, puede causar errores en el programa.
# name = 5
# print(name)

print("Hola " + name + ", tienes " + str(edad) + " años y mides " + str(estatura) + " metros.")


#Esto es una forma mas facil de imprimir variables en un string, usando f-strings.
print(f"Hola {name}, tienes {edad} años y mides {estatura} metros.") 
print(f"""
Hola {name},
tienes {edad} años 
y mides {estatura} metros.
""")

#No es recomendado hacer esto.
nombre, edad, estatura = "Aaron", 35, 1.80

print(f"Hola {nombre}, tienes {edad} años y mides {estatura} metros.")

#Buenas practicas para declarara variables en python

miNombrees = "Aaron" #Camel case, NO
minombreaqui = "Aaron" #Lower case, NO
mi_nombre_es = "Aaron" #Snake case, SI
tiene_comida = True #Snake case, SI
nombre = "Aaron" #Lower case, SI
Mi_NombreEs = "Aaron" #Camel case, NO