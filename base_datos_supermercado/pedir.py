def pedir_operacion_dato_producto(mensaje):
    operacion=input(mensaje)
    while len(operacion)==0:
        operacion=input(mensaje)
    return operacion

def pedir_unidades(mensaje):
    unidad=input(mensaje)
    while len(unidad)==0 or not unidad.isdigit():
        unidad=input(mensaje)
    return int(unidad)
