# Inicializar varibles y funciones
def Matriz(n,m,a):
    for i in range(n):
        for i in range(m):
            print(a, end = "")
        print("")

#Solicitar datos
ancho = int(input("Ingrese el ancho de la matriz: "))
alto = int(input("Ingrese el alto de la matriz: "))
char = input("Ingrese el caracter a repetir en matriz: ")

#Pritear la matriz
Matriz(alto,ancho,char)