# Variables Locales y Globales


nombre = 'Aaron' # Variable Global

def saludar():
    global nombre
    nombre = 'Manuelito' # Variable local
    print(nombre)

saludar()
print(nombre)

