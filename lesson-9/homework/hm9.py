#1.. Circle Class
Write a Python program to create a class representing a Circle. Include methods to calculate its area and perimeter.
import math

class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return math.pi * self.radius ** 2
    
    def perimeter(self):
        return 2 * math.pi * self.radius

radius = float(input("Enter the radius of the circle: "))
circle = Circle(radius)

print(f"The area of the circle is: {circle.area():.2f}")
print(f"The perimeter (circumference) of the circle is: {circle.perimeter():.2f}")

#2. Person Class
Write a Python program to create a Person class. Include attributes like name, country, and date of birth. Implement a method to determine the person's age.
from datetime import datetime

class Person:
    def __init__(self, name, country, date_of_birth)
        self.name = name
        self.country = country
        self.date_of_birth = datetime.strptime(date_of_birth, "%Y-%m-%d")  # Convert string to datetime object
    
    def age(self):
      
        today = datetime.today()
        age = today.year - self.date_of_birth.year - ((today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day))
        return age


name = input("Enter your name: ")
country = input("Enter your country: ")
date_of_birth = input("Enter your date of birth (YYYY-MM-DD): ")

person = Person(name, country, date_of_birth)


print(f"\nName: {person.name}")
print(f"Country: {person.country}")
print(f"Age: {person.age()} years old")

#3. Calculator Class
Write a Python program to create a Calculator class. Include methods for basic arithmetic operations.

class Calculator:
    def __init__(self):
        # Initialize the calculator (no state needed for basic operations)
        pass
    
    def add(self, a, b):
        return a + b
    
    def subtract(self, a, b):
        return a - b
    
    def multiply(self, a, b):
        return a * b
    
    def divide(self, a, b):
        try:
            return a / b
        except ZeroDivisionError:
            return "Error: Division by zero is not allowed."

# Example usage
calc = Calculator()

# Taking user input for the operation
print("Basic Calculator - Operations: +, -, *, /")
a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))
operation = input("Enter operation (+, -, *, /): ")

# Perform the selected operation
if operation == "+":
    result = calc.add(a, b)
elif operation == "-":
    result = calc.subtract(a, b)
elif operation == "*":
    result = calc.multiply(a, b)
elif operation == "/":
    result = calc.divide(a, b)
else:
    result = "Invalid operation."

# Display the result
print(f"Result: {result}")
#4. Shape and Subclasses
Write a Python program to create a class that represents a shape. Include methods to calculate its area and perimeter. Implement subclasses for different shapes like Circle, Triangle, and Square.
import math

# Base class representing a generic shape
class Shape:
    def area(self):
        raise NotImplementedError("Subclass must implement abstract method")

    def perimeter(self):
        raise NotImplementedError("Subclass must implement abstract method")

# Subclass for Circle
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        # Area of a circle: π * r^2
        return math.pi * self.radius ** 2

    def perimeter(self):
        # Perimeter (Circumference) of a circle: 2 * π * r
        return 2 * math.pi * self.radius

# Subclass for Triangle
class Triangle(Shape):
    def __init__(self, base, height, side1, side2, side3):
        self.base = base
        self.height = height
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def area(self):
        # Area of a triangle: 0.5 * base * height
        return 0.5

#5 Binary Search Tree Class
Write a Python program to create a class representing a binary search tree. Include methods for inserting and searching for elements in the binary tree.
class Node:
    def __init__(self, key):
        # Node class to represent each element in the tree
        self.left = None
        self.right = None
        self.value = key

class BinarySearchTree:
    def __init__(self):
        self.root = None

    # Method to insert a new value into the tree
    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert_recursive(self.root, key)
    
    def _insert_recursive(self, node, key):
        # Recursive helper function to insert a value
        if key < node.value:
            if node.left is None:
                node.left = Node(key)
            else:
                self._insert_recursive(node.left, key)
        else:
            if node.right is None:
                node.right = Node(key)
            else:
                self._insert_recursive(node.right, key)

    # Method to search for a value in the tree
    def search(self, key):
        return self._search_recursive(self.root, key)
    
    def _search_recursive(self, node, key):
        if node is None:
            return False
        if key == node.value:
            return True
        elif key < node.value:
            return self._search_recursive(node.left, key)
        else:
            return self._search_recursive(node.right, key)

