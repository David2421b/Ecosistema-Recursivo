import random
import time
from dataclasses import *


class Depredadores:

    def __init__(self, nombre: str, vida: int):
        self.nombre: str = nombre
        self.vida: int = vida
    
    def __repr__(self):
        return f"{self.nombre} ({self.vida})"


class Presas:
    
    def __init__(self, nombre: str, vida: int):
        self.nombre: str = nombre
        self.vida: int = vida
    
    def __repr__(self):
        return f"{self.nombre} ({self.vida})"


class Plantas:

    def __init__(self, nombre: str, vida: int = 0):
        self.nombre: str = nombre
        self.vida: int = vida

    def __repr__(self):
        return f"{self.nombre}"

@dataclass
class environment_creation:

    def crear_matriz(n: int, i: int = 0, j: int = 0, fila: list[str] = [], matriz: list[list[str]] = []) -> list[list[str]]:       
        if i == n:
            return matriz
        if j == n:
            matriz.append(fila)
            return environment_creation.crear_matriz(n, i + 1, 0, [], matriz)
        fila.append("___")
        return environment_creation.crear_matriz(n, i, j + 1, fila, matriz)

    def crear_objetos(num_objects: int, idx = 0, lista: list = []) -> list[object]:
        if num_objects == idx:
            return lista
        name_depredadores = ["🦁", "🐅", "🐺", "🦅", "🦈", "🐊", "🐻", "🐍", "🐆", "🐋", "🦛", "🦊", "🦎", "❄️🐆", "🦜", "🐗", "🐉", "🦂", "🦟", "🦀"]
        name_presas = ["🐰", "🦌", "🦓", "🐭", "🐇", "🕊️", "🦘", "🐿️", "🦡", "🐔", "🐹", "🐀", "🐄", "🐑", "🐖", "🦤", "🐥", "🦆", "🐦"]
        name_plantas_comestibles = ["🥕", "🥔", "🍅", "🍏", "🍓", "🌾", "🌽", "🍌", "🧅", "🥒", "🍇", "🥦", "🍍", "🍒", "🍑", "🍈", "🥭", "🥑"]
        ran1, ran2, ran3 = random.randint(0, len(name_depredadores) - 1), random.randint(0, len(name_presas) - 1), random.randint(0, len(name_plantas_comestibles) - 1)
        vida_depredadores, vida_presas = random.randint(1, 11), random.randint(1, 8)
        lista.append(Depredadores(name_depredadores[ran1], vida_depredadores))
        lista.append(Presas(name_presas[ran2], vida_presas))
        lista.append(Plantas(name_plantas_comestibles[ran3]))
        return environment_creation.crear_objetos(num_objects, idx + 1, lista)

    def asignar_elemento(matriz: list[list[int]], lista: list[object], idx = 0):
        n, m = random.randint(0, len(matriz) - 1), random.randint(0, len(matriz) - 1)
        if idx == len(lista):
            return matriz
        if matriz[n][m] == "___":
            matriz[n][m] = lista[idx]
        else: 
            return environment_creation.asignar_elemento(matriz, lista, idx)   
        return environment_creation.asignar_elemento(matriz, lista, idx + 1)




print(environment_creation.asignar_elemento(environment_creation.crear_matriz(6), environment_creation.crear_objetos(5)))

#dificultad = int(input("Ingrese el tamaño de la matriz: "))
