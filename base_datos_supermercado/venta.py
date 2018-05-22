import time
from constantes import *
from pedir import *
from agregar_eliminar import *

def realizar_venta(almacenamiento):
    factura=open(ARCHIVO_TICKET,"w")
    lista_precio_final=[0]
    lista_descuentos=[0]
    print(MENSAJE_FIN_VENTA)
    print()
    producto=pedir_operacion_dato_producto(MENSAJE_VENTA)
    while producto!="*":
        unidades=pedir_unidades(MENSAJE_UNIDADES)
        vender_producto_y_emitir_ticket(producto,unidades,almacenamiento,factura,lista_precio_final,lista_descuentos)
        producto=pedir_operacion_dato_producto(MENSAJE_VENTA)
    escribir_total(factura,lista_descuentos,lista_precio_final)

def vender_producto_y_emitir_ticket(producto,unidades,almacenamiento,factura,lista_precio_final,lista_descuentos):
    for codigo in almacenamiento:
        lista_producto=almacenamiento[codigo]
        if producto in lista_producto:
            if not hay_stock_venta(unidades,lista_producto[1]):
                print(MENSAJE_NO_STOCK)
                return
            if esta_vencido(producto,lista_producto[3]):
                print(MENSAJE_PRODUCTO_VENCIDO)
                eliminar_producto_(almacenamiento,codigo)
                return
            lista_producto[1]-=unidades
            escribir_factura(factura,unidades,lista_producto,codigo,lista_precio_final,lista_descuentos)
            reponer_stock(lista_producto)
            almacenamiento[codigo]=lista_producto
            return
    print(NO_EXISTE_PRODUCTO)
    return

def esta_vencido(producto,fecha):
    fecha_actual=time.strftime("%d/%m/%Y")
    lista_fecha_1=obtener_lista_fecha(fecha_actual)
    lista_fecha_2=obtener_lista_fecha(fecha)
    numero_dia_1=int(lista_fecha_1[0])
    numero_mes_1=int(lista_fecha_1[1])
    anio_1=int(lista_fecha_1[2])
    numero_dia_2=int(lista_fecha_2[0])
    numero_mes_2=int(lista_fecha_2[1])
    anio_2=int(lista_fecha_2[2])
    if anio_2<anio_1:
        return True
    if anio_2==anio_1 and numero_mes_2<numero_mes_1:
        return True
    if anio_2==anio_1 and numero_mes_2==numero_mes_1 and numero_dia_2<numero_dia_1:
        return True

def hay_stock_venta(unidades,cantidad_disponible):
    return cantidad_disponible>=unidades

def reponer_stock(lista_producto):
    if lista_producto[1]<10:
        lista_producto[1]+=60

def escribir_factura(factura,unidades,lista_producto,codigo,lista_precio_final,lista_descuentos):
    descripcion,stock,precio,fecha,tipo=lista_producto
    lista_precio=[precio]
    verificar_vencimiento_y_realizar_descuento(fecha,lista_precio,unidades,lista_descuentos)
    precio_total=lista_precio[0]*unidades
    lista_precio_final[0]+=precio_total
    factura.write("{}  {}  {}  {}\n".format(unidades,descripcion,codigo,precio_total))

def verificar_vencimiento_y_realizar_descuento(fecha,lista_precio,unidades,lista_descuentos):
    fecha_actual=time.strftime("%d/%m/%Y")
    lista_fecha_1=obtener_lista_fecha(fecha_actual)
    lista_fecha_2=obtener_lista_fecha(fecha)
    numero_dia_1=int(lista_fecha_1[0])
    numero_mes_1=int(lista_fecha_1[1])
    anio_1=int(lista_fecha_1[2])
    numero_dia_2=int(lista_fecha_2[0])
    numero_mes_2=int(lista_fecha_2[1])
    anio_2=int(lista_fecha_2[2])
    diferencia_dias=numero_dia_2-numero_dia_1
    diferencia_mes=numero_mes_2-numero_mes_1
    diferencia_anios=anio_2-anio_1
    if numero_mes_2==numero_mes_1 and diferencia_dias<=7:
        realizar_descuento(lista_precio,unidades,lista_descuentos)
    elif diferencia_mes==1 and 31+diferencia_dias<=7:
        realizar_descuento(lista_precio,unidades,lista_descuentos)
    elif diferencia_anios==1 and 12+diferencia_mes==1 and 31+diferencia_dias<=7:
        realizar_descuento(lista_precio,unidades,lista_descuentos)

def realizar_descuento(lista_precio,unidades,lista_descuentos):
    descuento=lista_precio[0]*0.1
    lista_descuentos[0]+=descuento*unidades
    lista_precio[0]-=descuento

def escribir_total(factura,lista_descuentos,lista_precio_final):
    factura.write("\n")
    factura.write("DESCUENTO            {}\n".format(lista_descuentos[0]))
    factura.write("\n")
    factura.write("TOTAL                {}\n".format(lista_precio_final[0]))
    factura.close()

def obtener_lista_fecha(fecha):
    return fecha.split("/")
