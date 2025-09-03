# book_class
class book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def __del__(self):
        print(f"Deleting {self.title}")
              
    def __str__(self):
        return f"{self.title} by {self.author} was published in {self.year}"

    def __rep__(self):
        return f"Book('{self.title}','{self.author}', {self.year})"
    
    
