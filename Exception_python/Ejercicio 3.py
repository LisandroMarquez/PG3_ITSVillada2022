tupla: tuple[str] = ("Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre")
flag: bool = True
mes: int = 0
x: int = 0
while flag:
    try:
        mes = int(input("Ingrese el número de mes que desea: "))
        if mes == 0:
            raise ValueError
        else:
            print(f"El mes ingresado es: {tupla[mes - 1]}")
    except ValueError as exc:
        print(f"Error! Por favor, ingrese un número {exc.args}")
    except IndexError as exc:
        print(f"Error! El número ingresado está fuera de rango {exc.args}")
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
        print(f"Error! Error desconocido {exc.args}")
    except BaseException as exc:
        print(f"Error! Error desconocido {exc.args}")