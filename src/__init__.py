from fastapi import FastAPI
from src.books.router import router as books_router
from contextlib import asynccontextmanager
from src.db.main import init_db
from fastapi.middleware.cors import CORSMiddleware

@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Lifespan: starting up")
    init_db()
    yield
    print("Lifespan: shutting down")

version = "v1"

app = FastAPI(
    title = "Books API",
    description = "Books API with FastAPI", 
    version=version,
    lifespan=lifespan
)
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

app.include_router(books_router, prefix=f"/api/{version}/books", tags=["books"])
