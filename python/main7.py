def celsius_a_fahrenheit(celsius):
    return(celsius * 9/5)+32

def fahrenheit_a_celsius(fahrenheit):
    return(fahrenheit - 32)* 5/9


def main():
    print("gracias por hacistir")


print("Convertidor de celsius a fahrenheit y viseversa")
print("opcion 1 conventir de celsius a fahrenheit")
print("opcion 2 conventir de fahrenheit a celsius")


opcion = int(input("Seleccione una opcion (1 or 2): "))

if opcion == 1:
    celsius = float(input("Introduce la temperatura el celsius:  "))
    fahrenhait = celsius_a_fahrenheit(celsius) 
    print("°F", celsius,"°C son",fahrenhait,"°F")# type: ignore

elif opcion == 2:
    fahrenhait = float(input("Introduce la temperatura en fahrenhait: "))
    celsius = fahrenheit_a_celsius(fahrenhait)
    print("°F", fahrenhait,"°F son",celsius,"°C") # type: ignore

else:
    print("is't not valid")


if __name__ == "__main__":
    main()