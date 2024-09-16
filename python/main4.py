def main():
    lista_compras = []  # Lista vacía para almacenar los ítems

    print("Lista de Compras - Agrega ítems (escribe 'salir' para terminar)")

    while True:
        item = input("Agrega un ítem a la lista (o escribe 'salir' para terminar): ")
        
        if item.lower() == 'salir':
            break  # Termina el bucle si el usuario escribe 'salir'
        else:
            lista_compras.append(item)  # Agrega el ítem a la lista

    # Mostrar la lista completa de ítems
    print("\nHas agregado los siguientes ítems a tu lista de compras:")
    for i, item in enumerate(lista_compras, 1):
        print(f"{i}. {item}")

if __name__ == "__main__":
    main()
