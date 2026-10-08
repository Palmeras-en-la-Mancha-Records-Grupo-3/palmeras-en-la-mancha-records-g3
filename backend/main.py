from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from .config.config import APP_DESCRIPTION, APP_TITLE, APP_VERSION
from .database.database import Base, engine


from .model import (  
    model_albums,
    model_album_formats,
    model_artists,
    model_branches,
    model_formats,
    model_genres,
    model_record_labels,
)


from .routes import (
    routes_albums,
    routes_artists,
    routes_branches,
    routes_formats,
    routes_genres,
    routes_record_labels,
)


Base.metadata.create_all(bind=engine)


app = FastAPI(
    title=APP_TITLE,
    version=APP_VERSION,
    description=APP_DESCRIPTION,
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.exception_handler(ValueError)
async def value_error_handler(request: Request, exc: ValueError):
   
    return JSONResponse(status_code=400, content={"detail": str(exc)})


@app.exception_handler(Exception)
async def general_error_handler(request: Request, exc: Exception):
   
    return JSONResponse(status_code=500, content={"detail": "Error interno del servidor"})


app.include_router(routes_albums.router)
app.include_router(routes_artists.router)
app.include_router(routes_branches.router)
app.include_router(routes_formats.router)
app.include_router(routes_genres.router)
app.include_router(routes_record_labels.router)


@app.get("/")
def root():
    return {"message": f"{APP_TITLE} en funcionamiento"}