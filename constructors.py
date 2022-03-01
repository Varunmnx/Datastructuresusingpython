# class Book:
#     def __init__(self, title, quantity, author, price):
#         self.t = title
#         self.q = quantity
#         self.a = author
#         self.p = price
#
#     def __repr__(self):
#         return f"Book: {self.t}, Quantity: {self.q}, Author: {self.a}, Price: {self.p}"
#
#
# book1 = Book('Book 1', 12, 'Author 1', 120)
# book2 = Book('Book 2', 18, 'Author 2', 220)
# book3 = Book('Book 3', 28, 'Author 3', 320)
#
# print(book1)
# print(book2)
# print(book3)



class students:
    def __init__(self,name,age,place,phone):
        self.n = name
        self.a =age
        self.p = place
        self.ph = phone
    def __repr__(self):
        return f"name = {self.n} ,Quantity = {self.a} ,place = {self.p},phone = {self.ph}"

if __name__ =="__main__":
 mate1 = students("hari",18,"manathana",989898)
 print(mate1)