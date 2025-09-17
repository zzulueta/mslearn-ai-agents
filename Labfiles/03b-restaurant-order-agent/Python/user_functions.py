import json
import uuid
from pathlib import Path
from typing import Set, Callable, Any, Dict

# Menu items with prices (you can modify this as needed)
MENU_ITEMS = {
    "burger": 12.99,
    "pizza": 15.99,
    "pasta": 13.49,
    "salad": 9.99,
    "sandwich": 8.99,
    "fries": 4.99,
    "soda": 2.99,
    "coffee": 3.49,
    "dessert": 6.99
}

# TODO: Create a function to calculate order total
# STUDENT TASK: Implement a function named 'calculate_order_total' that:
# - Takes a list of menu items as parameter (items: list)
# - Calculates the total cost using the MENU_ITEMS dictionary
# - Returns a JSON string with the total amount and itemized breakdown
# 
# Example function signature:
# def calculate_order_total(items: list) -> str:
#     # Your implementation here
#     pass



# TODO: Create a function to process a restaurant order
# STUDENT TASK: Implement a function named 'process_restaurant_order' that:
# - Takes customer_name (str), phone_number (str), and items (list) as parameters
# - Generates a unique order number using uuid
# - Calculates total using the calculate_order_total function
# - Saves the order to a text file named "order-{order_number}.txt"
# - Returns a JSON string with order confirmation details
#
# Example function signature:
# def process_restaurant_order(customer_name: str, phone_number: str, items: list) -> str:
#     # Your implementation here
#     pass



# TODO: Define a set of callable functions
# STUDENT TASK: Create a Set containing your implemented functions
# This set will be used by the Azure AI agent to discover available functions
#
# Example:
# user_functions: Set[Callable[..., Any]] = {
#     # Add your functions here
# }
