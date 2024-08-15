class User:

   def __init__(self, user_id, name):
      self.user_id = user_id
      self.name = name 
      self.borrowed_books=[]

   def __str__(self):
      return f"User ID: {self.user_id}, name: {self.name}"
   
   def borrow_book(self, book):
      if book.available:
         book.checkout()
         self.borrowed_books.append(book)
      else:
         raise Exception("Book not available.")
   def return_book(self, book):
      if book in self.borrowed_books:
         self.borrowed_books.remove(book)
      else:
         raise Exception("This book was not borrowed by the user")
         
      