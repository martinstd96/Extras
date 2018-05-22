def agregar_producto(almacenamiento):
    datos=pedir_operacion_dato_producto(MENSAJE_PRODUCTO)
    lista_producto=datos.split(",")
    agregar_producto_(almacenamiento,lista_producto)

def agregar_producto_(almacenamiento,lista_producto):
    codigo=int(lista_producto[0])
    descripcion=lista_producto[1]
    stock=int(lista_producto[2])
    precio=int(lista_producto[3])
    fecha=lista_producto[4]
    tipo=lista_producto[5]
    almacenamiento[codigo]=[descripcion,stock,precio,fecha,tipo]

def eliminar_producto(almacenamiento):
    codigo=pedir_unidades(MENSAJE_CODIGO)
    if codigo not in almacenamiento:
        print(NO_CODIGO)
        return
    eliminar_producto_(almacenamiento,codigo)

def eliminar_producto_(almacenamiento,codigo):
    almacenamiento.pop(codigo)