# Example usage:
def main():
    # Create a binary search tree instance
    bst = BinarySearchTree()

    # Insert values into the binary search tree
    values = [20, 8, 22, 4, 12, 10, 14]
    for value in values:
        bst.insert(value)
    
    # Search for values
    search_values = [10, 5, 22,_

#6. Stack Data Structure
Write a Python program to create a class representing a stack data structure. Include methods for pushing and popping elements.
class Stack:
    def __init__(self):
        # Initialize the stack as an empty list
        self.stack = []
    
    def push(self, item):
        # Method to push an item onto the stack
        self.stack.append(item)
        print(f"Item {item} pushed to the stack.")
    
    def pop(self):
        # Method to pop an item from the stack
        if not self.is_empty():
            popped_item = self.stack.pop()
            print(f"Item {popped_item} popped from the stack.")
            return popped_item
        else:
            print("Stack is empty. Cannot pop.")
            return None
    
    def peek(self):
        # Method to return the top item of the stack without removing it
        if not self.is_empty():
            return self.stack[-1]
        else:
            print("Stack is empty. No top element.")
            return None
    
    def is_empty(self):
        # Method to check if the stack is empty
        return len(self.stack) == 0
    
    def size(self):
        # Method to get the size of the stack
        return len(self.stack)

# Example usage:
def main():
    stack = Stack()

    # Push items onto the stack
    stack.push(10)
    stack.push(20)
    stack.push(30)

    # Peek the top item
    print(f"Top item: {stack.peek()}")

    # Pop items from the stack
    stack.pop()
    stack.pop()

    # Check if the stack is empty and print its size
    print(f"Is the stack empty? {stack.is_empty()}")
    print(f"Stack size: {stack.size()}")

    # Try popping from an empty stack
    stack.pop()

if __name__ == "__main__":
    main()

#7.Linked List Data Structure
Write a Python program to create a class representing a linked list data structure. Include methods for displaying linked list data, inserting, and deleting nodes.

class Node:
    def __init__(self, data):
        # Node class represents an element of the linked list
        self.data = data
        self.next = None  # Pointer to the next node

class LinkedList:
    def __init__(self):
        # Initialize the linked list with an empty head
        self.head = None

    def insert_at_end(self, data):
        # Method to insert a node at the end of the list
        new_node = Node(data)
        if self.head is None:
            # If the list is empty, make the new node the head
            self.head = new_node
        else:
            # Traverse to the end of the list and insert the new node
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        print(f"Node with data {data} inserted at the end.")

    def insert_at_beginning(self, data):
        # Method to insert a node at the beginning of the list
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        print(f"Node with data {data} inserted at the beginning.")

    def delete(self, data):
        # Method to delete a node with specific data
        if self.head is None:
            print("The list is empty. Cannot delete.")
            return
        
        # Special case for deleting the head node
        if self.head.data == data:
            self.head = self.head.next
            print(f"Node with data {data} deleted from the beginning.")
            return
        
        # Traverse the list to find the node to delete
        current = self.head
        while current.next and current.next.data != data:
            current = current.next
        
        if current.next is None:
            print(f"Node with data {data} not found.")
        else:
            current.next = current.next.next
            print(f"Node with data {data} deleted.")
    
    def display(self):
        # Method to display the linked list
        if self.head is None:
            print("The list is empty.")
            return
        current = self.head

#8. Shopping Cart Class
Write a Python program to create a class representing a shopping cart. Include methods for adding and removing items, and calculating the total price.
class Item:
    def __init__(self, name, price, quantity=1):
        # Item class to represent an item in the cart
        self.name = name
        self.price = price
        self.quantity = quantity

    def total_price(self):
        # Returns the total price for this item (price * quantity)
        return self.price * self.quantity

class ShoppingCart:
    def __init__(self):
        # Initialize the shopping cart with an empty list of items
        self.cart = []

    def add_item(self, item):
        # Add an item to the cart (if item already exists, update quantity)
        for i in self.cart:
            if i.name == item.name:
                i.quantity += item.quantity
                print(f"Updated quantity of {item.name} to {i.quantity}.")
                return
        self.cart.append(item)
        print(f"Added {item.quantity} {item.name}(s) to the cart.")

    def remove_item(self, item_name):
        # Remove an item from the cart by name
        for i in range(len(self.cart)):
            if self.cart[i].name == item_name:
                self.cart.pop(i)
                print(f"Removed {item_name} from the cart.")
                return
        print(f"Item {item_name} not found in the cart.")

    def total_price(self):
        # Calculate the total price of all items in the cart
        total = sum(item.total_price() for item in self.cart)
        return total

    def display_items(self):
        # Display all items in the cart
        if not self.cart:
            print("Your cart is empty.")
        else:
            print("Items in your cart:")
            for item in self.cart:
                print(f"{item.quantity} x {item.name} - ${item.price} each")
            print(f"Total price: ${self.total_price():.2f}")

# Example usage:
def main():
    # Create a shopping cart
    cart = ShoppingCart()

    # Create some items
    item1 = Item("Apple", 0.99, 5)  # 5 Apples, $0.99 each
    item2 = Item("Banana", 0.59, 3)  # 3 Bananas, $0.59 each
    item3 = Item("Orange", 1.29, 2)  # 2 Oranges, $1.29 each

    # Add items to the cart
    cart.add_item(item1)
    cart.add_item(item2)
    cart.add_item(item3)

    # Display the cart items and total price
    cart.display_items()

    # Remove an item and display the updated cart
    cart.remove_item("Banana")
    cart.display_items()

if __name__ == "__main__":
    main()
#9. Stack with Display
Write a Python program to create a class representing a stack data structure. Include methods for pushing, popping, and displaying elements.
  class Stack:
    def __init__(self):
        # Initialize the stack as an empty list
        self.stack = []

    def push(self, item):
        # Push an item onto the stack
        self.stack.append(item)
        print(f"Item {item} pushed to the stack.")

    def pop(self):
        # Pop an item from the stack
        if not self.is_empty():
            popped_item = self.stack.pop()
            print(f"Item {popped_item} popped from the stack.")
            return popped_item
        else:
            print("Stack is empty. Cannot pop.")
            return None

    def display(self):
        # Display all elements in the stack
        if not self.is_empty():
            print("Stack elements (top to bottom):")
            for item in reversed(self.stack):  # Display from top to bottom
                print(item)
        else:
            print("The stack is empty.")

    def is_empty(self):
        # Check if the stack is empty
        return len(self.stack) == 0

    def size(self):
        # Get the size of the stack
        return len(self.stack)


# Example usage:
def main():
    stack = Stack()

    # Push elements onto the stack
    stack.push(10)
    stack.push(20)
    stack.push(30)

    # Display stack
    stack.display()

    # Pop elements from the stack
    stack.pop()

    # Display stack after popping
    stack.display()

    # Push a new element
    stack.push(40)

    # Display stack after new push
    stack.display()

    # Check the size

#10. Queue Data Structure
Write a Python program to create a class representing a queue data structure. Include methods for enqueueing and dequeueing elements.
class Queue:
    def __init__(self):
        # Initialize the queue as an empty list
        self.queue = []

    def enqueue(self, item):
        # Method to add an item to the queue (enqueue)
        self.queue.append(item)
        print(f"Item {item} added to the queue.")

    def dequeue(self):
        # Method to remove and return the item from the front of the queue (dequeue)
        if not self.is_empty():
            dequeued_item = self.queue.pop(0)
            print(f"Item {dequeued_item} removed from the queue.")
            return dequeued_item
        else:
            print("Queue is empty. Cannot dequeue.")
            return None

    def front(self):
        # Method to get the front item of the queue without removing it
        if not self.is_empty():
            return self.queue[0]
        else:
            print("Queue is empty. No front element.")
            return None

    def is_empty(self):
        # Method to check if the queue is empty
        return len(self.queue) == 0

    def size(self):
        # Method to get the size of the queue
        return len(self.queue)

    def display(self):
        # Method to display all the elements in the queue
        if self.is_empty():
            print("The queue is empty.")
        else:
            print("Queue elements:")
            for item in self.queue:
                print(item, end=" -> ")
            print("None")


# Example usage:
def main():
    queue = Queue()

    # Enqueue some elements
#11. Bank Class
Write a Python program to create a class representing a bank. Include methods for managing customer accounts and transactions.
class Customer:
    def __init__(self, customer_id, name, initial_balance=0):
        # Initialize the customer with an ID, name, and an initial balance
        self.customer_id = customer_id
        self.name = name
        self.balance = initial_balance

    def deposit(self, amount):
        # Deposit money into the customer's account
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount} to {self.name}'s account. New balance: ${self.balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        # Withdraw money from the customer's account
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print(f"Withdrew ${amount} from {self.name}'s account. New balance: ${self.balance}")
            else:
                print("Insufficient funds for withdrawal.")
        else:
            print("Withdrawal amount must be positive.")

    def get_balance(self):
        # Return the current balance of the customer
        return self.balance

    def display_account_info(self):
        # Display the customer's account details
        print(f"Customer ID: {self.customer_id}")
        print(f"Customer Name: {self.name}")
        print(f"Account Balance: ${self.balance}")


