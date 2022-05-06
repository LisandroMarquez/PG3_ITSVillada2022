import pymysql

conexion = pymysql.connect( host='localhost', user= 'bdi', passwd='12345678', db='Ejercicio_6')
cur = conexion.cursor()

try:
    cur.execute( "SEL.ECT nombre, apellido FROM usuarios" )
    for nombre, apellido in cur.fetchall() :
        print (nombre, apellido)
except pymysql.err.ProgrammingError as exc:
    print(f"Error! Error de programación. {exc}")
except pymysql.err.InternalError as exc:
    print(f"Error! Error interno detectado. {exc}")
except pymysql.err.OperationalError as exc:
    print(f"Error! Error de operaciones. {exc}")
except pymysql.err.DataError as exc:
    print(f"Error! Error de datos. {exc}")
except pymysql.err.DatabaseError as exc:
    print(f"Error! Error de la base de datos. {exc}")
except RuntimeError as exc:
    print(f"Error! Error al intentar abrir el archivo. {exc}")
except Exception as exc:
    print(f"Error! Error desconocido. {exc}")
conexion.close()