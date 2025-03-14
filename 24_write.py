
with open('./text.txt', 'r+') as file:
    # Leer todas las líneas y mostrarlas
    for line in file:
        print(line.strip())  # strip() elimina saltos de línea innecesarios

    # Escribir una nueva línea al final
    file.write('\nNuevas cosas en este archivo')
    file.write('\nNuevas cosas en este archivo')
