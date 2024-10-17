class User:
    def __init__(self, user_id, name, email, address):
        self.user_id = user_id
        self.name = name
        self.email = email
        self.address = address
        self.orders = []

    def create_order(self, products):
        new_order = Order(self, products)
        self.orders.append(new_order)
        return new_order

    def view_orders(self):
        return self.orders


class Product:
    def __init__(self, product_id, name, price, stock_level):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.stock_level = stock_level


class Order:
    def __init__(self, user, products):
        self.order_id = generate_order_id()  # Generate unique ID
        self.user = user
        self.products = products
        self.status = 'Pending'
        self.total_amount = sum([product.price for product in products])

    def update_status(self, new_status):
        self.status = new_status


class Payment:
    def __init__(self, order, amount):
        self.payment_id = generate_payment_id()  # Generate unique ID
        self.order_id = order.order_id
        self.amount = amount
        self.status = 'Pending'

    def make_payment(self):
        # Payment gateway integration logic
        self.status = 'Completed'


# Utility function to generate unique IDs
def generate_order_id():
    import uuid
    return str(uuid.uuid4())


def generate_payment_id():
    import uuid
    return str(uuid.uuid4())
