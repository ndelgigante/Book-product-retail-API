class Order:
    def __init__(self, orderNumber, orderDate, userid):
        self.orderNumber = orderNumber
        self.orderDate = orderDate
        self.userid = userid

    def to_list(self):
        return [self.orderNumber, self.orderDate, self.userid]