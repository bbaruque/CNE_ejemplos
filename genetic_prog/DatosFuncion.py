# Datos del problema

# Por simplificación, aquí se incluyen ya los vectores que contienen los datos del problema
# En muchos casos, es probable que tengamos que extraerlos de alguna fuente externa (ficheros, APIs)

# -----

# Problem data

# For simplicity, the vectors containing the problem data are already included here.
# In many cases, we may need to extract them from some external source (files, APIs).


'''Se trata de obtener la correspondencia entre el dato de la x y la y obtenida en la funcion f(y) = x^4 + x^3 + x^2 + x, al suministrar diferentes valores a la x'''

'''The problem is the obtaining the correspondence between the data of x and y obtained in the function f(y) = x^4 + x^3 + x^2 + x, by supplying different values to the x. 
function f(y) = x^4 + x^3 + x^2 + x, by giving different values to the x'''


def fCuarta():
    entradas = [x/10. for x in range(-10,10)]
    salidas = [x**4 - x**3 - x**2 - x for x in entradas]
    
    return entradas,salidas


def prueba():
    entradas, salidas = fCuarta()
    
    for x,y in zip(entradas,salidas):
        print("x=",x,"y=",y)

if __name__ == "__main__":
    prueba()
