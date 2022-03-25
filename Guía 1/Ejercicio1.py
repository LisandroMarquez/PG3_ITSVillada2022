# Inicializar variables y funciones 
numeros = [3,31,21,17,28,43,30,36,7,19,12,4,38,49]
num = 1

# Solicitar el numero
num = int(input("Ingrese un número entre 1 y 50:"))

# Verificar que el numero este en el rango y devolver el indice
if num < 51 and num > 0:
    try:
        print("El indice del numero que indicó es: "+str(numeros.index(num)))
    except:
        print("El número ingresado no se encuentra en la lista")
else:
    print("El número ingresado no se encuentra dentro del rango solicitado")