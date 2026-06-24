# SO new file for OOPS previous one is now become too messy
print("--------------------------dir, __dict__, help Methods------------------------")

class Game():
    def __init__(self, name, price):
        self._name = name
        self._price = price

    @property
    def showInfo(self):
        print(f"The Game name is {self._name} and its price is {self._price} INR")

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if(value < 0):
            raise ValueError ("Invalid Price")
        self._price = value

try:
    in_name = input("Add Your Game Here : ")
    in_price = float(input("Set your Price : "))

    g1 = Game(in_name, in_price)
    g1.showInfo
except ValueError as e:
    print(f"\nERROR : {e}")


# print(dir(in_name)) # It shows all methods of that data type like this is a String its output is this ['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
# we can also see that methods like this 
# print(in_name.__add__) # and so on methods of String like len, strip , join so if you forget methods you can see it like that--


# print(g1.__dict__) # this method shows all data inside of our class object like sometimes the class is very big and we want to see data inside it we can use it output : {'_name': 'haas', '_price': 232.0} this makes a internal DIctionary 

# print(help(Game)) # this is use to see info and takes help output : 
# #Help on class Game in module __main__:                                                                                                                         

# class Game(builtins.object)
#  |  Game(name, price)
#  |
#  |  Methods defined here:
#  |
#  |  __init__(self, name, price)
#  |      Initialize self.  See help(type(self)) for accurate signature.
#  |
#  |  ----------------------------------------------------------------------
#  |  Readonly properties defined here:
#  |
#  |  showInfo
#  |
#  |  ----------------------------------------------------------------------
#  |  Data descriptors defined here:
#  |
#  |  __dict__
#  |      dictionary for instance variables
#  |
#  |  __weakref__
#  |      list of weak references to the object
#  |
# -- More  -- 


print("----------------------------- Super Keyword -----------------------------------------------")

# So basically when i inherit one class into another then i need to call its method so i use super keyword to call the parent class methods

class GameReviews(Game):
    def __init__(self, name, price, Ratings):
        super().__init__(name, price)
        self.Ratings = Ratings

    @property
    def info(self):
        return (f"Name of the Game is {self._name} price is {self._price} and Rating is {self.Ratings}")
    
g2 = GameReviews(in_name, in_price, 5.0)
print(g2.info)
    

print()

print("------------------------------------------Method OverRiding--------------------------------------------")
# so basically when we inherit a class and wants to manipulate its method we can use Method OverRiding for ex. 

class shape():
    def __init__(self, val1, val2):
        self.val1 = val1
        self.val2 = val2

    
    def area (self):
        return self.val1 * self.val2
    
a = shape(2, 4)
print(a.area())

class CircleArea(shape):

    def __init__(self, radius):
        self.radius = radius
        super().__init__(radius, radius)
    def Area(self):
        return 3.14 * super().area() 
    #Class method overrids first area is found using x*y now for different case we use that parentMethod a/c to condition now super.area() is multiply x and y so that parameter is our radius it do radius * radius then we multiply that answer with 3.14 and got out answer --
    
    
c = CircleArea(4)
print(c.Area())



















































































