from modelo_numero import Numero
from vista import Vista_formulario
from controlador import Controlador
#zona principal del codigo
# paso 5

obj_modelo = Numero()
obj_vista = Vista_formulario()
obj_controlador = Controlador(obj_vista, obj_modelo)
 
""" obj_numero = Numero() 
obj_numero.set_numero(5)  # paso 6
print(f"El numero ingresado es: {obj_numero.get_numero()}")  
# paso 7
mensaje = obj_numero.validar_par()
print(f"Resultado: {mensaje}")
"""
obj_formuario = Vista_formulario()
dato_numero = obj_formuario.hacer_campo()
print(dato_numero)