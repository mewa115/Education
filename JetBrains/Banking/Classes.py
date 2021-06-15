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


class Movie:
    # create class here
    all_movies = []
    def __init__(self, title, director, year):
        self.title = title
        self.director = director
        self.year = year
        # Movie.all_movies.append(self)


# objects of the class Movie
titanic = Movie('"Titanic"', '(James Cameron,', '1997)')
star_wars = Movie('"Star Wars"', '(George Lucas,', '1977)')
fight_club = Movie('"Fight Club"', '(David Fincher,', '1999)')


class RightTriangle:
    def __init__(self, hyp, leg_1, leg_2):
        self.c = hyp
        self.a = leg_1
        self.b = leg_2
        # calculate the area here
        s = 1 / 2 * (self.a * self.b)
        print(s)


# triangle from the input
input_c, input_a, input_b = [int(x) for x in input().split()]
# print(input_c, input_b, input_a)
# write your code here
if input_a**2 + input_b**2 == input_c**2:
    triangle = RightTriangle(input_c, input_a, input_b)
    # print(RightTriangle)
else:
    print('Not right')