class Bank:
    def __init__(self):
        # Initialize the bank with an empty dictionary of customers
        self.customers = {}

    def add_customer(self, customer):
        # Add a new customer to the bank
        if customer.customer_id not in self.customers:
            self.customers[customer.customer_id] = customer
            print(f"Customer {customer.name} added to the bank.")
        else:
            print(f"Customer with ID {customer.customer_id} already exists.")

    def get_customer(self, customer_id):
        # Retrieve a customer by their ID
        return self.customers.get(customer_id, None)

    def perform_transaction(self, customer_id, action, amount=0):
        # Perform a transaction (deposit or withdraw) for a given customer ID
        customer = self.get_customer(customer_id)
        if customer:
            if action == 'deposit':
                customer.deposit(amount)
            elif action == 'withdraw':
                customer.withdraw(amount)
            else:
                print("Invalid transaction type.")
        else:
            print(f"Customer with ID {customer_id} not found.")

    def display_all_customers(self):
        # Display all customers' account information
        if self.customers:
            print("\nAll Customers' Information:")
            for customer in self.customers.values():
                customer.display_account_info()
                print("-" * 30)
        else:
            print("No customers found in the bank.")


# Example usage:
def main():
    # Create a bank instance
    bank = Bank()

    # Create customers
    customer1 = Customer(customer_id=101, name="Alice", initial_balance=1000)
    customer2 = Customer(customer_id=102, name="Bob", initial_balance=500)

    # Add customers to the bank
    bank.add_customer(customer1)


