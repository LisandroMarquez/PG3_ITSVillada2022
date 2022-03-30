# Inicializar varibles y funciones 
vocales: list[str] =    ['a','e','i','o','u',
                        'A','E','I','O','U',
                        'á','é','í','ó','ú',
                        'Á','É','Í','Ó','Ú','ü','Ü']
contador: int = 0
def ContVocales(a: str,b: list) -> int:
    for car in a:
        if car in b:
            contador += 1

# Ingresar la oración
oracion = input("Ingresa una oración: ")

# Devolver la cantidad de vocales
ContVocales(oracion,vocales)
print("La oración ingresada contiene "+str(contador)+" vocales")