class Product:
    def __init__(self, bookid, bookname, bookdescription, bookauthor, bookgenre, quantity, MSRP):
        self.bookid = bookid
        self.bookname = bookname
        self.bookdescription = bookdescription
        self.bookauthor = bookauthor
        self.bookgenre = bookgenre
        self.quantity = quantity
        self.MSRP = MSRP

    def to_list(self):
        return [self.bookid, self.bookname, self.bookdescription, self.bookauthor, self.bookgenre, self.quantity, self.MSRP]