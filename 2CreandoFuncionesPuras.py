# Cuando codifica con un estilo funcional , sus funciones no tendran efectos secundario
# Mejor veamos un ejemplos

                      # Esto es una funcion nopura

def eliminarUltimoElemento(lista):
    lista.pop(-1)     # Esto modifica la lista que le pasamos

                      # Esto es una funcion pura

def elUltimo(lista):
    return lista[:-1] # Aqui retornamos una copia de la lista sin el ultimo elemento.
                      # No modifico la lista

if __name__ == "__main__":
    miLista = [1,2,3,4,5]
    laCopia = elUltimo(miLista)
    print(miLista)
    print(laCopia)
    
