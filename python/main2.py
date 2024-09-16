



def calcular_IMC(peso , altura):
    return peso /(altura ** 2)


print("Calculadora de indice de masa corporal (IMC)")
peso = float(input("introduce tu peso en kilogramos: "))
altura = float(input("Introduce tu altura en metros: "))

IMC = calcular_IMC(peso, altura)

print("f Tu IMC es",IMC)

def main():
    print("Gracias por asistir")

if __name__ == "__main__":
    main()