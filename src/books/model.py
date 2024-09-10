from sqlmodel import SQLModel, Field, Column
import sqlalchemy.dialects.postgresql as pg
from datetime import datetime
import uuid


class Book(SQLModel, table=True):
    __tablename__ = "books"
    uid : uuid.UUID = Field(
        sa_column=Column(
            pg.UUID,
            primary_key=True,
            #unique=True,
            nullable=False,
            default=uuid.uuid4
        )
    )
    
    title : str
    author : str
    publisher :  str
    published_date : str
    page_count : int
    language : str
    created_at : datetime = Field(
        Column(
            pg.TIMESTAMP,
            default=datetime.now
        )
    )
    updated_at : datetime = Field(
        Column(
            pg.TIMESTAMP,
            default=datetime.now
        )
    )
    
    def __repr__(self):
        return f"Book({self.uid}, {self.title}, {self.author}, {self.publisher}, {self.published_date}, {self.page_count}, {self.language}, {self.created_at}, {self.updated_at})"
    
