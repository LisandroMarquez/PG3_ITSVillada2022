# Inicializar variables y funciones
flag = False
def NumStep(num):
    for i in range(0, len(num), 2):
        if not (int(num[i:i + 2][0]) + 1 == int(num[i:i + 2][1]) or int(num[i:i + 2][0]) - 1 == int(num[i:i + 2][1])):
            return False
    return True

# Ingresar el numero
num = input("Ingrese un número: ")

# Comprobar si es un Número Step
flag = NumStep(num)
if flag == True:
    print("El número ingresado es un Número Step")
else:
    print("El número ingresado NO es un Número Step")