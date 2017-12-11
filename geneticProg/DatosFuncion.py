# Datos del problema
# Por simplificación, aquí se incluyen ya los vectores que contienen los datos del problema
# En muchos casos, es probable que tengamos que extraerlos de fuera

'''Se trata de obtener la correspondencia entre el dato de la x y la y obtenida en la 
funcion f(y) = x^4 + x^3 + x^2 + x, al suministrar diferentes valores a la x'''
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
