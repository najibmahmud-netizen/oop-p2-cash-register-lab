class CashRegister:
    def __init__(self, discount=0):
        self.discount = discount
        self.total = 0
        self.items = []
        self.previous_transactions = []

    @property
    def discount(self):
        return self._discount

    @discount.setter
    def discount(self, value):
        if isinstance(value, int) and 0 <= value <= 100:
            self._discount = value
        else:
            print("Not valid discount")

    def add_item(self, item, price, quantity):
        self.total += price * quantity

        self.items.append(item)

        transaction = {
            "item": item,
            "price": price,
            "quantity": quantity
        }

        self.previous_transactions.append(transaction)

    def apply_discount(self):
        if len(self.previous_transactions) == 0:
            print("There is no discount to apply.")
            return

        discount_amount = self.total * (self.discount / 100)
        self.total -= discount_amount

    def void_last_transaction(self):
        if len(self.previous_transactions) == 0:
            return

        last_transaction = self.previous_transactions.pop()

        self.total -= (
            last_transaction["price"]
            * last_transaction["quantity"]
        )

        self.items.pop()