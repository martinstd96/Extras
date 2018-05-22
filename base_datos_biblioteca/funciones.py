def esta_vacia(base_datos):
    return len(base_datos)==0

def obtener_operacion(mensaje):
    operacion=input(mensaje)
    while len(operacion)==0:
        operacion=input(mensaje)
    return operacion

def obtener_numero(mensaje):
    numero=input(mensaje)
    while not numero.isdigit():
        print()
        numero=input(mensaje)
    return int(numero)

def cargar_datos(base_datos):
    with open("libros.txt") as archivo:
        for linea in archivo:
            lista_datos=linea.rstrip().split(",")
            if len(lista_datos)==1:
                continue
            titulo=lista_datos[0]
            lista_titulo=lista_datos[1:]
            base_datos[titulo]=lista_titulo

def subir_datos(base_datos):
    with open("libros.txt","w") as archivo:
        for titulo in base_datos:
            lista_titulo=base_datos[titulo]
            archivo.write("{},{},{},{},{},{},{}\n".format(titulo,lista_titulo[0],lista_titulo[1],lista_titulo[2],lista_titulo[3],lista_titulo[4],lista_titulo[5]))
