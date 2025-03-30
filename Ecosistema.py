import random
import threading
import time
from dataclasses import *
import sys

sys.setrecursionlimit(100000)


def start():
    dificultad = int(input("""Seleccione el nivel que quieres Jugar\n     1. Matriz 4x4 y 4 de cada especie\n     2. Matriz 5x5 y 6 de cada especie\n     3. Matriz 6x6 y 8 de cada especie\n     4. Tu pones las reglas 😏 \nSeleccion: """))
    if dificultad not in [1, 2, 3, 4]:
        print("\n¡Ingrese un numero valido de las opciones!\n")
        time.sleep(3.5)
        return start()
    world = environment_creation()
    world2 = world.tamaño_matriz(dificultad)
    print(f"\n¡Así arranca el juego! \n\n")
    imprimir_matriz(world2)
    game(world2)

def game(world: list[list[str]], idx: int = 0):
    if idx == 10:
        return
    time.sleep(1)
    print(f"----------------------------------------------------------------\n\n                        MOVIMIENTO: {idx + 1}\n")
    secuencia = Play()
    secuencia2 = secuencia.movimiento_general(world)
    imprimir_matriz(secuencia2)
    return game(secuencia2, idx + 1)

def imprimir_matriz(matriz):
    print("\n\n".join([" | ".join(map(str, fila)) for fila in matriz]))

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
        return f"{self.nombre} 🄲 🄾 🄼 🄴 🅁  "


class environment_creation:

    def tamaño_matriz(self, num):
        match num:
            case 1:
                cantidad_objetos_1 = self.crear_objetos(4)
                tamaño_matriz_1 = self.crear_matriz(4)
                mundo_1 = self.asignar_elemento(tamaño_matriz_1, cantidad_objetos_1)
                return mundo_1
            case 2:
                cantidad_objetos_2 = self.crear_objetos(6)
                tamaño_matriz_2 = self.crear_matriz(5)
                mundo_2 = self.asignar_elemento(tamaño_matriz_2, cantidad_objetos_2)
                return mundo_2
            case 3:
                cantidad_objetos_3 = self.crear_objetos(8)
                tamaño_matriz_3 = self.crear_matriz(6)
                mundo_3 = self.asignar_elemento(tamaño_matriz_3, cantidad_objetos_3)
                return mundo_3
            case 4:
                n = int(input("Ingresa el tamaño de la matriz: "))
                m = int(input("Ingresa la cantidad de elementos por especie: "))
                if n * n <= m * 3:
                    print("     \n¡Por favor verifique que la cantidad de especies no supere ni sea igual a la cantidad de espacios!\n")
                    time.sleep(1.5)
                    return self.tamaño_matriz(4)
                return self.asignar_elemento(self.crear_matriz(n), self.crear_objetos(m))

    def crear_matriz(self, n: int, i: int = 0, j: int = 0, fila: list[str] = [], matriz: list[list[str]] = []) -> list[list[str]]:       
        if i == n:
            return matriz
        if j == n:
            matriz.append(fila)
            return self.crear_matriz(n, i + 1, 0, [], matriz)
        fila.append(" □□□□□□ ")
        return self.crear_matriz(n, i, j + 1, fila, matriz)

    def crear_objetos(self, num_objects: int, idx = 0, lista: list = []) -> list[object]:
        if num_objects == idx:
            return lista
        name_depredadores = ["🦁", "🐅", "🐺", "🦅", "🦈", "🐊", "🐻", "🐍", "🐆", "🦛", "🦊", "🦎", "🦜", "🐗", "🐉", "🦂", "🦟", "🦀"]
        name_presas = ["🐰", "🦌", "🦓", "🐭", "🐇", "🕊️", "🦘", "🐿️", "🦡", "🐔", "🐹", "🐀", "🐄", "🐑", "🐖", "🦤", "🐥", "🦆", "🐦"]
        name_plantas_comestibles = ["🥕", "🥔", "🍅", "🍏", "🍓", "🌽", "🍌", "🧅", "🥒", "🍇", "🥦", "🍍", "🍒", "🍑", "🍈", "🥭", "🥑"]
        emogiD, emogiP, emogiF = random.randint(0, len(name_depredadores) - 1), random.randint(0, len(name_presas) - 1), random.randint(0, len(name_plantas_comestibles) - 1)
        vida_depredadores, vida_presas = self.generar_vidas(random.randint(1, 4)), self.generar_vidas(random.randint(1, 2))
        lista.extend([Depredadores(name_depredadores[emogiD], vida_depredadores), Presas(name_presas[emogiP], vida_presas), Frutas(name_plantas_comestibles[emogiF])])
        return self.crear_objetos(num_objects, idx + 1, lista)

    def generar_vidas(self, n: int, idx: int = 0, vida: str =""):
        if n == idx:
            return vida
        return self.generar_vidas(n, idx + 1, vida + "❤️ ")
               
    def asignar_elemento(self, matriz: list[list[int]], lista: list[object], idx = 0) -> list[list[int]]:
        i, j = random.randint(0, len(matriz) - 1), random.randint(0, len(matriz) - 1)
        if idx == len(lista):
            return matriz
        if matriz[i][j] == " □□□□□□ ":
            matriz[i][j] = lista[idx]
        else: 
            return self.asignar_elemento(matriz, lista, idx)   
        return self.asignar_elemento(matriz, lista, idx + 1)


