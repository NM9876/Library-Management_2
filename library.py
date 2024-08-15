from book import Book
from user import User

class Library:
    def __init__(self):
        self.books={}
        self.users={}

    def add_book(self, book):
        if book.book_id not in self.books:
            self.books[book.book_id]= book
        else:
            raise Exception("This book already exists")
   
    def remove_book(self, book_id):
        if book_id in self.books:
            del books[book_id]
        else:
            raise Exception("Book doesn't exist")
     
    def register_user(self, user):
        if user.user_id not in self.users:
            self.users[user.user_id]= user
        else:
            raise Exception("User already exists")
    def unregister_user(self, user_id):
        if user_id not in self.users:
            del self.users[user_id]
        else:
            raise Exception("User unregistered")
    def borrow_book(self, user_id, book_id):
        if user_id in self.users and book_id in self.books:
           user = self.users[user_id]
           book = self.books[book_id]
           user.borrow_book(book)
        else:
           raise Exception("User or book doesn't exists")
      
    def list_books(self):
        return '\n'.join([str(book) for book in self.books.values()])
    
    def list_users(self):
        return '\n'.join([str(user) for user in self.users.values() ])        
        