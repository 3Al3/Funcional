from functools import partial # Esta funcion es mas flexible que lambda
# en vez de cambiar el comportamiento de una funcion cambia el argumento
from first import first 

def masGrandeque(numero,min=0):
    return numero > min

print(first([-1,0,1,2],key=partial(masGrandeque,min=1))) # En este casi imprime el primer numero mayor a 0

# se debe considerar partial() como una alternativa superiro a lambda