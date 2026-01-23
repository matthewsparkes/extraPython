# Magic methods = Dunder methods (double underscore) __init__, __str__, __eq__
#                 They are automatically called by many of Python's built-in operations.
#                 They allow devleopers to define or customize the behaviour of objects

class Book:

    def __init__(self, title, author, num_pages):
        self.title = title
        self.author = author
        self.num_pages = num_pages

    def __str__ (self):
        return f"'{self.title}' by {self.author}"
    
    def __eq__(self, other):            # other for the other book we will be comparing it too
        return self.title == other.title and self.author == other.author
    
    def __lt__(self, other):
        return self.num_pages < other.num_pages
    
    def __gt__(self, other):
        return self.num_pages > other.num_pages
    
    def __add__(self, other):
        return self.num_pages + other.num_pages
    
    def __contains__(self, keyword):
        return keyword in self.title or keyword in self.author
    
    def __getitem__(self, key):
        if key == "title":
            return self.title
        elif key == "author":
            return self.author
        elif key == "num_pages":
            return self.num_pages
        else:
            return f"Key '{key}' not found."

book1 = Book("The Hobbit", "J.R.R. Tolkien", 310)
book2 = Book("Harry Potter", "J.K. Rowling", 223)
book3 = Book("The Lion, the Witch and the Wardrobe", "C.S Lewis", 172)

print(book1) # dunder string lets us return a string representaiotn of the object when we print directly to the console

print(book1 == book2) # now true using dunder eq to see that author name and book name are the same therefore true

print(book2 < book3) # __lt__ for less than
print(book2 > book3) # __gt__ for greater than

print(book2 + book3) # __add__

print("J.K. Rowling" in book2) # __contains__

print(book1['author'])