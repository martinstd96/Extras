from constantes import *
from funciones import *

def listar_autores(base_datos):
    if esta_vacia(base_datos):
        print(BASE_DE_DATOS_VACIA)
        return
    for titulo in base_datos:
        lista_titulo=base_datos[titulo]
        print(lista_titulo[0])

def listar_libros(base_datos):
    if esta_vacia(base_datos):
        print(BASE_DE_DATOS_VACIA)
        return
    for titulo in base_datos:
        lista_titulo=base_datos[titulo]
        _imprimir_informacion(titulo,lista_titulo)

def listar_libros_genero(base_datos):
    if esta_vacia(base_datos):
        print(BASE_DE_DATOS_VACIA)
        return
    genero=obtener_operacion(GENERO_LISTADO)
    for titulo in base_datos:
        lista_titulo=base_datos[titulo]
        if genero in lista_titulo:
            _imprimir_informacion(titulo,lista_titulo)

def listar_libros_autor(base_datos):
    if esta_vacia(base_datos):
        print(BASE_DE_DATOS_VACIA)
        return
    autor=obtener_operacion(AUTOR_LISTADO)
    for titulo in base_datos:
        lista_titulo=base_datos[titulo]
        if autor in lista_titulo:
            _imprimir_informacion(titulo,lista_titulo)

def listar_libros_editorial(base_datos):
    if esta_vacia(base_datos):
        print(BASE_DE_DATOS_VACIA)
        return
    editorial=obtener_operacion(EDITORIAL_LISTADO)
    for titulo in base_datos:
        lista_titulo=base_datos[titulo]
        if editorial in lista_titulo:
            _imprimir_informacion(titulo,lista_titulo)

def listar_libros_editorial_edicion(base_datos):
    if esta_vacia(base_datos):
        print(BASE_DE_DATOS_VACIA)
        return
    editorial=obtener_operacion(EDITORIAL_LISTADO)
    print(AVISO)
    rango_anios_edicion=obtener_operacion(RANGO_AÑOS_LISTADO)
    anio_1=obtener_numero(RANGO_AÑOS_1_LISTADO)
    anio_2=obtener_numero(RANGO_AÑOS_2_LISTADO)
    for titulo in base_datos:
        lista_titulo=base_datos[titulo]
        if editorial in lista_titulo and anio_1<=lista_titulo[3]<=anio_2:
            _imprimir_informacion(titulo,lista_titulo)

def listar_editorial_autor(base_datos):
    if esta_vacia(base_datos):
        print(BASE_DE_DATOS_VACIA)
        return
    editorial=obtener_operacion(EDITORIAL_LISTADO)
    for titulo in base_datos:
        lista_titulo=base_datos[titulo]
        if editorial in lista_titulo:
            print(lista_titulo[0])

def listar_libros_anio(base_datos):
    if esta_vacia(base_datos):
        print(BASE_DE_DATOS_VACIA)
        return
    anio=obtener_numero(AÑO_LISTADO)
    for titulo in base_datos:
        lista_titulo=base_datos[titulo]
        if anio in lista_titulo:
            _imprimir_informacion(titulo,lista_titulo)

def listar_libros_palabra(base_datos):
    if esta_vacia(base_datos):
        print(BASE_DE_DATOS_VACIA)
        return
    palabra=obtener_operacion(PALABRA_LISTADO)
    for titulo in base_datos:
        lista_titulo=base_datos[titulo]
        if palabra in titulo:
            _imprimir_informacion(titulo,lista_titulo)

def listar_libros_autor_letra(base_datos):
    if esta_vacia(base_datos):
        print(BASE_DE_DATOS_VACIA)
        return
    letra=obtener_operacion(LETRA_LISTADO)
    for titulo in base_datos:
        lista_titulo=base_datos[titulo]
        autor=lista_titulo[0]
        lista_autor=autor.split()
        apellido=lista_autor[len(lista_autor)-1]
        if letra.upper()==apellido[0]:
            _imprimir_informacion(titulo,lista_titulo)

def _imprimir_informacion(titulo,lista_datos):
    print("Titulo: {}, Autor: {}, Cantidad de paginas: {}, Numero ISBN: {}, Año: {}, Editorial: {}, Genero: {}".format(titulo,lista_datos[0],lista_datos[1],lista_datos[2],lista_datos[3],lista_datos[4],lista_datos[5]))
