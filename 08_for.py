# For es una función de control que permite 
# ejecutar un bloque de código un número determinado de veces. 
# La sintaxis básica es:


for i in range(0, 10): # range(inicio, limite, aumento)
    print(i)

for t in "Hola mundo":
    print(t)

print("----------------------------")
#for anidados
for i in range(3):
    for j in range(2):
        print(i, j)

# El if in comprueba si el valor existe

nombre = 'aaron'

if 'a' in nombre:
    print("La letra 'a' esta en el nombre")