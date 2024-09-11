from sqlmodel.ext.asyncio.session import AsyncSession
from .schema import BookCreateModel, BookUpdateModel
from .model  import Book
from sqlmodel import select, desc

class BookService:
    async def get_all_books(self, session: AsyncSession):
        statements = select(Book).order_by(desc(Book.created_at))
        result = await session.exec(statements)
        
        return result.all()
    
    
    async def get_book(self, book_uid, session: AsyncSession):
        
        statements = select(Book).where(Book.uid == book_uid)
        result = await session.exec(statements)
        
        book = result.first()
        return book if book is not None else None
    
    
    async def create_book(self, book_data: BookCreateModel, session: AsyncSession):
        
        book_date_dict = book_data.model_dump()
        
        new_book = Book(**book_date_dict)
        session.add(new_book)
        
        await session.commit()
        return new_book
    
    
    async def update_book(self, book_uid, book_data: BookUpdateModel, session: AsyncSession):
        
        book_to_update =  self.get_book(book_uid, session)
        update_book_dict = book_data.model_dump()
        if book_to_update is None:
            for key, value in update_book_dict.items():
                setattr(book_to_update, key, value)
        
            await session.commit()
            return book_to_update
        else:
            return None
    async def delete_book(self, book_uid, session: AsyncSession):
        
        book_to_delete =  self.get_book(book_uid, session)
        
        if book_to_delete is not None:
            await session.delete(book_to_delete)
            await session.commit()
            # return book_to_delete
        else:
            return None
        
    