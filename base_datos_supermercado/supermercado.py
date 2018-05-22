import sys
from constantes import *
from pedir import*
from agregar_eliminar import *
from venta import*

def main():
    print(MENSAJE_TERMINAR)
    print()
    almacenamiento={}
    datos_envios={}
    cargar_datos(almacenamiento)
    envios=0
    operacion=pedir_operacion_dato_producto(MENSAJE_PRINCIPAL)
    while True:
        if operacion==ENVIO:
            realizar_envio_a_domicilio(datos_envios,envios)
            envios+=1
        elif operacion=='#':
            guardar_datos(almacenamiento)
            sys.exit(0)
        else:
            try:
                ejecutar_operacion(operacion)(almacenamiento)
            except TypeError:
                pass
        operacion=pedir_operacion_dato_producto(MENSAJE_PRINCIPAL)

def cargar_datos(almacenamiento):
    with open(ARCHIVO_DATOS) as archivo_entrada:
        for linea in archivo_entrada:
            lista_producto=linea.rstrip().split(",")
            agregar_producto_(almacenamiento,lista_producto)

def guardar_datos(almacenamiento):
    with open(ARCHIVO_DATOS,"w") as archivo_salida:
        for codigo in almacenamiento:
            lista_producto=almacenamiento[codigo]
            descripcion,stock,precio,fecha,tipo=lista_producto
            archivo_salida.write("{},{},{},{},{},{}\n".format(codigo,descripcion,stock,precio,fecha,tipo))

def listar_productos(almacenamiento):
    encabezado=TUPLA_ENCABEZADO
    print("{}        {}        {}       {}       {}       {}".format(encabezado[0],encabezado[1],encabezado[2],encabezado[3],encabezado[4],encabezado[5]))
    for codigo in almacenamiento:
            imprimir_productos(codigo,almacenamiento[codigo])

def imprimir_productos(codigo,lista_producto):
    print("{}          {}         {}          {}           {}         {}".format(codigo,lista_producto[0],lista_producto[1],lista_producto[2],lista_producto[3],lista_producto[4]))

def realizar_envio_a_domicilio(datos_envios,cantidad_envios):
    print(MENSAJE_DATOS_ENVIOS)
    print()
    datos=pedir_operacion_dato_producto(MENSAJE_ENVIOS)
    lista_datos=datos.split(",")
    DNI=int(lista_datos[0])
    nombre_apelldio=lista_datos[1]
    telefono=int(lista_datos[2])
    domicilio=lista_datos[3]
    piso=int(lista_datos[4])
    depto=lista_datos[5]
    datos_envios[cantidad_envios]=[DNI,nombre_apelldio,telefono,domicilio,piso,depto]

def actualizar_precio(almacenamiento):
    codigo=pedir_unidades(MENSAJE_CODIGO)
    porcentaje=pedir_unidades(MENSAJE_PORCENTAJE)/100
    if codigo not in almacenamiento:
        print(NO_CODIGO)
        return
    lista_producto=almacenamiento[codigo]
    incremento=lista_producto[2]*porcentaje
    lista_producto[2]+=incremento
    almacenamiento[codigo]=lista_producto

def ejecutar_operacion(operacion):
    funciones={AGREGAR:agregar_producto,
                ELIMINAR:eliminar_producto,
                LISTAR:listar_productos,
                VENTA:realizar_venta,
                ACTUALIZAR_PRECIO:actualizar_precio,
                }
    try:
        return funciones[operacion]
    except KeyError:
        print(NO_OPERACION)
        return

main()
