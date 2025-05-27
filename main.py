from fastapi import FastAPI, UploadFile, File
import geopandas as gpd
from io import BytesIO

app = FastAPI()

@app.post("/procesar-gpkg")
async def procesar_gpkg(file: UploadFile = File(...)):
    try:
        contents = await file.read()
        file_like = BytesIO(contents)
        gdf = gpd.read_file(file_like)
        return {
            "columnas": list(gdf.columns),
            "filas": len(gdf),
            "preview": gdf.head().to_dict(orient="records")
        }
    except Exception as e:
        return {"error": str(e)}