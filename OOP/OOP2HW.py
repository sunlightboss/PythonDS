class Order:
    def __init__(self, amount):
        self._amount = amount

    def get_amount(self):
        return self._amount

    def get_type(self):
        return "Order"


class OnlineOrder(Order):
    def get_type(self):
        return "OnlineOrder"


class OfflineOrder(Order):
    def get_type(self):
        return "OfflineOrder"


class OrderList:
    def __init__(self, orders):
        self.orders = orders

    def __iter__(self):
        return iter(self.orders)


orders = OrderList([
    OnlineOrder(1000),
    OfflineOrder(500),
    OnlineOrder(2000)
])

for order in orders:
    print(f"Type: {order.get_type()}, Amount: {order.get_amount()}")

##########