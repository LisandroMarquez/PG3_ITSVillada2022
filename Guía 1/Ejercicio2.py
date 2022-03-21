# Inicializar variables y funciones
flag = False
def Bisiesto(n):
    if n % 4 != 0: 
        return False
    elif año % 4 == 0 and año % 100 != 0:
        return True
    elif año % 4 == 0 and año % 100 == 0 and año % 400 != 0:
        return False
    elif año % 4 == 0 and año % 100 == 0 and año % 400 == 0:
	    return True

# Solicitar el año
año = int(input("Ingrese un año para comprobar si es bisiesto:"))

# Combrobar si es bisiesto
flag = Bisiesto(año)
if flag == True:
    print("El año "+str(año)+" si es bisiesto")
else:
    print("El año "+str(año)+" no es bisiesto")