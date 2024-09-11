from fastapi import APIRouter, status, Depends
from fastapi.exceptions import HTTPException
from sqlmodel.ext.asyncio.session import AsyncSession
from src.books.service import BookService
from src.books.schema import Book, BookUpdateModel
from src.db.main import get_session
from typing import List



router = APIRouter()
book_service = BookService()

@router.get("/", response_model=List[Book])
async def get_books(session: AsyncSession = Depends(get_session)):
    """
    Get all books

    Returns:
        List[Book]: A list of all books
    """
    books = await book_service.get_all_books(session)
    return books

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=Book)
async def create_book(book_data: Book, session: AsyncSession = Depends(get_session)) -> dict:
    """
    Create a new book

    Args:
        book_data (Book): The book to be created

    Returns:
        Book: The created book
    """
    new_book = await book_service.create_book(book_data, session)
    return new_book

@router.get("/{book_id}")
async def  get_book(book_id: int):
    for book in books:
        if book["id"] == book_id:
            return book
    
    raise HTTPException(status_code=404, detail="Book not found")

@router.patch("/{book_id}")
async def  update_book(book_id: int, book_data: BookUpdateModel) -> dict:
    for book in books:
        if book["id"] == book_id:
            book["title"] = book_data.title
            book["author"] = book_data.author
            book["publisher"] = book_data.publisher
            book["page_count"] = book_data.page_count
            book["language"] = book_data.language
            return book

    raise HTTPException(status_code=404, detail="Book not found")

@router.delete("/{book_id}")
async def  delete_book(book_id: int, status_code=status.HTTP_204_NO_CONTENT):
    for book in books:
        if book["id"] == book_id:
            books.remove(book)
            return {"message" : "Book deleted"}
    raise HTTPException(status_code=404, detail="Book not found")
