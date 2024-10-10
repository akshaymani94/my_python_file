# magic methods or dunder methods

# Example : __init__ , __str__ , __eq__
# They allow developers to define or customize the behavior of obejcts
# they are automatically called by many of pythons buit in operations

class Book:

    def __init__(self,title,author,num_pages):
        self.title = title
        self.author = author
        self.num_pages = num_pages

    def __str__(self):
        return f"'{self.title}' by {self.author}"
    
    def __eq__(self,other):
        return self.title == other.title and self.author == other.author

    def __lt__(self,other):
        return self.num_pages < other.num_pages
    
    def __gt__(self,other):
        return self.num_pages > other.num_pages
    
    def __add__(self,other):
        return f"{self.num_pages + other.num_pages} pages"
    
    def __contains__(self,keyword):
        return keyword in self.title or keyword in self.author
    
    def __getitem__(self,key):
        if key == 'title':
            return self.title
        elif key == 'author':
            return self.author
        elif key == 'num_pages':
            return self.num_pages
        else:
            return f"Key '{key}' not found"

    
book1 = Book("abc","ik",78)
book2 = Book("def","im",998)
book3 = Book("ghi","il",125)
book4 = Book("abc","ik",78)

print(book1)            # return as object if dunder string was not there

print(book1 == book4)   # dunder equal

print(book3 < book4)    # dunder less than

print(book3 > book4)    # dunder greater than

print(book1 + book2)    # dunder add

print("im" in book2)    # dunder contains
print("abc" in book2)

print(book1['title'])   # dunder get item
print(book2['author']) 
print(book4['num_pages']) 
print(book3['audio'])

