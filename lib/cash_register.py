class CashRegister:
    def __init__(self, discount=0):
        self.discount = discount
        self.total = 0.0
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

    def add_item(self, item, price, quantity=1):
        self.total += price * quantity

        # Add item(s) to items list
        for _ in range(quantity):
            self.items.append(item)

        # Store transaction for possible voiding later
        self.previous_transactions.append({
            "item": item,
            "price": price,
            "quantity": quantity
        })

    def apply_discount(self):
        if self.discount == 0:
            print("There is no discount to apply.")
            return

        self.total = self.total - (self.total * self.discount / 100)

        print(f"After the discount, the total comes to ${int(self.total)}.")

    def void_last_transaction(self):
        if len(self.previous_transactions) == 0:
            return

        last_transaction = self.previous_transactions.pop()

        self.total -= (
            last_transaction["price"]
            * last_transaction["quantity"]
        )

        # Remove all occurrences added in that transaction
        for _ in range(last_transaction["quantity"]):
            self.items.pop()