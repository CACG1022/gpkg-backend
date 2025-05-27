from fastapi import FastAPI, UploadFile, File
import geopandas as gpd
import tempfile

app = FastAPI()

@app.post("/procesar-gpkg/")
async def procesar_gpkg(file: UploadFile = File(...)):
    try:
        contents = await file.read()

        # Crear archivo temporal
        with tempfile.NamedTemporaryFile(delete=False, suffix=".gpkg") as tmp:
            tmp.write(contents)
            tmp_path = tmp.name

        # Leer el archivo desde disco
        gdf = gpd.read_file(tmp_path)

        return {
            "columnas": list(gdf.columns),
            "filas": len(gdf),
            "preview": gdf.head().to_dict(orient="records")
        }

    except Exception as e:
        return {"error": str(e)}
