# Flask Ejemplo de Backend

Este proyecto es una aplicación básica en Flask para practicar la logica

## Estructura del Proyecto

- **`app.py`**: Punto de entrada de la aplicación.
- **`controllers/empleado_controller.py`**: Lógica de filtrado de empleados.
- **`routes/empleado_routes.py`**: Definición de rutas y endpoints.
- **`mocks/empleado_mock.py`**: Datos mockeados de empleados.

## Requisitos

- Python 3.8 o superior

## Instalación

1. **Crea un entorno virtual**:
    ```bash
    python -m venv venv
    ```

2. **Activa el entorno virtual**:
    - En Windows:
        ```bash
        venv\Scripts\activate
        ```
    - En gitbash:
        ```
        source venv/Scripts/activate
        ```
    - En macOS y Linux:
        ```bash
        source venv/bin/activate
        ```

3. **Instala las dependencias**:
    ```bash
    pip install Flask
    ```

## Ejecución

1. **Inicia la aplicación Flask**:
    ```bash
    python app.py
    ```

2. **Accede al endpoint**:
    - Abre tu navegador o usa una herramienta como Postman para probar el endpoint:
      ```
      http://127.0.0.1:5000/api/v1/empleados
      ```

## Notas

- Asegúrate de estar en el entorno virtual al ejecutar la aplicación.
- Los datos están mockeados en `mocks/empleado_mock.py` y pueden ser modificados para pruebas adicionales.

## Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo [LICENSE](LICENSE) para más detalles.
