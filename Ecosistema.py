import random

class Depredadores:

    def __init__(self, nombre: str, vida: int, fuerza: int):
        self.nombre: int = nombre
        self.vida: int = vida
        self.fuerza: int = fuerza
        


class Presas:
    
    def __init__(self, vida: int, fuerza: int):
        self.vida: int = vida
        self.fuerza: int = fuerza


class Plantas:

    def __init__(self):
        pass


def crear_matriz(n: int, i: int = 0, j: int = 0, fila: list[int] = [], matriz: list[list[int]] = []):
    if i == n:
        return matriz
    
    if j == n:
        matriz.append(fila)
        return crear_matriz(n, i + 1, 0, [], matriz)
    
    fila.append(0)
    return crear_matriz(n, i, j + 1, fila, matriz)


def asignar_elemento(matriz: list[list[int]], elemento: object):
    n = random.randint(1, len(matriz) + 1)
    m = random.randint(1, len(matriz) + 1)
    if matriz[n][m] == 0:
        matriz[n][m] = elemento
    
    else:
        asignar_elemento(matriz, elemento)
    
    return matriz

predador1 = Depredadores("Dinosaurio", 5, 10)

print(asignar_elemento(crear_matriz(5), predador1.nombre))





dificult = int(input("Ingrese el nivel de dificultad: "))