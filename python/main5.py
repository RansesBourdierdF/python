def main():
    notas = []  # Lista vacía para almacenar las notas
    
    print("Calculadora de Promedio de Notas - Ingrese las notas (escribe 'salir' para terminar)")
    
    while True:
        entrada = input("Introduce una nota (o escribe 'salir' para terminar): ")
        
        if entrada.lower() == 'salir':
            break  # Termina el bucle si el usuario escribe 'salir'
        
        try:
            nota = float(entrada)  # Convierte la entrada a un número decimal
            notas.append(nota)     # Agrega la nota a la lista
        except ValueError:
            print("Por favor, introduce un número válido.")  # Si la entrada no es válida, muestra un mensaje de error
    
    # Calcular el promedio si hay notas en la lista
    if len(notas) > 0:
        promedio = sum(notas) / len(notas)
        print(f"\nEl promedio de tus notas es {promedio:.2f}")
    else:
        print("\nNo se ingresaron notas.")

if __name__ == "__main__":
    main()
