# Sports Tracker API

API para procesar y analizar entrenamientos deportivos a partir de archivos CSV.

## Estructura del proyecto

- `app/main.py`: Punto de entrada de la aplicación FastAPI.
- `app/api/routes.py`: Endpoints de la API.
- `app/services/workouts.py`: Lógica de procesamiento de entrenamientos.
- `tests/`: Pruebas unitarias.
- `workouts.csv`: Archivo de ejemplo.

## Ejecución

```bash
uvicorn app.main:app --reload
```

## Pruebas

```bash
pytest
```
