#!/usr/bin/env python3
"""
Quick Test Runner for Restaurant Order AI Agent Grading
======================================================

This script provides a simple way to test the auto-grader with sample submissions.
"""

import os
import sys
import shutil
import tempfile
from pathlib import Path
from grade_submission import AIAgentGrader

def create_sample_student_submission(base_dir: Path) -> Path:
    """Create a sample student submission for testing"""
    
    student_dir = base_dir / "sample_student"
    student_dir.mkdir(exist_ok=True)
    
    # Create a partially completed agent.py
    agent_code = '''import os
from dotenv import load_dotenv
from typing import Any
from pathlib import Path

# Student completed imports
from azure.identity import DefaultAzureCredential
from azure.ai.agents import AgentsClient
from azure.ai.agents.models import FunctionTool, ToolSet, ListSortOrder, MessageRole
from user_functions import user_functions

def main(): 
    os.system('cls' if os.name=='nt' else 'clear')
    
    load_dotenv()
    project_endpoint= os.getenv("PROJECT_ENDPOINT")
    model_deployment = os.getenv("MODEL_DEPLOYMENT_NAME")

    # Student completed Azure connection
    agent_client = AgentsClient(
        endpoint=project_endpoint,
        credential=DefaultAzureCredential(
            exclude_environment_credential=True,
            exclude_managed_identity_credential=True)
    )

    # Student completed agent setup - partial implementation
    with agent_client:
        functions = FunctionTool(user_functions)
        toolset = ToolSet()
        toolset.add(functions)
        agent_client.enable_auto_function_calls(toolset)
        
        agent = agent_client.create_agent(
            model=model_deployment,
            name="restaurant-order-agent",
            instructions="You are a restaurant order agent.",
            toolset=toolset
        )
        
        thread = agent_client.threads.create()
        print(f"Chatting with: {agent.name}")
    
    while True:
        user_prompt = input("Enter order (quit to exit): ")
        if user_prompt.lower() == "quit":
            break
        if len(user_prompt) == 0:
            print("Please enter an order.")
            continue

        # Student completed message handling
        message = agent_client.messages.create(
            thread_id=thread.id,
            role="user",
            content=user_prompt
        )
        run = agent_client.runs.create_and_process(thread_id=thread.id, agent_id=agent.id)

        # Missing error handling - student didn't implement this
        
        # Student completed response retrieval
        last_msg = agent_client.messages.get_last_message_text_by_role(
            thread_id=thread.id,
            role=MessageRole.AGENT,
        )
        if last_msg:
            print(f"{agent.name}: {last_msg.text.value}")

    # Missing conversation history - student didn't implement this
    
    # Student completed cleanup
    agent_client.delete_agent(agent.id)
    print("Agent deleted")

if __name__ == '__main__': 
    main()
'''

    # Create user_functions.py with partial implementation
    functions_code = '''import json
import uuid
from pathlib import Path
from typing import Set, Callable, Any

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

# Student implemented this function correctly
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

# Student implemented this function with minor issues
def process_restaurant_order(customer_name: str, phone_number: str, items: list) -> str:
    order_number = str(uuid.uuid4()).replace('-', '')[:8]
    file_name = f"order-{order_number}.txt"
    
    # Student didn't use proper file path handling
    with open(file_name, 'w') as f:
        f.write(f"Order: {order_number}\\nCustomer: {customer_name}\\nPhone: {phone_number}\\n")
        for item in items:
            f.write(f"Item: {item}\\n")
    
    # Student returned simple string instead of JSON
    return f"Order {order_number} created"

# Student correctly defined the functions set
user_functions: Set[Callable[..., Any]] = {
    calculate_order_total,
    process_restaurant_order
}
'''

    # Write the files
    (student_dir / "agent.py").write_text(agent_code)
    (student_dir / "user_functions.py").write_text(functions_code)
    
    return student_dir

def run_sample_test():
    """Run a sample test to demonstrate the grader"""
    
    print("🧪 Running Sample Auto-Grader Test")
    print("=" * 50)
    
    with tempfile.TemporaryDirectory() as temp_dir:
        temp_path = Path(temp_dir)
        
        # Create sample student submission
        student_dir = create_sample_student_submission(temp_path)
        
        # Use the reference solution as the reference directory
        reference_dir = Path(__file__).parent
        
        print(f"📁 Student submission: {student_dir}")
        print(f"📁 Reference solution: {reference_dir}")
        
        # Run the grader
        grader = AIAgentGrader(str(student_dir), str(reference_dir))
        report = grader.grade_submission()
        grader.print_report(report)
        
        print("\n🎯 Test completed! This demonstrates how the auto-grader evaluates student submissions.")

if __name__ == "__main__":
    run_sample_test()