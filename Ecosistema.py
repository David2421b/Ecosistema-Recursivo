import random
import time
from dataclasses import *
import sys
sys.setrecursionlimit(100000)


inicio = time.time()

def start():
    dificultad = int(input("""Seleccione el nivel que quieres Jugar\n     1. Matriz 4x4 y 4 de cada especie\n     2. Matriz 5x5 y 6 de cada especie\n     3. Matriz 6x6 y 8 de cada especie\n     4. Tu pones las reglas 😏 \nSeleccion: """))
    if dificultad not in [1, 2, 3, 4]:
        print("\n¡Ingrese un numero valido de las opciones!\n")
        time.sleep(1.5)
        return start()
    world = environment_creation.tamaño_matriz(dificultad)
    print(f"\n¡Así arranca el juego! \n\n{world}")
    game(world)


def game(world: list[list[str]], idx: int = 0):
    if idx == 10:
        return
    time.sleep(1)
    print()
    secuencia = Play.movimiento_general(world)
    print(secuencia)
    return game(secuencia, idx + 1)




class Depredadores:

    def __init__(self, nombre: str, vida: str):
        self.nombre: str = nombre
        self.vida: str = vida
    
    def __repr__(self):
        return f"{self.nombre} ({self.vida})"


class Presas:
    
    def __init__(self, nombre: str, vida: str):
        self.nombre: str = nombre
        self.vida: str = vida
    
    def __repr__(self):
        return f"{self.nombre} ({self.vida})"


class Frutas:

    def __init__(self, nombre: str, vida: str = ""):
        self.nombre: str = nombre
        self.vida: str = vida

    def __repr__(self):
        return f"{self.nombre}"


class environment_creation:
    def tamaño_matriz(num):
        match num:
            case 1:
                return environment_creation.asignar_elemento(environment_creation.crear_matriz(4), environment_creation.crear_objetos(4))
            case 2:
                return environment_creation.asignar_elemento(environment_creation.crear_matriz(5), environment_creation.crear_objetos(6))
            case 3:
                return environment_creation.asignar_elemento(environment_creation.crear_matriz(6), environment_creation.crear_objetos(8))
            case 4:
                n = int(input("Ingresa el tamaño de la matriz: "))
                m = int(input("Ingresa la cantidad de elementos por especie: "))
                if n * n <= m * 3:
                    print("     \n¡Por favor verifique que la cantidad de especies no supere ni sea igual a la cantidad de espacios!\n")
                    time.sleep(1.5)
                    return environment_creation.tamaño_matriz(4)
                return environment_creation.asignar_elemento(environment_creation.crear_matriz(n), environment_creation.crear_objetos(m))


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
        name_depredadores = ["🦁", "🐅", "🐺", "🦅", "🦈", "🐊", "🐻", "🐍", "🐆", "🦛", "🦊", "🦎", "🦜", "🐗", "🐉", "🦂", "🦟", "🦀"]
        name_presas = ["🐰", "🦌", "🦓", "🐭", "🐇", "🕊️", "🦘", "🐿️", "🦡", "🐔", "🐹", "🐀", "🐄", "🐑", "🐖", "🦤", "🐥", "🦆", "🐦"]
        name_plantas_comestibles = ["🥕", "🥔", "🍅", "🍏", "🍓", "🌽", "🍌", "🧅", "🥒", "🍇", "🥦", "🍍", "🍒", "🍑", "🍈", "🥭", "🥑"]
        emogiD, emogiP, emogiF = random.randint(0, len(name_depredadores) - 1), random.randint(0, len(name_presas) - 1), random.randint(0, len(name_plantas_comestibles) - 1)
        vida_depredadores, vida_presas = environment_creation.generar_vidas(random.randint(1, 4)), environment_creation.generar_vidas(random.randint(1, 2))
        lista.extend([Depredadores(name_depredadores[emogiD], vida_depredadores), Presas(name_presas[emogiP], vida_presas), Frutas(name_plantas_comestibles[emogiF])])
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


