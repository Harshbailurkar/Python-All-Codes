# library management system

class library:
    def __init__(self) :
         self.no_of_books=0
         self.books=[]
    
    def addbook(self,book=str):
        self.books.append(book)
        self.no_of_books= len(self.books)
    
    def showinfo(self):
        print(f"the library has {self.no_of_books} books")

        
l1=library()
l1.addbook("harrypooter")
l1.addbook("haooter")
l1.addbook("harryer")
l1.addbook("haooter")
l1.addbook("hoter")

l1.showinfo()