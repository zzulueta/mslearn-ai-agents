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

# TODO: Complete the calculate_order_total function
def calculate_order_total(items: list) -> str:
    """Calculate the total cost for a list of menu items."""
    total = 0.0
    order_details = []
    
    # STUDENT TASK: Complete this function
    # 1. Loop through each item in the items list
    # 2. Check if item exists in MENU_ITEMS (convert to lowercase)
    # 3. Add price to total and create order detail entry
    # 4. Handle items not found in menu
    # 5. Return JSON string with total and itemized breakdown
    
    # Example structure for return value:
    # result = {
    #     "items": order_details,
    #     "total": round(total, 2),
    #     "message": f"Order total calculated: ${total:.2f}"
    # }
    # return json.dumps(result)
    
    pass  # Remove this and add your implementation



# TODO: Complete the process_restaurant_order function
def process_restaurant_order(customer_name: str, phone_number: str, items: list) -> str:
    """Process a complete restaurant order and save to file."""
    script_dir = Path(__file__).parent
    
    # STUDENT TASK: Complete this function
    # 1. Generate unique order number: str(uuid.uuid4()).replace('-', '')[:8]
    # 2. Create filename: f"order-{order_number}.txt"  
    # 3. Calculate total using your calculate_order_total function
    # 4. Create order text with customer info, items, and total
    # 5. Save to file using file_path.write_text(order_text)
    # 6. Return JSON confirmation with order number and total
    
    # Provided starter code:
    order_number = str(uuid.uuid4()).replace('-', '')[:8]
    file_name = f"order-{order_number}.txt"
    file_path = script_dir / file_name
    
    # TODO: Calculate total using calculate_order_total function
    # TODO: Create order text content
    # TODO: Save to file and return confirmation JSON
    
    pass  # Remove this and add your implementation



# TODO: Define the function set for Azure AI agent
# STUDENT TASK: Create a Set containing your implemented functions
# This set enables Azure AI agents to automatically discover and call your functions
# 
# Instructions:
# 1. Create a Set with type annotation: Set[Callable[..., Any]]
# 2. Name the variable 'user_functions' 
# 3. Add both of your implemented functions to the set
# 4. This allows the AI agent to automatically find and use your functions
#
# Example structure:
# user_functions: Set[Callable[..., Any]] = {
#     your_function_name_here,
#     your_other_function_name_here
# }
