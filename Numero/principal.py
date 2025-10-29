# principal.py
from modelo_numero import Numero
from vista import Vista_formulario
from controlador import Controlador

# zona principal del código
if __name__ == "__main__":
    # paso 1: crear objetos de cada capa
    obj_modelo = Numero()
    obj_vista = Vista_formulario()
    obj_controlador = Controlador(obj_vista, obj_modelo)

    # paso 2: ejecutar el flujo MVC
    obj_controlador.ejecutar_programa()
