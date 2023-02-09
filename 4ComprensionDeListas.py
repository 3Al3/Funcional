# ComprensiónDeListas

# Este ejemplo creara una lista sin la comprensió

if __name__ == "__main__":
    x = [] # Declaramos nuestra listas vacia
    for i in (1,2,3):
        x.append(i) # Agregamos cada i a la lista
    
    print(x)

    # Ahora vamos a crear lo mismo utilizando la comprensió de listas

    a = [x for x in (1,2,3)]
    print(f"Utilizando comprensió de listas: {a}")

    # ventajas el codigo es mas corto lo que hace que se compile mas rapido
    # simplemente crea la lista con los elemetnso y los mueve a la nueva lista en 1 sola operación
    # Esto permite mas declaraciones for e if

    # Tambien puede crear diccionarios y tuplas de la misma forma
    # Ejemplo
    dictPrueba = ({x:x.upper() for x in ['comuni','hola']})
    print(dictPrueba)