class Play:
    
    def movimiento_general(self, matriz: list[list[object]], i: int = 0, j: int = 0, idxF: int = 0):
        if i == len(matriz):
            return matriz

        self.depredador_movimiento(matriz, i ,j)
        limite_comida = self.presa_movimiento(matriz, i, j, limite_comida)
        self.fruta_movimiento(matriz, i, j, idxF)

        if j + 1 < len(matriz):
            return self.movimiento_general(matriz, i, j + 1, idxF + 1)
        return self.movimiento_general(matriz, i + 1, 0, idxF + 1)
    

    def depredador_movimiento(self, matriz, i, j):
        if isinstance(matriz[i][j], Depredadores):
            arriba = self.observador_arriba(matriz, i ,j)
            abajo = self.observador_abajo(matriz, i , j)
            derecha = self.observador_derecha(matriz, i , j)
            izquierda = self.observador_izquierda(matriz, i , j)
            mayor = max(arriba, abajo, derecha, izquierda)

            if mayor == arriba:
                newD, mewD = i - 1, j
            elif mayor == abajo:
                newD, mewD = i + 1, j
            elif mayor == derecha:
                newD, mewD = i , j +1
            else:
                newD, mewD = i , j - 1

            if matriz[newD][mewD] == " □□□□□□ ":
                matriz[newD][mewD] = matriz[i][j]
                matriz[i][j] = " □□□□□□ " 

            elif isinstance(matriz[newD][mewD], Presas):
                depredador = matriz[i][j]
                presa = matriz[newD][mewD]
                if len(depredador.vida) > len(presa.vida):
                    matriz[newD][mewD] = matriz[i][j]
                    matriz[i][j] = " □□□□□□ "
                    depredador.vida =  depredador.vida[:len(presa.vida)]
                    depredador.vida = depredador.vida + "❤️ "
                else:
                    matriz[newD][mewD] = matriz[newD][mewD] 
                    presa.vida = presa.vida[:len(depredador.vida)]

            elif isinstance(matriz[newD][mewD], Frutas):
                matriz[newD][mewD] = matriz[i][j]
                matriz[i][j] = " □□□□□□ "
            
            elif isinstance(matriz[newD][mewD], Depredadores):
                matriz[i][j], matriz[newD][mewD] = matriz[newD][mewD], matriz[i][j]


    def presa_movimiento(self, matriz, i, j, frutas_comidas: int = 0):
        if isinstance(matriz[i][j], Presas):
            newP = i + random.randint(-1, 1)
            mewP = j + random.randint(-1, 1)
            newP = max(0, min(newP, len(matriz) - 1))
            mewP = max(0, min(mewP, len(matriz[0]) - 1))

            if matriz[newP][mewP] == " □□□□□□ ":
                matriz[newP][mewP] = matriz[i][j]
                matriz[i][j] = " □□□□□□ "
            
            elif isinstance(matriz[newP][mewP], Depredadores):
                presa = matriz[i][j]
                depredador = matriz[newP][mewP]
                if len(depredador.vida) > len(presa.vida):
                    matriz[i][j] = matriz[newP][mewP]
                    matriz[newP][mewP] = " □□□□□□ "
                    depredador.vida = depredador.vida[:len(presa.vida)]
                else:
                    matriz[i][j] = matriz[i][j]
                    presa.vida = presa.vida[:len(depredador.vida)]
                    
            elif isinstance(matriz[newP][mewP], Presas) and matriz[newP][mewP].nombre == matriz[i][j].nombre and len(matriz[i][j].vida) > 2 and len(matriz[newP][mewP].vida) > 2:
                newP2, mewP2 = random.randint(0, len(matriz) - 1), random.randint(0, len(matriz) - 1)
                if matriz[newP2][mewP2] == " □□□□□□ ":
                    matriz[newP2][mewP2] = matriz[i][j]  
            
            elif isinstance(matriz[newP][mewP], Frutas):
                presa = matriz[i][j]
                if len(presa.vida) <= 3:
                    matriz[newP][mewP] = matriz[i][j]
                    presa.vida = presa.vida + "❤️ "
                    return frutas_comidas + 1

    def fruta_movimiento(self, matriz, i, j, idxF):
        if isinstance(matriz[i][j], Frutas) and idxF >= 6:
            n, m = random.randint(0, len(matriz) - 1), random.randint(0, len(matriz[0]) - 1)
            if matriz[n][m] == " □□□□□□ ":
                matriz[n][m] = matriz[i][j]
                idxF = 0



    def observador_arriba(self, matriz: list[list[str]], i: int, j: int, counter: int = 0) -> int:
        if i < 0:
            return -1    
        if isinstance(matriz[i][j], Presas):
            return counter
        return self.observador_arriba(matriz, i - 1, j, counter + 1)
    
    def observador_abajo(self, matriz: list[list[str]], i: int, j: int, counter: int = 0) -> int:
        if i == len(matriz):
            return -1
        if isinstance(matriz[i][j], Presas):
            return counter
        return self.observador_abajo(matriz, i + 1, j, counter + 1)
        
    def observador_derecha(self, matriz: list[list[str]], i: int, j:int, counter : int = 0) -> int:
        if j == len(matriz[0]):
            return -1
        if isinstance(matriz[i][j], Presas):
            return counter
        return self.observador_derecha(matriz, i, j + 1, counter + 1) 

    def observador_izquierda(self, matriz: list[list[str]], i: int, j: int, counter: int = 0) -> int:
        if j < 0:
            return -1
        if isinstance(matriz[i][j], Presas):
            return counter
        return self.observador_izquierda(matriz, i, j - 1, counter + 1)


if __name__ == "__main__":
    start()