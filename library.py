from book import Book

class Library:
   def __init__(self):
      self.books={}

   def add_book(self, book):
      if book.book_id not in self.books:
         self.books[book.book_id] = book
      else:
         raise Exception("Book already present")
      
   def remove_book(self, book_id):
      if book_id in books:
         del books[book_id]
      else:
         raise Exception("Book doesn't exist")
      
      