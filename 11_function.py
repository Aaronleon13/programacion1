# Las funciones nos permiten organizar y reutilizar codigo
#argumentos posicionales
#argumentos con nombre


def saludar(nombre, saludo = "Hola"):
    mensaje = f"{saludo} {nombre}"
    return mensaje

print(saludar("Aarón", "Bienvenido"))
print(saludar("Bienvenido", "Manuel"))
print(saludar(saludo="Saludos", nombre="Carlos Ismael"))


def sumar(a, b, c = 5):
    suma = a + b + c
    return suma


print(sumar(5,10))
print(sumar(10,30,20))


# Promedio de un estudiante

def promedio(cal1, cal2, cal3):
    promedio = (cal1 + cal2 + cal3) / 3
    return promedio

def verificar_aprobacion(promedio, minima = 75):
    if promedio >= minima:
        return "Aprobado"
    else:
        return "Reprobado"

def mostrar_mensaje (nombre, promedio, estado ):
    print(f"Alumno: {nombre}")
    print(f"Promedio: {promedio}")
    print(f"Estado: {estado}")


nom = input("Dame el nombre del alumno: ")
calif1 = float(input("Dame la calificación 1: "))
calif2 = float(input("Dame la calificación 2: "))
calif3 = float(input("Dame la calificación 3: "))

prom = promedio(calif1, calif2, calif3)
status = verificar_aprobacion(prom)
mostrar_mensaje(nom, prom, status)
