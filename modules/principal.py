# from conversiones import metros_a_centimetros, horas_a_minutos
import conversiones

def main():
    metros = int(input("Ingrese la cantidad de metros: "))
    resultado = conversiones.metros_a_centimetros(metros)
    print(f"{metros} metros son {resultado} centimetros")

    horas = int(input("Ingrese la cantidad de horas: "))
    resultado = conversiones.horas_a_minutos(horas)
    print(f"{horas} horas son {resultado} minutos")

if __name__ == "__main__":
    main()