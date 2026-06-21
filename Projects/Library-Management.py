class Library():
    def __init__(self):
        self.books = []
        self.total_books = 0
    def func(self):
        new_li = str(input("Enter the book name -- "))
        # new_li2 = list(new_li)
        self.books.append(new_li)
        self.total_books += 1

    def printing(self):
        for i in self.books:
            print(i)
    
    def count(self):
        print(self.total_books)
       

a = Library()
while True:
    user_start = input('type start or quit : ')
    user_start = user_start.strip().lower()
    if(user_start == "start"):
     try:
      a.func()
      a.printing()
      a.count()
     except ValueError as e:
        print(f"\nERROR {e}")
    elif(user_start == "quit" or user_start == "exit"):
       print("EXITING !! ")
       break
    else:
       print("Invalid Input try again __ ")
       continue
    

# Making this using Getters and Setters

class Lib:
    def __init__(self):
        # Initialize hidden variables using the single underscore convention
        self._books = []
        self._total = 0

    @property
    def books(self):
        """Getter for books: Formats and displays the book collection."""
        if not self._books:
            print("The library is currently empty.")
        else:
            print("\n--- Library Books ---")
            for index, book in enumerate(self._books, start=1):
                print(f"{index}. {book}")
        return self._books

    @books.setter
    def books(self, value):
        """Setter for books: Appends the book name and updates the counter."""
        self._books.append(value)
        self._total += 1  # Updates the count automatically behind the scenes

    @property
    def total(self):
        """Getter for total: Read-only property to view the book count."""
        print(f"Total books in library: {self._total}")
        return self._total


# --- MAIN PROGRAM LOOP ---
# Create the library object ONCE outside the loop so it persists
my_library = Lib()

while True:
  
    user_start = input("Type 'add', 'show', 'count', or 'quit': ").strip().lower()
    

    if user_start == "add":
        # Ask for the book name OUTSIDE the class
        book_name = input("Enter BOOK name ==> ").strip()
        
        if book_name:
            # Drop the book name into the magic mailbox slot (the setter)
            my_library.books = book_name
            print(f"Success: '{book_name}' added to the library!")
        else:
            print("Book name cannot be empty.")

    elif user_start == "show":
        # Triggers the books getter property to loop and display
        my_library.books

    elif user_start == "count":
        # Triggers the total getter property to display the count
        my_library.total

    elif user_start in ["quit", "exit"]:
        print("EXITING !! ")
        break

    else:
        print("Invalid Input, try again _ ")
   




































