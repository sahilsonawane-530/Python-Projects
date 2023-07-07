class Library:
    def __init__(self):
        self.no_of_books = 0
        self.books = []
    
    def addBook(self, book):
        self.books.append(book)
        self.no_of_books = len(self.books)
    
    def showDetails(self):
        print(f"\nThe library has {self.no_of_books - 1} books\n")
        for i in self.books:
            if (i == "q"):
                break
            print(i)

l1 = Library()

books = None
while (books != "q"):
    books = input("Enter books or press 'q' for quit : ")
    l1.addBook(books)

l1.showDetails()