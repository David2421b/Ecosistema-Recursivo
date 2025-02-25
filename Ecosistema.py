import random
import time
from dataclasses import *

inicio = time.time()

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
        emogiD, emogiP, emogiPl = random.randint(0, len(name_depredadores) - 1), random.randint(0, len(name_presas) - 1), random.randint(0, len(name_plantas_comestibles) - 1)
        vida_depredadores, vida_presas = environment_creation.generar_vidas(random.randint(1, 11)), environment_creation.generar_vidas(random.randint(1, 7))
        lista.append(Depredadores(name_depredadores[emogiD], vida_depredadores))
        lista.append(Presas(name_presas[emogiP], vida_presas))
        lista.append(Plantas(name_plantas_comestibles[emogiPl]))
        return environment_creation.crear_objetos(num_objects, idx + 1, lista)

    def generar_vidas(n: int, idx: int = 0, vida: str =""):
        if n == idx:
            return vida
        return environment_creation.generar_vidas(n, idx + 1, vida + "❤️ ")
               


    def asignar_elemento(matriz: list[list[int]], lista: list[object], idx = 0) -> list[list[int]]:
        i, j = random.randint(0, len(matriz) - 1), random.randint(0, len(matriz) - 1)
        if idx == len(lista):
            return matriz
        if matriz[i][j] == "___":
            matriz[i][j] = lista[idx]
        else: 
            return environment_creation.asignar_elemento(matriz, lista, idx)   
        return environment_creation.asignar_elemento(matriz, lista, idx + 1)


@dataclass
class Play:

    def proximo_movimiento(matriz: list[list[object]], i: int = 0, j: int = 0):
        pass

    def adyacente_ortogonal(x1, x2, y1, y2):
        if (abs(x1 - x2) == 1 and y1 == y2) or (abs(y1 - y2) == 1 and x1 == x2):
            return True
        return False

print(environment_creation.asignar_elemento(environment_creation.crear_matriz(6), environment_creation.crear_objetos(5)))

fin = time.time()

print(f"\nel tiempo de ejecucion fue: {fin - inicio:.6f} segundos")


#dificultad = int(input("Ingrese el tamaño de la matriz: "))

# if __name__ =="__main__":
#     environment_creation.crear_matriz(6)