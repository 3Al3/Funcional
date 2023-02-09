# Los generadores son objetos que se comportan como Iteradores
# Es como su fuera una pila
# Devuelve un valor en cada llamada con el metodo next()
# Creemos un generador

# Creamos una funcion y retornamos los datos con yield
# Cuando python ve la palabra clave yield nombrara a la funcion como generador

# Listo vamos
def generador():
    yield 1
    yield 2
    yield 3
    yield "Hola"

if __name__=="__main__":
    print(generador()) # Nos dice que es un OBJETO
    gen = generador()  # Guardamos el objeto en una variable
    print(next(gen))
    print(next(gen))
    print(next(gen))
    print(next(gen))
    print(next(gen))   # Cuando llega al final nos retorna un StopIteration

    # Los generadores mantiene una referencia a la pila , por eso cuando llama a next() puede dar el sigueinte valor

    # Supongo que se estara preguntando para que usarlos 
    # El problema que solucionan es el siguiente:
    # Cuando estas iterando sobre alguna estructura de datos SIN los generadores lo que hace es cargar todos los datos
    # y esto consume mucha memoria

    # Pequeño problema para representar la importancia de los generadores
    # Suponga que quiere encontrar el numero que esta en el medio de 10,000,000
    # Pero ahora tendra una restriccion y solo puede usar 128MB de ram

    # Ejecute lo siguiente en la terminal

    # ulimit -v 131072
    # python3
    # a = list(range(10000000)) 

    # Despues de esto tendra el error de que no tiene suficiente memoria

    # Ahora usemos un generador en su lugar

    # for value in range(10000000):
    #   if value == 50000:
    #        print("Lo encontramos")
    #       break
 
    # El programa funciona sin problemas
    # range() se comporta como un generador, por lo tanto la lista se va generado de forma dinimica

    



