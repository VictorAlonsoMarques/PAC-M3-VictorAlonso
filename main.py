libroPalabras = {}

# Menú y opciones de gestión del libro
while True:
    print("\nGestión del Libro de las Accepciones")
    print("1. Añadir palabra y definición")
    print("2. Mostrar todas las palabras y definiciones")
    print("3. Modificar una definición existente")
    print("4. Eliminar una palabra o categoría")
    print("5. Salir")
    opcion = input("Elige una opción: ")

    # Añadir palabra y definición
    if opcion == '1':
        palabra = input("Palabra: ")
        categoria = input("Categoría: ")
        definicion = input("Definición: ")
        if palabra in libroPalabras:
            libroPalabras[palabra][categoria] = definicion
        else:
            libroPalabras[palabra] = {categoria: definicion}

    # Mostrar todas las palabras y definiciones
    elif opcion == '2':
        for palabra, categorias in libroPalabras.items():
            print(f"Palabra: {palabra}")
            for categoria, definicion in categorias.items():
                print(f"  {categoria}: {definicion}")

    # Modificar una definición existente
    elif opcion == '3':
        palabra = input("Palabra a modificar: ")
        categoria = input("Categoría de la definición: ")
        nueva_definicion = input("Nueva definición: ")
        if palabra in libroPalabras and categoria in libroPalabras[palabra]:
            libroPalabras[palabra][categoria] = nueva_definicion
            print(f"Definición actualizada para {palabra} en {categoria}.")
        else:
            print("Palabra o categoría no encontrada.")

    # Eliminar una palabra o categoría
    elif opcion == '4':
        palabra = input("Palabra a eliminar o modificar: ")
        respuesta = input("¿Eliminar una categoría específica? (s/n): ")
        if respuesta.lower() == 's':
            categoria = input("Categoría a eliminar: ")
            if palabra in libroPalabras and categoria in libroPalabras[palabra]:
                del libroPalabras[palabra][categoria]
                if not libroPalabras[palabra]:
                    del libroPalabras[palabra]
                print(f"Categoría {categoria} eliminada de {palabra}.")
            else:
                print("Categoría no encontrada.")
        else:
            if palabra in libroPalabras:
                del libroPalabras[palabra]
                print(f"Palabra {palabra} eliminada.")
            else:
                print("Palabra no encontrada.")

    # Salir del programa
    elif opcion == '5':
        print("Saliendo...")
        break
    else:
        print("Opción no válida. Inténtalo de nuevo.")
