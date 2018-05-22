from constantes import *
from funciones import *

def modificar_libro(base_datos):
    titulo=obtener_operacion(TITULO_PEDIDO)
    if  _no_esta(titulo,base_datos):
        print()
        print(NO_HAY_LIBRO)
        return
    print()
    datos=obtener_operacion(DATOS_MODIFICAR)
    lista_datos=datos.split(",")
    for x in range(len(lista_datos)):
        print()
        dato=lista_datos[x]
        if dato==TITULO and x<len(lista_datos)-1:
            _swap(lista_datos,x)
            dato=lista_datos[x]
        _modificar(dato)(base_datos,titulo)

def _swap(lista,posicion):
    lista[posicion],lista[len(lista)-1]=lista[len(lista)-1],lista[posicion]

def _modificar_titulo(base_datos,titulo):
    titulo_nuevo=obtener_operacion(TITULO_NUEVO)
    lista_titulo_viejo=base_datos[titulo]
    base_datos.pop(titulo)
    base_datos[titulo_nuevo]=lista_titulo_viejo

def _modificar_autor(base_datos,titulo):
    autor_nuevo=obtener_operacion(AUTOR_PEDIDO)
    lista_titulo=base_datos[titulo]
    lista_titulo[0]=autor_nuevo
    base_datos[titulo]=lista_titulo

def _modificar_paginas(base_datos,titulo):
    paginas_nuevas=obtener_numero(PAGINAS_NUEVAS)
    lista_titulo=base_datos[titulo]
    lista_titulo[1]=paginas_nuevas
    base_datos[titulo]=lista_titulo

def _modificar_isbn(base_datos,titulo):
    isbn_nuevo=obtener_numero(ISBN_NUEVO)
    lista_titulo=base_datos[titulo]
    lista_titulo[2]=isbn_nuevo
    base_datos[titulo]=lista_titulo

def _modificar_anio_edicion(base_datos,titulo):
    año_nuevo=obtener_numero(AÑO_NUEVO)
    lista_titulo=base_datos[titulo]
    lista_titulo[3]=año_nuevo
    base_datos[titulo]=lista_titulo

def _modificar_editorial(base_datos,titulo):
    editorial_nueva=obtener_operacion(EDITORIAL_NUEVA)
    lista_titulo=base_datos[titulo]
    lista_titulo[4]=editorial_nueva
    base_datos[titulo]=lista_titulo

def _modificar_genero(base_datos,titulo):
    genero_nuevo=obtener_operacion(GENERO_NUEVO)
    lista_titulo=base_datos[titulo]
    lista_titulo[5]=genero_nuevo
    base_datos[titulo]=lista_titulo

def _no_esta(titulo,base_datos):
    return titulo not in base_datos

def _modificar(dato):
    funciones={ TITULO:_modificar_titulo,
                AUTOR:_modificar_autor,
                PAGINAS:_modificar_paginas,
                ISBN:_modificar_isbn,
                AÑO_EDICION:_modificar_anio_edicion,
                EDITORIAL:_modificar_editorial,
                GENERO:_modificar_genero
                }
    try:
        return funciones[dato]
    except KeyError:
        print(OPERACION_INVALIDA)
