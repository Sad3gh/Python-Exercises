import json
from json import dumps
from json import JSONDecodeError
from typing import TypeAlias, TextIO

JSON: TypeAlias = dict[str, "JSON"] | list["JSON"] | str | int | float | bool | None


class Product:
    def __init__(self, name, price, quantity, description):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.description = description

    def to_dict(self):
        """This function returns the dictionary format of our Product class
            which is a format that can be easily Serialized into JSON.
        """
        return {
            'name': self.name,
            'price': self.price,
            'quantity': self.quantity,
            'description': self.description
        }

    def update_quantity(self, amount):
        """ Update the quantity of the product. Positive amount increases
            the quantity and negative will decrease it.
        """
        if self.quantity + amount < 0:
            print(f"Cannot update the quantity.Not enough stock for {self.name}.Current stock: {self.quantity}")
        else:
            self.quantity += amount
            action = "added to" if amount > 0 else "Removed from"
            print(f"{abs(amount)} units {action} stock for {self.name}.New stock: {self.quantity}")

    def __str__(self):
        return f"{self.name}: ${self.price:.2f} (Available: {self.quantity})"


class Customer:
    def __init__(self, name, email, address):
        self.name = name
        self.email = email
        self.address = address

    def to_dict(self):
        """This function returns the dictionary format of our Product class
            which is a format that can be easily Serialized into JSON.
        """
        return {
            'name': self.name,
            'email': self.email,
            'address': self.address
        }

    def place_order(self, ordered_product, quantity):
        """ Place an order for a product if available """
        if quantity <= 0:
            print("The amount should be greater than zero.")
            return
        if ordered_product.quantity < quantity:
            print(f"Cannot place the order. only {ordered_product.quantity} available for {ordered_product.name}")
            return
        ordered_product.update_quantity(-quantity)
        order = Order(self, ordered_product, quantity)
        print(f"order placed. {order}")

    def __str__(self):
        return f"Customer Name: {self.name}, Email: {self.email}, Address: {self.address}"


class Order:
    def __init__(self, customer, ordered_product, quantity):
        self.customer = customer
        self.ordered_product = ordered_product
        self.quantity = quantity
        self.total_price = ordered_product.price * quantity

    def to_dict(self):
        """This function returns the dictionary format of our Product class
           which is a format that can be easily Serialized into JSON.
        """
        return {
            'customer': self.customer.to_dict(),  # Convert Customer to dict
            'ordered_product': self.ordered_product.to_dict(),  # Convert Product to dict
            'quantity': self.quantity,
            'total_price': self.total_price
        }

    def __str__(self):
        return (f"Order for {self.customer.name}: {self.quantity} x {self.ordered_product.name} "
                f"@ {self.ordered_product.price:.2f} each. Total: ${self.total_price:.2f}")


class Store:
    def __init__(self):
        self.products = []
        self.customers = []
        self.orders = []

    def add_product(self, new_product):
        """Add a new product to the store"""
        self.products.append(new_product)
        print(f"Product added: {new_product}")

    def register_customer(self, customer):
        """ Register a new customer to the store """
        self.customers.append(customer)
        print(f"Customer registered: {customer}")

    def process_order(self, customer, product_name, quantity):
        """ Process an order for a given product and quantity """
        # Find the first matching product in our list of products with the product name given in the order
        found_product = next((p for p in self.products if p.name == product_name), None)
        if found_product is None:
            print(f"product '{product_name}' not found.")
            return
        # Place the order through the customer
        customer.place_order(found_product, quantity)
        # Create an order object
        order = Order(customer, found_product, quantity)
        # Add the order to the orders list
        self.orders.append(order)

    def display_products(self):
        """ Display all the products available in the store"""
        print("Available Products:")
        for item in self.products:
            print(item)

    def display_orders(self):
        """ Display all the orders. """
        for order in self.orders:
            print(order)

    def save_data(self, filename='store_data.json'):
        """Save products, customers, and orders to a JSON file.
           Pay attention how we used to_dict methods in each of our list comprehensions below. we did that
           because of the conversion of the object instances to a format (dictionary here) that can be
           easily serialized into JSON.
        """
        data = {
            'products': [product.to_dict() for product in self.products],
            'customers': [customer.to_dict() for customer in self.customers],
            'orders': [order.to_dict() for order in self.orders]
        }

        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4)
            print("Data saved to", filename)

    def load_data(self, filename='store_data.json'):
        """Loads products,customers and orders from a JSON file. """
        try:
            with open(filename, 'r') as f:
                data = json.load(f)
            self.products = [Product(**item) for item in data['products']]
            self.customers = [Customer(**item) for item in data['customers']]
            self.orders = [Order(Customer(**order['customer']), Product(**order['ordered_product']), order['quantity'])
                           for order in data['orders']]
            print("Data loaded from ", filename)
        except FileNotFoundError:
            print("No data file found. Starting with empty store")
        except JSONDecodeError:
            print("Error decoding json. Starting with empty store")


def main():
    store = Store()
    store.load_data()
    while True:
        print("\n--- Online Store Management System ---")
        print("1. Add Product")
        print("2. Register Customer")
        print("3. Process Order")
        print("4. Display Products")
        print("5. Display Orders")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            # Add Product
            name = input("Enter product name: ")
            price = float(input("Enter product price: "))
            quantity = int(input("Enter product quantity: "))
            description = input("Enter product description: ")
            new_product = Product(name, price, quantity, description)
            store.add_product(new_product)

        elif choice == '2':
            # Register Customer
            name = input("Enter customer name: ")
            email = input("Enter customer email: ")
            address = input("Enter customer address: ")
            customer = Customer(name, email, address)
            store.register_customer(customer)

        elif choice == '3':
            # Process Order
            customer_name = input("Enter customer name: ")
            product_name = input("Enter product name: ")
            quantity = int(input("Enter quantity: "))
            customer = next((c for c in store.customers if c.name == customer_name), None)
            if customer:
                store.process_order(customer, product_name, quantity)
            else:
                print(f"Customer '{customer_name}' not found.")

        elif choice == '4':
            # Display Products
            store.display_products()

        elif choice == '5':
            # Display Orders
            store.display_orders()

        elif choice == '6':
            store.save_data()  # Save data before exiting
            print("Exiting the program. Goodbye!")
            break

        else:
            print("Invalid choice. Please choose a number between 1 and 6.")


if __name__ == "__main__":
    main()
