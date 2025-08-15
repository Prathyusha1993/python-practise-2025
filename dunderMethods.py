from operator import getitem


# under methods: Dunder methods customize how objects behave with built-ins — e.g., __len__ for len(obj)

class Book:
    def __init__(self, title, pages):
        self.title = title
        self.pages = pages

    def __str__(self):
        return f'{self.title} ({self.pages} pages)'

    def __repr__(self):
        return f'book({self.title!r}, {self.pages})'

    def __len__(self):
        return self.pages

    def __getitem__(self, index):
        return self.title[index]

b = Book('Python 101', 300)
print(str(b))
print(repr(b))
print(len(b))
print(b[0])