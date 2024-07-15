class Book:
    def __init__(self, title, author, pages) -> None:
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self) -> str:
        return f"{self.title} by {self.author} has {self.pages} pages"


    def __repr__(self) -> str:
        return f"The book {self.title} written by {self.author} has a total of {self.pages} pages"