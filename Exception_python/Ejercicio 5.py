try:
    var = open('a.txt', "w")
    var.write(45)
    var.close()
except IOError as exc:
    print(f"Error! No se pudo abrir el archivo. {exc}")
except TypeError as exc:
    print(f"Error! El tipo de dato ingresado no es correcto. {exc}")
except Exception as exc:
    print(f"Error! Error desconocido. {exc}")