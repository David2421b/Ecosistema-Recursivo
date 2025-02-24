import random

class Depredadores:

    def __init__(self, nombre: str, vida: int):
        self.nombre: int = nombre
        self.vida: int = vida

    
    def __repr__(self):
        return f"{self.nombre} \n Vida: {self.vida}"

class Presas:
    
    def __init__(self, nombre: str, vida: int):
        self.nombre: str = nombre
        self.vida: int = vida
    
    def __repr__(self):
        return f"{self.nombre} \n Vida: {self.vida}"


class Plantas:

    def __init__(self, nombre: str, vida: int = 0):
        self.nombre: str = nombre
        self.vida: int = vida

    def __repr__(self):
        return f"{self.nombre}"


def crear_matriz(n: int, i: int = 0, j: int = 0, fila: list[int] = [], matriz: list[list[int]] = []) -> list[list[int]]:
    if i == n:
        return matriz
    
    if j == n:
        matriz.append(fila)
        return crear_matriz(n, i + 1, 0, [], matriz)
    
    fila.append(0)
    return crear_matriz(n, i, j + 1, fila, matriz)


def crear_objetos(num_objects: int, idx = 0, lista: list = []) -> list[object]:
    if num_objects == idx:
        return lista
    
    name_depredadores = [
        "León", "Tigre", "Lobo", "Águila", "Tiburón blanco",
        "Cocodrilo", "Oso pardo", "Serpiente pitón", "Guepardo", "Orca",
        "Jaguar", "Hiena", "Zorro", "Dragón de Komodo", "Leopardo de las nieves"
    ]


    name_presas = [
        "Conejo", "Venado", "Cebra", "Ratón", "Pez pequeño",
        "Liebre", "Gacela", "Paloma", "Canguro", "Rana",
        "Ardilla", "Ciervo", "Topo", "Gallina", "Antílope"
    ]


    naem_plantas_comestibles = [
        "Lechuga", "Zanahoria", "Papa", "Tomate", "Espinaca",
        "Manzana", "Fresas", "Trigo", "Maíz", "Plátano",
        "Cebolla", "Perejil", "Pepino", "Uva", "Brócoli"
    ]

    ran1, ran2, ran3 = random.randint(0, len(name_depredadores) - 1), random.randint(0, len(name_presas) - 1), random.randint(0, len(naem_plantas_comestibles) - 1)
    vida_depredadores, vida_presas = random.randint(1, 11), random.randint(1, 8)

    lista.append(Depredadores(name_depredadores[ran1], vida_depredadores))
    lista.append(Presas(name_presas[ran2], vida_presas))
    lista.append(Plantas(naem_plantas_comestibles[ran3]))


    return crear_objetos(num_objects, idx + 1, lista)

    


def asignar_elemento(matriz: list[list[int]], elemento: object):
    n = random.randint(0, len(matriz) - 1)
    m = random.randint(0, len(matriz) - 1)
    print(f"n es {n} y m es {m}")
    if matriz[n][m] == 0:
        matriz[n][m] = elemento
    
    else:
        asignar_elemento(matriz, elemento)
    
    return matriz


print(crear_objetos(5))





#dificult = int(input("Ingrese el nivel de dificultad: "))