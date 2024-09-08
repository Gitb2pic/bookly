from fastapi import FastAPI
from src.books.router import router as books_router
from fastapi.middleware.cors import CORSMiddleware

version = "v1"

app = FastAPI(
    title = "Books API",
    description = "Books API with FastAPI", 
    version=version,
)
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

app.include_router(books_router, prefix=f"/api/{version}/books", tags=["books"])
