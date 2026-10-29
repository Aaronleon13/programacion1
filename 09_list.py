# Las listas en Python son estructuras de datos 
# que permiten almacenar varios valores dentro de una
# variables. Son modificables podemos agregar, eliminar
# o cambiar elementos.
# Funciones utiles para listas.


#Crear una lista

nombres = ["Aaron", "Juan", "Maria"]
edades = [20, 30, 10, 8]
mix = ["Aaron", 30, "sabritas", 15]


print(nombres)
print(edades)
print(mix)

#Acceder a elementos de una lista
print(nombres[0])
print(edades[1])
print(mix[2])

#Agregar elementos una lista 
edades.append(25)
print(edades)

#Eliminar elementos de una lista
edades.remove(10)
print(edades)

#Eliminar con pop
edades.pop()
print(edades)

#Insertar elementos en una posicion especifica
edades.insert(1, 25)
print(edades)

#Cambiar elementos de una lista
edades[0] = 5
print(edades)

# Funciones utiles para listas.

#Tamaño de la lista
print(len(edades))
#Sumar elementos de una lista
print(sum(edades))
#Minimo de una lista
print(min(edades))
#Maximo de una lista
print(max(edades))
#Ordenar una lista
edades.sort()
print(edades)
#Ordenar una lista en orden descendente
edades.sort(reverse=True)
print(edades)
