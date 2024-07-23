from flask import jsonify, Blueprint
# Vamos a usar la mock
from mocks.empleado_mock import empleados
# Estoy importando las funciones de mi controlador
from controllers.empleado_controller import mostrarTodosMisEmpleados, mostrarCasados


empleado_routes = Blueprint('empleado_routes', __name__)

@empleado_routes.route('/hombre_casado', methods=['GET'])
def mostrar_hombre_casado():

    hombres_cas = mostrarCasados()
    # Hasta antes del jsonify
    return jsonify(
            {"msg": hombres_cas}
        )


@empleado_routes.route('/empleados', methods=['GET'])
def mostrar_empleados():
    todosLosEmpleados = mostrarTodosMisEmpleados()
    return jsonify({
        "msg": todosLosEmpleados
    })
