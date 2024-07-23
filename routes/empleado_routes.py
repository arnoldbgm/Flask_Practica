from flask import Blueprint, jsonify
from controllers.empleado_controller import todos_empleados

empleado_routes = Blueprint('empleado_routes', __name__)

@empleado_routes.route('/empleados', methods=['GET'])
def obtener_adultos_endpoint():
    empleados = todos_empleados()
    return jsonify({
        "nmroEmpleados": f"El numero de empleados es de {len(empleados)}",
        "empleados" : empleados
    })
