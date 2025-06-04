from sqlalchemy import create_engine,Column,Integer,String,ForeignKey,Table
from sqlalchemy.orm import declarative_base,relationship,sessionmaker

Base=declarative_base

#Assaciation table 
author_book= Table(
    'author_book',Base.metadata,
    Column('author_id',ForeignKey('authors.id') ,primary_key=True),
    Column('book_id', ForeignKey('book.id') ,primary_key=True)
)

class Authors(Base):
    __tablename__='authors'
    id =Column(Integer,primary_key=True)
    name=Column(String)

class Books(Base):
    __tablename__='books'
    id= Column(Integer,primary_key='True')
    title=Column(String)

#Here i am setting the data base
engine=create_engine
Base.metadata.create_all(engine)
Session=sessionmaker(bind=engine)
session=Session()

with Session(engine) as session:
    #Created the authors
    author1=Authors(name='Yazz')
    author2=Authors(name='Is Very')
    author3=Authors(name='Calm')

    #Creating books
    book1=Books(title="Harry Potter and the Philosopher's Stone")
    book2=Books(title="Good Omens")
    book3=Books(title="The Shining")

    # Associate them
    author1.books.append(book1)     # J.K. Rowling wrote Harry Potter
    author2.books.append(book2)     # Stephen King wrote The Shining
    author1.books.append(book3)     # Both wrote Co-Written Fantasy
    author2.books.append(book3)

    session.add_all(author1,author2,author3,book1,book2,book3)
    session.commit()


