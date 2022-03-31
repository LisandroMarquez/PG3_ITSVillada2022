# Inicializar varibles y funciones  
ancho: int = 0
alto: int = 0
char: str = ""
def Matriz(n: int,m: int,a: str) -> str:
    i: int = 0
    for i in range(n):
        for i in range(m):
            print(a, end = "")
        print("")

#Solicitar datos
ancho = int(input("Ingrese el ancho de la matriz: "))
alto = int(input("Ingrese el alto de la matriz: "))
char = input("Ingrese el caracter a repetir en la matriz: ")

#Printear la matriz
Matriz(alto,ancho,char)