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

# Create a function to calculate order total
def calculate_order_total(items: list) -> str:
    total = 0.0
    order_details = []
    
    for item in items:
        item_lower = item.lower().strip()
        if item_lower in MENU_ITEMS:
            price = MENU_ITEMS[item_lower]
            total += price
            order_details.append({"item": item_lower, "price": price})
        else:
            order_details.append({"item": item_lower, "price": 0.0, "note": "Item not found"})
    
    result = {
        "items": order_details,
        "total": round(total, 2),
        "message": f"Order total calculated: ${total:.2f}"
    }
    return json.dumps(result)

# Create a function to process a restaurant order
def process_restaurant_order(customer_name: str, phone_number: str, items: list) -> str:
    script_dir = Path(__file__).parent
    order_number = str(uuid.uuid4()).replace('-', '')[:8]
    file_name = f"order-{order_number}.txt"
    file_path = script_dir / file_name
    
    # Calculate total
    order_calc = json.loads(calculate_order_total(items))
    
    # Create order text
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
    
    # Save order
    file_path.write_text(order_text)
    
    message = {
        "message": f"Order {order_number} processed successfully! Total: ${order_calc['total']:.2f}. Order saved as {file_name}",
        "order_number": order_number,
        "total": order_calc['total']
    }
    return json.dumps(message)

# Define a set of callable functions
user_functions: Set[Callable[..., Any]] = {
    calculate_order_total,
    process_restaurant_order
}