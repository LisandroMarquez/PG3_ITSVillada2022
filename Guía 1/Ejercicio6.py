# Inicializar varibles y funciones
vocales = ['a','e','i','o','u','A','E','I','O','U','á','é','í','ó','ú','Á','É','Í','Ó','Ú','ä','ë','ï','ö','ü','Ä','Ë','Ï','Ö','Ü']
contador = 0
def ContVocales(str,list):
    for car in str:
        if car in list:
            contador += 1

# Ingresar la oración
oracion = input("Ingresa una oración: ")

# Devolver la cantidad de vocales
ContVocales(oracion,vocales)
print("La oración ingresada contiene "+str(contador)+" vocales")