class Library:
    def __init__(self,listOfBooks):
         self.Books=listOfBooks
    def dispalyBooks(self):
        print("The Books present are:")
        for index,item in enumerate(self.Books):
            print("\t"+str(index+1),item)
    def borrowBook(self,bookname):
        if bookname in self.Books:
            print(f"the  {bookname} book is issued and pls return it within 30day after then u will be fined!")
            self.Books.remove(bookname)
            return True
        else:
            print("Sorry,book is not present in lib pls wait until someone returned it or check our e-lib")
            return False
    def returnBook(self,bookname):
        self.Books.append(bookname)
        print("book is returned or U Added a new book ! ")

class Student:
    def requestBook(self):
        self.Books=input("Enter the book U want to request:\n")
        return self.Books
    def returnBook(self):
        self.Books=input("Enter the book U want to return:\n")
        return self.Books

if __name__=="__main__":
    DJsanghvi_libray=Library(["algorims","c++ by upen","python by harry","c by alan"])
    Upendra=Student()
    rahul=Student()
    while(True):
        start='''*******Welcome To The DJsanghvi-libray*******
        Press the key:
        1.Lists all Books
        2.Request Books
        3.Add/Return Books
        4.Quit
        '''
        print(start)
        a=int(input("Enter the Choice:\n"))
        if a==1:
            DJsanghvi_libray.dispalyBooks()
        elif a==2:
            DJsanghvi_libray.borrowBook(rahul.requestBook())
        elif a==3:
            DJsanghvi_libray.returnBook(rahul.returnBook())

        elif a==4:
            print("Thank you to using this libray software")
            exit()
        else:
            print("Invalid Choice")


