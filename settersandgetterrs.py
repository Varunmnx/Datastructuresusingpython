class Book:
    def __init__(self, title, quantity, author, price):
        self.title = title
        self.quantity = quantity
        self.author = author
        self.__price = price
        self.__discount = None

    def set_discount(self, discount):
        self.__discount = discount

    def get_price(self):
        if self.__discount:
            return self.__price * (1-self.__discount)
        return self.__price

    def __repr__(self):
        return f"Book: {self.title}, Quantity: {self.quantity}, Author: {self.author}, Price: {self.get_price()}"


single_book = Book('Two States', 1, 'Chetan Bhagat', 200)

bulk_books = Book('Two States', 25, 'Chetan Bhagat', 200)
bulk_books.set_discount(0.20)

print(single_book.get_price())
print(bulk_books.get_price())
print(single_book)
print(bulk_books)

# class balls:
#     def __init__(self,name,price,available,company):
#         self.name=name
#         self.__price =price
#         self.availability=available
#         self.company=company
#         self.__discount = None
#
#     def set_discount(self,discount):
#         self.__discount =discount
#     def get_value(self):
#         if self.__discount:
#             return self.__price*(1-self.__discount)
#         return self.__price
#
#     def __repr__(self):
#         return f"{self.name}::{self.company}::{self.availability}::{self.get_value()}"
#
# if __name__=="__main__":
#     cricket = balls("cricketball",100,"none","viso")
#     football = balls("football",200,"none","adidas")
#     cricket.set_discount(.20)
#     print(cricket)
#     print(football)
