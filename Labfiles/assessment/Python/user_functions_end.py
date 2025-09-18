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

# Complete calculate_order_total function - COMPLETED VERSION
def calculate_order_total(items: list) -> str:
    """Calculate the total cost for a list of menu items."""
    total = 0.0
    order_details = []
    
    # COMPLETED: Loop through each item and calculate total
    for item in items:
        item_lower = item.lower().strip()
        if item_lower in MENU_ITEMS:
            price = MENU_ITEMS[item_lower]
            total += price
            order_details.append({"item": item_lower, "price": price})
        else:
            order_details.append({"item": item_lower, "price": 0.0, "note": "Item not found"})
    
    # COMPLETED: Return JSON string with total and itemized breakdown
    result = {
        "items": order_details,
        "total": round(total, 2),
        "message": f"Order total calculated: ${total:.2f}"
    }
    return json.dumps(result)

# Complete process_restaurant_order function - COMPLETED VERSION
def process_restaurant_order(customer_name: str, phone_number: str, items: list) -> str:
    """Process a complete restaurant order and save to file."""
    script_dir = Path(__file__).parent
    
    # COMPLETED: Generate unique order number and create filename
    order_number = str(uuid.uuid4()).replace('-', '')[:8]
    file_name = f"order-{order_number}.txt"
    file_path = script_dir / file_name
    
    # COMPLETED: Calculate total using calculate_order_total function
    order_calc = json.loads(calculate_order_total(items))
    
    # COMPLETED: Create order text content
    order_text = f"Restaurant Order: {order_number}\n"
    order_text += f"Customer: {customer_name}\n"
    order_text += f"Phone: {phone_number}\n"
    order_text += f"Items ordered:\n"
    
    for item in order_calc['items']:
        if 'note' in item:
            order_text += f"  - {item['item']}: ${item['price']:.2f} ({item['note']})\n"
        else:
            order_text += f"  - {item['item']}: ${item['price']:.2f}\n"
    
    order_text += f"\nTotal: ${order_calc['total']:.2f}\n"
    order_text += f"Order placed at: {Path(__file__).parent}"
    
    # COMPLETED: Save to file and return confirmation JSON
    file_path.write_text(order_text)
    
    message = {
        "message": f"Order {order_number} processed successfully! Total: ${order_calc['total']:.2f}. Order saved as {file_name}",
        "order_number": order_number,
        "total": order_calc['total']
    }
    return json.dumps(message)

# Define the function set for Azure AI agent - COMPLETED VERSION
user_functions: Set[Callable[..., Any]] = {
    calculate_order_total,
    process_restaurant_order
}