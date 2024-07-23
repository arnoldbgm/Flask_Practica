from mocks.empleado_mock import empleados

# No importa el nombre de la funcion
def mostrarTodosMisEmpleados():
   return empleados

def mostrarCasados():
   hombres_casados = []
   for empl in empleados:
      if empl['estado_civil'] == 'casado':
         hombres_casados.append(empl)
   # Aqui debes de retornar una lista
   return hombres_casados