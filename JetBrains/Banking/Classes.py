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


class Tree:
    trunk = True
    branches = True

    def __init__(self, name, height):
        self.name = name
        self.height = height


class River:
    # list of all rivers
    all_rivers = []

    def __init__(self, name, length):
        self.name = name
        self.length = length
        # add current river to the list of all rivers
        River.all_rivers.append(self)


volga = River("Volga", 3530)
seine = River("Seine", 776)
nile = River("Nile", 6852)

# print all river names
for river in River.all_rivers:
    print(river.name)


class Store:
    def __init__(self, name, category):
        self.name = name
        self.category = category


shop = Store("GAP", "clothes")
print(shop.name, shop.category)




