from fastapi.staticfiles import StaticFiles
from fastapi import FastAPI
from .cdn import images,js,css,font
from .router import template,post,user,vote
from . import models
from .database import engine



app = FastAPI(version=1.03, title="Nah my blog post, Be this")

# app.add_middleware(
#     CORSMiddleware,
#     allow_origin=["*"],
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"]
# )

app.mount("/statics", StaticFiles(directory="statics"), name="statics")

@app.on_event("startup")
def on_start():
    models.Base.metadata.create_all(bind=engine)

# @app.on_event("startup")
# def on_startup():
#     create_db_and_tables()

app.include_router(vote.router)
app.include_router(user.router)
app.include_router(post.router)
app.include_router(images.router)
app.include_router(js.router)
app.include_router(css.router)
app.include_router(font.router)
app.include_router(template.router)

