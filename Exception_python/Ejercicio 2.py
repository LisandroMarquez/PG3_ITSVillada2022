flag: bool = True
while flag:
    try:
        numero1: int = int(input("Ingrese el primer numero: "))
        numero2: int = int(input("Ingrese el segundo numero: "))
        print(f"La división entre {numero1} y {numero2} es: {numero1 / numero2}")
    except ZeroDivisionError as exc:
        print(f"Error! No se puede dividir entre 0 {exc.args}")
    except ValueError as exc:
        print(f"Error! No se puede dividir con caracteres {exc.args}")
    except BaseException as exc:
        print(f"Error! Error desconocido {exc.args}")
    try:
        x = int(input("¿Desea continuar? (0 para salir, otro para continuar): "))
        if x == 0:
            print("Fin del programa")
            flag = False
    except ValueError as exc:
        print(f"Error! Por favor, ingrese un número {exc.args}")
    except NameError as exc:
        print(f"Error! Por favor, ingrese un número {exc.args}")
    except BaseException as exc:
        print(f"Error! Error desconocido {exc.args}")