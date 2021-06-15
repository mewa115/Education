class Book:
    material = "paper"
    cover = "paperback"
    all_books = []


my_book = Book()
print(my_book.material)  # "paper"
print(my_book.cover)  # "paperback"
print(my_book.all_books)  # []

print(Book.material)


class Angel:
    color = "white"
    feature = "wings"
    home = "Heaven"


class Demon:
    color = "red"
    feature = "horns"
    home = "Hell"


print(Angel.color, Demon.color)
print(Angel.feature, Demon.feature)
print(Angel.home, Demon.home)