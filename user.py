class User: 
    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name
        self.borrowed_books = []
    
    def borrow_book(self, book):
        if book.available:
           book.check_out()
           self.borrowed_books.append(book)
        else:
           raise Exception("Book is not available")
        
    def return_book(self, book):
        if book in self.borrowed_books:
            book.return_book()
            self.borrowed_books.remove(book)
        else:
            raise Exception("This book was not borrowed by the user")