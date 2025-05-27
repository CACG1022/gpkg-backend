# gpkg-backend

API en FastAPI que recibe archivos GPKG, los procesa y devuelve un resumen útil.

## Cómo ejecutar

```bash
pip install -r requirements.txt
uvicorn main:app --reload
```

## Endpoint

- POST `/procesar-gpkg`
  - Formulario con archivo GPKG
  - Devuelve columnas, número de filas y primeras filas del archivo
