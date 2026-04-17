class Library:
    def __init__(self,name):
        self.name=name
        # Store all books titles in a list
        self.books=[] 
    
    def add_book(self,book):
        self.books.append(book)
        print(f"{book}' has been added to {self.name} Library")

    def remove_book(self,book):
        if book in self.books:
           self.books.remove(book)
           print(f"{book}' has been removed from the library")
        else:
            print(f"{book} not found in the library")

    def display_books(self):
        if self.books:
            print(f"\nBooks in {self.name} Library")
            for idx,book in enumerate(self.books, start=1):
              print(f"{idx}.{book}")
        else:
            print("No books in the library right now")

    def search_book(self,book):
        if book in self.books:
            print(f"{book} is available in the library")
        else:
            print(f"{book} is not availalbe ")                               

        
# Example usage
my_library=Library("City Centeral")

my_library.add_book("Python Programming")
my_library.add_book("Data Structure in C")
my_library.add_book("Introduction to Algorithms")

my_library.display_books()
my_library.search_book("Python Programming")

my_library.remove_book("Data Structure in C")

my_library.display_books()