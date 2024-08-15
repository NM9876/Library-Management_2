class Book:
    def __init__(self, book_id, title, auther, available=True):
        self.book_id = book_id
        self.title = title
        self.auther = auther
        self.available= available
      
    def __str__(self):
        status = "available" if self.available else "not available"
        return f"ID: {self.book_id}, title: {self.title}, auther: {self.auther}, status: {status}"
    
    def check_out(self)
        if self.available:
            self.available = False
        else:
            raise Exception("Already checked out")
        
    def return_book(self):
        if not self.available:
            self.available = True 
        else:
            raise Exception("Already available")
        
        
        
    
