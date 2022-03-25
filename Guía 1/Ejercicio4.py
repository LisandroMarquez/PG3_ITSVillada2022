# Inicializar varibles y funciones 
numeros = []
numerosOrdenados = []
num = 1
flag = True
# Ingresar valores al vector
while flag:
    num = int(input("Ingresar numeros a la matriz (0 para salir):"))
    if num == 0:
        break
    numeros.append(num)
numerosOrdenados = numeros.copy() # Copiar el vector

# Ordenar el vector
numerosOrdenados.sort(reverse = True)
print(numeros)
print(numerosOrdenados)