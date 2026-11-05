# Datos del problema
# Por simplificación, aquí se incluyen ya los vectores que contienen los datos del problema
# En muchos casos, es probable que tengamos que extraerlos de un fichero externo

#Trabajamos con 20 objetos

# ---

# Problem data
# For simplicity, the vectors containing the problem data are already included here.
# In many cases, it is likely that we will have to extract them from an external file.

# We work with 20 objects

# Descripcion detallada de los objetos (indice, valor, peso, relacion valor/peso):
# Index 0:  valor=12,   peso=10,   relacion=1.2   -> Objeto pequeño
# Index 1:  valor=25,   peso=20,   relacion=1.25
# Index 2:  valor=38,   peso=30,   relacion=1.27
# Index 3:  valor=42,   peso=40,   relacion=1.05
# Index 4:  valor=50,   peso=50,   relacion=1.0   -> Relacion neutra
# Index 5:  valor=55,   peso=15,   relacion=3.67  -> Alto valor/peso
# Index 6:  valor=60,   peso=25,   relacion=2.4   -> Alto valor/peso
# Index 7:  valor=68,   peso=35,   relacion=1.94
# Index 8:  valor=75,   peso=45,   relacion=1.67
# Index 9:  valor=80,   peso=55,   relacion=1.45
# Index 10: valor=85,   peso=65,   relacion=1.31
# Index 11: valor=90,   peso=75,   relacion=1.2
# Index 12: valor=95,   peso=85,   relacion=1.12
# Index 13: valor=100,  peso=95,   relacion=1.05
# Index 14: valor=110,  peso=10,   relacion=11.0  -> Muy alto valor/peso
# Index 15: valor=120,  peso=20,   relacion=6.0   -> Alto valor/peso
# Index 16: valor=130,  peso=30,   relacion=4.33
# Index 17: valor=140,  peso=40,   relacion=3.5
# Index 18: valor=150,  peso=50,   relacion=3.0
# Index 19: valor=160,  peso=60,   relacion=2.67

global __values__
global __weights__
global __knapsackMax__

# valor de cada objeto
# value of each object
#__values__ = [10,200,50,120,200]
__values__ = [12, 25, 38, 42, 50, 55, 60, 68, 75, 80, 85, 90, 95, 100, 110, 120, 130, 140, 150, 160] 

# peso de cada objeto
# weight of each object
#__weights__ = [45,80,25,15,75]
__weights__ = [10, 20, 30, 40, 50, 15, 25, 35, 45, 55, 65, 75, 85, 95, 10, 20, 30, 40, 50, 60] 

# peso maximo que se puede cargar en la mochila
# maximum weight that can be carried in the backpack
#__knapsackMax__ = 200
__knapsackMax__ = 300 