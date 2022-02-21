
from tkinter import N


def ladder(a):
    for i in range(a+1):
        print(str("#"*i).rjust(a))


if __name__ == "__main__":
    n = int(input("enter number"))
    ladder(n)
