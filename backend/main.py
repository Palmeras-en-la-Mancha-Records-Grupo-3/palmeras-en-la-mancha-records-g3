from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from config.config import APP_DESCRIPTION, APP_TITLE, APP_VERSION
from database.database import Base, engine


from model import (  
    model_album,
    model_album_format,
    model_artist,
    model_branch,
    model_format,
    model_genre,
    model_record_label,
)


from routes import (
    route_album,
    route_artist,
    route_branch,
    route_format,
    route_genre,
    route_record_label,
)


# Crear tablas
Base.metadata.create_all(bind=engine)


# FAST API
app = FastAPI(
    title=APP_TITLE,
    version=APP_VERSION,
    description=APP_DESCRIPTION,
)


# CORS 
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Manejo de errores 
@app.exception_handler(ValueError)
async def value_error_handler(request: Request, exc: ValueError):
   
    return JSONResponse(status_code=400, content={"detail": str(exc)})


@app.exception_handler(Exception)
async def general_error_handler(request: Request, exc: Exception):
   
    return JSONResponse(status_code=500, content={"detail": "Error interno del servidor"})


# Rutas
app.include_router(route_album.router)
app.include_router(route_artist.router)
app.include_router(route_branch.router)
app.include_router(route_format.router)
app.include_router(route_genre.router)
app.include_router(route_record_label.router)


@app.get("/")
def root():
    return {"message": f"{APP_TITLE} funcionando"}