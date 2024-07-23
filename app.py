from flask import Flask
from routes.empleado_routes import empleado_routes

app = Flask(__name__)

# Registrar las rutas
app.register_blueprint(empleado_routes, url_prefix='/api/v1')

if __name__ == '__main__':
    app.run(debug=True)
