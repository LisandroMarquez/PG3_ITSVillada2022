# Inicializar varibles y funciones  
vocales: list[str] =    ['a','e','i','o','u',
                        'A','E','I','O','U',
                        'á','é','í','ó','ú',
                        'Á','É','Í','Ó','Ú','ü','Ü']
cont: int = 0
oracion: str = ""
def ContVocales(a: str,b: list) -> int:
    i: int = 0
    car: str
    for car in a:
        if car in b:
            i += 1
    return i

# Ingresar la oración
oracion = input("Ingresa una oración: ")

# Devolver la cantidad de vocales
cont = ContVocales(oracion,vocales)
print("La oración ingresada contiene "+str(cont)+" vocales")