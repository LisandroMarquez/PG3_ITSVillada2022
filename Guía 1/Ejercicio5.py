# Inicializar varibles y funciones 
flag: bool = False
palabra: str = ""
def Palindromo(a: str) -> bool:
    return a == a[::-1] # Verifica que el caracter 0 sea igual al -1(el último) y así sucesivamente
 
# Ingresar la palabra
palabra = input("Ingrese una palabra para determinar si es un palíndromo:")

# Comprobar si es un palíndromo
flag = Palindromo(palabra)
if flag == True:
    print('La palabra "'+palabra+'" si es un palíndromo')
else:
    print('La palabra "'+palabra+'" no es un palíndromo')