# Inicializar varibles y funciones  
from math import trunc

ancho: int = 0
alto: int = 0
char: str = ""
rta: int = 0
def SquareMatrix(n: int,m: int,a: str) -> str:
    for i in range(n):
        for j in range(m):
            print(a, end = "")
        print("")
def TriangularMatrix(n: int,m: str) -> list[int]:
    for i in range(n + 1):
        for j in range(0, n - i):
            print(end = " ")
        for j in range(n - i, n):
            print(m, end = " ")
        print()
def TriangularMatrix2(n: int,m: str) -> list[int]:
    for i in range(n):
        for j in range(0, i):
            print(end = " ")
        for j in range(i, n):
            print(m, end = " ")
        print()
def DiamondMatrix(n: int,m: str) -> list[int]:
    result1 = [" " * (n - i) + m * (i + i - 1) for i in range(1, n + 1)]
    print("\n".join(result1 + list(reversed(result1[:-1]))))

# Elegit tipo de matriz
while rta != 1 and rta != 2 and rta != 3 and rta != 4:
    rta = int(input("Seleccione la matriz a ejecutar\n- 1 Matriz Paralelipeda\n- 2 Matriz Triangular\n- 3 Matriz Triangular Invertida\n- 4 Matriz Diamante\n"))

# Solicitar datos
if rta == 1:
    print("Usted eligio matriz paralelipeda")
    ancho = int(input("Ingrese el ancho de la matriz: "))
    alto = int(input("Ingrese el alto de la matriz: "))
    char = input("Ingrese el caracter a repetir en la matriz: ")
    # Imprimir la matriz
    SquareMatrix(alto,ancho,char)
if rta == 2:
    print("Usted eligio matriz triangular")
    alto = int(input("Ingresa el número de filas: "))
    char = input("Ingresa el caracter a repetir: ")
    # Imprimir la matriz
    TriangularMatrix(alto,char)
if rta == 3:
    print("Usted eligio matriz triangular invertida")
    alto = int(input("Ingresa el número de filas: "))
    char = input("Ingresa el caracter a repetir: ")
    # Imprimir la matriz
    TriangularMatrix2(alto,char)
if rta == 4:
    print("Usted eligio matriz diamante")
    alto = int(input("Ingresa el número de filas: "))
    char = input("Ingresa el caracter a repetir: ")
    alto_a = trunc(alto/2)+1
    # Imprimir la matriz
    DiamondMatrix(int(alto_a),char)