class Hash:
    def __init__(self):
        self.size = 1000
        self.table = [None]* self.size
    def calculate_hash(self,key):
        return key%self.size
    def add(self, key):
        val = self.calculate_hash(key)
        if self.table[val] == None:
            self.table[val] =[key]
        else :
            self.table[val].append(key)
    def remove(self,key):
        val = self.calculate_hash(key)
        if self.table[val] != None:
            while key in self.table[val]:
                self.table[val].remove(key)


    def check(self,key):
        val = self.calculate_hash(key)
        if self.table[val] !=None:
            return key in self.table[val]
        else :
            return False

if __name__ == "__main__":
    h = Hash()
    h.add(20)
    h.check(20)
    
    








# class Hash:
#     def __init__(self) :
#         self.size = 1000
#         self.table = [None] *self.size
#     def calculate(self,key):
#             return key % self.size

#     def add(self,key):
#         p = self.calculate(key)
#         if self.table[p] ==None:
#             self.table[p] = key
#         else:
#             self.table[p].append(key)
#     def remove(self,key):
#         p =self.calculate(key)
#         if self.table[p] !=None:
#             while key in self.table[p]:
#                 self.table[p].remove(key)


                


             
        






















# def remove(self,val):
#     val = self.calculatehas(val)
#     if self.table[val] != none:
#         while key in self.table[val]:
#             self.table[val].remove(key)
#



#
# def add(self,key):
#     hash = self.calculatehash(key)
#     if self.table[hash] ==None:
#         self.table[hash] = [key]
#     else:
#         self.tabel[hash].append(key)