class Play:
    
    @staticmethod
    def movimiento_general(matriz: list[list[object]], i: int = 0, j: int = 0, idx: int = 0):
        if i == len(matriz):
            return matriz
        
        if isinstance(matriz[i][j], Depredadores):
            arriba = Play.observador_arriba(matriz, i ,j)
            abajo = Play.observador_abajo(matriz, i , j)
            derecha = Play.observador_derecha(matriz, i , j)
            izquierda = Play.observador_izquierda(matriz, i , j)
            mayor = max(arriba, abajo, derecha, izquierda)

            if mayor == arriba:
                newD, mewD = i - 1, j
            elif mayor == abajo:
                newD, mewD = i + 1, j
            elif mayor == derecha:
                newD, mewD = i , j +1
            else:
                newD, mewD = i , j - 1


            if matriz[newD][mewD] == "___":
                matriz[newD][mewD] = matriz[i][j]
                matriz[i][j] = "___"      

            elif isinstance(matriz[newD][mewD], Presas):
                depredador = matriz[i][j]
                presa = matriz[newD][mewD]
                if len(depredador.vida) > len(presa.vida):
                    matriz[newD][mewD] = matriz[i][j]
                    matriz[i][j] = "___"
                    depredador.vida =  depredador.vida[:len(presa.vida)]
                else:
                    matriz[newD][mewD] = matriz[newD][mewD]
                    presa.vida = presa.vida[:len(depredador.vida)]

            elif isinstance(matriz[newD][mewD], Frutas):
                matriz[newD][mewD] = matriz[i][j]
                matriz[i][j] = "___"
        

        if isinstance(matriz[i][j], Presas):
            newP = i + random.randint(-1, 1)
            mewP = j + random.randint(-1, 1)
            newP = max(0, min(newP, len(matriz) - 1))
            mewP = max(0, min(mewP, len(matriz[0]) - 1))

            if matriz[newP][mewP] == "___":
                matriz[newP][mewP] = matriz[i][j]
                matriz[i][j] = "___"

            elif isinstance(matriz[newP][mewP], Depredadores):
                presa = matriz[i][j]
                depredador = matriz[newP][mewP]
                if len(depredador.vida) > len(presa.vida):
                    matriz[i][j] = matriz[newP][mewP]
                    matriz[newP][mewP] = "___"
                    depredador.vida = depredador.vida[:len(presa.vida)]
                else:
                    matriz[i][j] = matriz[i][j]
                    presa.vida = presa.vida[:len(depredador.vida)]
                
            elif isinstance(matriz[newP][mewP], Frutas):
                presa = matriz[i][j]
                matriz[newP][mewP] = matriz[i][j]
                presa.vida = presa.vida + "❤️ "


        if isinstance(matriz[i][j], Frutas) and idx >= 4:
            n, m = random.randint(0, len(matriz) - 1), random.randint(0, len(matriz[0]) - 1)
            if matriz[n][m] == "___":
                matriz[n][m] = matriz[i][j]
                idx = 0

        
        if j + 1 < len(matriz):
            return Play.movimiento_general(matriz, i, j + 1, idx + 1)
        return Play.movimiento_general(matriz, i + 1, 0, idx + 1)
    

    def observador_arriba(matriz: list[list[str]], i: int, j: int, idx: int = 0) -> int:
        if i < 0:
            return -1    
        if isinstance(matriz[i][j], Presas):
            return idx
        return Play.observador_arriba(matriz, i - 1, j, idx + 1)
    

    def observador_abajo(matriz: list[list[str]], i: int, j: int, idx: int = 0) -> int:
        if i == len(matriz):
            return -1
        if isinstance(matriz[i][j], Presas):
            return idx
        return Play.observador_abajo(matriz, i + 1, j, idx + 1)
    
        
    def observador_derecha(matriz: list[list[str]], i: int, j:int, idx : int = 0) -> int:
        if j == len(matriz[0]):
            return -1
        if isinstance(matriz[i][j], Presas):
            return idx
        return Play.observador_derecha(matriz, i, j + 1, idx + 1)
    

    def observador_izquierda(matriz: list[list[str]], i: int, j: int, idx: int = 0) -> int:
        if j < 0:
            return -1
        if isinstance(matriz[i][j], Presas):
            return idx
        return Play.observador_izquierda(matriz, i, j - 1, idx + 1)
    
         

fin = time.time()
print(f"\nel tiempo de ejecucion fue: {fin - inicio:.6f} segundos")


if __name__ =="__main__":
    start()