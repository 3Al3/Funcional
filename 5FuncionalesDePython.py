# Python incluye muchas funciones para la programacion Funcional

# La primera funcion que veremos es map()

# map(funcion,iterable) : Aplica la funcion a cada elemento

lista1 = [1,2,3,4,-1]
print(map(lambda x:x*2,lista1)) # Con el map solo retorna un Objeto
print(list(map(lambda x:x*2,lista1)))

# Obtener indices con enumerate()

for i,item in enumerate(lista1):  # Es util para trabajar con matriz
    print(f"el indice es:{i} y el valor es :{item}")  


# Vamos a ordenar una matriz con sorted()

# sorted(iterable,key=None, reverse=False)
# ejemplos

print(sorted([("a",2),("c",1),("d",4)])) # Una lista con varias tuplas que tienen 2 valores
# En el caso anterior ordeno por la primera variable de cada tupla
print(sorted([("a",2),("c",1),("d",4)],key=lambda x:x[1])) # Ahora ordenara por el segundo valor

if any(map(lambda x:x > 0,lista1)):
    print(f"Aunque sea 1 es mayor a 0")

# La funcion zip(): Une 2 listas y retorna un objeto

claves = ["python","hola","mundo"]
print(list(zip(claves,map(len,claves)))) # Asi creamos una lista clave valor que se puede convertir en un diccionario facilmente

# Esta es la manera mas eficiente de encontrar el primer elemento que cumpla una condicion
print(next(filter(lambda x: x>0,[-1,0,1,2]))) # Podriamos utilizar un list por si nunguno cumple que retorne una lista vacia
