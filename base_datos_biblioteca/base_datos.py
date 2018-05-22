import sys
from constantes import *
from funciones import *
from listar import *
from modificar import *

def main():
    print()
    print(AVISO_SALIR)
    print()
    datos={}
    cargar_datos(datos)
    operacion=obtener_operacion(OPERACION)
    while True:
        if operacion==SALIR:
            subir_datos(datos)
            sys.exit(0)
        print()
        try:
            _operacion(operacion)(datos)
        except TypeError:
            pass
        print()
        operacion=obtener_operacion(OPERACION)

def dar_alta_libro(base_datos):
    datos=obtener_operacion(DATOS)
    lista_datos=datos.split(",")
    if lista_datos[0] in base_datos:
        print()
        print(YA_ESTA)
        return
    lista_axuliar_datos=[]
    for x in range(1,len(lista_datos)):
        lista_axuliar_datos.append(lista_datos[x])
    base_datos[lista_datos[0]]=lista_axuliar_datos

def dar_baja_libro(base_datos):
    if esta_vacia(base_datos):
        print(BASE_DE_DATOS_VACIA)
        return
    dato=obtener_operacion(DATOS)
    if dato not in base_datos or esta_vacia(base_datos):
        print()
        print(NO_HAY_LIBRO)
        return
    base_datos.pop(dato)

def consultar_libro(base_datos):
    titulo=obtener_operacion(DATOS)
    if titulo in base_datos:
        print()
        print(ESTA)
        return
    print()
    print(NO_ESTA)

def _operacion(operacion):
    lista_operacion=operacion.split()
    funciones={ ALTA:dar_alta_libro,
                BAJA:dar_baja_libro,
                CONSULTA:consultar_libro,
                MODIFICAR:modificar_libro,
                LISTAR_AUTORES:listar_autores,
                LISTAR_LIBROS:listar_libros,
                LISTAR_LIBROS_GENERO:listar_libros_genero,
                LISTAR_LIBROS_AUTOR:listar_libros_autor,
                LISTAR_LIBROS_EDITORIAL:listar_libros_editorial,
                LISTAR_LIBROS_EDITORIAL_EDICION:listar_libros_editorial_edicion,
                LISTAR_EDITORIAL_AUTOR:listar_editorial_autor,
                LISTAR_LIBROS_AÑO:listar_libros_anio,
                LISTAR_LIBROS_AUTOR_LETRA:listar_libros_autor_letra,
                LISTAR_LIBROS_PALABRA:listar_libros_palabra
                }
    if lista_operacion[0].lower()!=LISTAR:
        try:
            return funciones[lista_operacion[0].lower()]
        except KeyError:
            print(OPERACION_INVALIDA)
    else:
        try:
            return funciones[operacion.lower()]
        except KeyError:
            print(OPERACION_INVALIDA)

main()
