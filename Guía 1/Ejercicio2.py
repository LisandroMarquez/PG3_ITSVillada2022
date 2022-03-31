# Inicializar variables y funciones  
flag: bool = False
año: int = 0
def Bisiesto(n: int) -> bool:
    if n % 4 != 0: 
        return False
    elif n % 4 == 0 and n % 100 != 0:
        return True
    elif n % 4 == 0 and n % 100 == 0 and n % 400 != 0:
        return False
    elif n % 4 == 0 and n % 100 == 0 and n % 400 == 0:
	    return True

# Solicitar el año
año = int(input("Ingrese un año para comprobar si es bisiesto:"))

# Combrobar si es bisiesto
flag = Bisiesto(año)
if flag == True:
    print("El año "+str(año)+" si es bisiesto")
else:
    print("El año "+str(año)+" no es bisiesto")