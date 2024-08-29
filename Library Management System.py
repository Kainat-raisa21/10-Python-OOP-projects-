class Library:

    def __init__(self, booklist):
        self.stock = booklist

    def display_stock_details(self):
        print("The books that are currently available in our stock: \n")
        for i in range(1, len(self.stock)+1):
            print(f"{i}. {self.stock[i-1]}")

    def lend_book(self, requested_book):
        if requested_book in self.stock:
            print(f"You have now borrowed the book {requested_book}")
            self.stock.remove(requested_book)
        else:
            print(f"Oops, {requested_book} is not in stock right now!")

    def add_book(self, returned_book):
        self.stock.append(returned_book)


class Customer:

    def __init__(self):
        self.name = None
        self.id = None
        self.books_borrowed = []
        self.no_books = 0
        self.books_returned = []

    def customer_details(self):
        print("Customer's name:",self.name)
        print("Customer ID:",self.id)
        print("No. of books borrowed:", self.no_books)
        print("Books have been borrowed:", self.books_borrowed)
        print("Books have been returned:", self.books_returned)

    def request_book(self):
        self.book = input("Which book you wanna borrow?: ")
        self.books_borrowed.append(self.book)
        return self.book

    def return_book(self):
        self.book = input("Enter the book name you want to return: ")
        self.books_returned.append(self.book)
        return self.book


if __name__ == "__main__":

    library = Library(["To Kill a Mockingbird", "1984","Pride and Prejudice", "The Great Gatsby", "The Catcher in the Rye", "The Lord of the Rings",
    "The Hobbit", "Brave New World", "The Chronicles of Narnia", "Moby-Dick", "War and Peace", "The Harry Potter series", "The Hunger Games",
    "The Da Vinci Code", "The Hitchhiker's Guide to the Galaxy", "The Shining", "The Alchemist", "The Road", "To the Lighthouse", "The Grapes of Wrath"])

    cus1 = Customer()
    cus1.name = "Kainat Raisa Hossain"
    cus1.id = "KRH21221"


    while True:
        answer = int(input("Hello reader, how can we help you?:(enter a number) \n"
                       "1.Display my deatils \n"
                       "2.I wanna borrow a book \n"
                       "3.I wanna return a book \n"
                       "4.I wanna see the stock details \n"
                           "enter : "))
        if answer == 1:
            cus1.customer_details()
        elif answer == 2:
            library.lend_book(cus1.request_book())
            cus1.no_books += 1
        elif answer == 3:
            library.add_book(cus1.return_book())
        elif answer == 4:
            print(library.display_stock_details())
        else:
            break



