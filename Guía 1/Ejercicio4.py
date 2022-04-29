# Inicializar varibles y funciones  
numeros: list[int] = []
numerosOrdenados: list[int] = []
num: int = 1
flag: bool = True
# Ingresar valores al vector
while flag == True:
    num = int(input("Ingresar números a la matriz (0 para salir): "))
    if num == 0:
        break
    numeros.append(num)

# Copiar el vector
numerosOrdenados = numeros.copy()

# Ordenar el vector
numerosOrdenados.sort(reverse = True)
print(f"Números ingresados: {numeros}")
print(f"Números ordenados: {numerosOrdenados}")