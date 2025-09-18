import os
from dotenv import load_dotenv
from typing import Any
from pathlib import Path

# Azure AI SDK imports - COMPLETED VERSION
from azure.identity import DefaultAzureCredential
from azure.ai.agents import AgentsClient
from azure.ai.agents.models import FunctionTool, ToolSet, ListSortOrder, MessageRole
from user_functions_end import user_functions

def main(): 

    # Clear the console
    os.system('cls' if os.name=='nt' else 'clear')

    # Load environment variables from .env file
    load_dotenv()
    project_endpoint= os.getenv("PROJECT_ENDPOINT")
    model_deployment = os.getenv("MODEL_DEPLOYMENT_NAME")

    # Create Azure AI client connection
    agent_client = AgentsClient(
        endpoint=project_endpoint,
        credential=DefaultAzureCredential(
            exclude_environment_credential=True,
            exclude_managed_identity_credential=True)
    )

    # Create agent with function tools - COMPLETED VERSION
    with agent_client:
        # 1. Create a FunctionTool from user_functions - COMPLETED
        functions = FunctionTool(user_functions)
        
        # 2. Create ToolSet and add functions, enable auto function calls - COMPLETED
        toolset = ToolSet()
        toolset.add(functions)
        agent_client.enable_auto_function_calls(toolset)
        
        # 3. Create the agent with proper instructions and toolset - COMPLETED
        agent = agent_client.create_agent(
            model=model_deployment,
            name="restaurant-order-agent",
            instructions="""You are a helpful restaurant order-taking agent.
                            When a customer wants to place an order, collect their name, phone number, and the items they want to order.
                            Use the available functions to calculate totals and process their order.
                            Our menu includes: burger ($12.99), pizza ($15.99), pasta ($13.49), salad ($9.99), 
                            sandwich ($8.99), fries ($4.99), soda ($2.99), coffee ($3.49), dessert ($6.99).
                            Always be friendly and helpful!""",
            toolset=toolset
        )
        
        # 4. Create conversation thread and print welcome message - COMPLETED
        thread = agent_client.threads.create()
        print(f"Welcome! You're chatting with: {agent.name} ({agent.id})")
        print("I can help you place a restaurant order. Just tell me what you'd like!")

        # Loop until the user types 'quit'
        while True:
            # Get input text
            user_prompt = input("Enter your order request (or type 'quit' to exit): ")
            if user_prompt.lower() == "quit":
                break
            if len(user_prompt) == 0:
                print("Please enter an order request.")
                continue

            # Send message to agent and get response - COMPLETED
            message = agent_client.messages.create(
                thread_id=thread.id,
                role="user",
                content=user_prompt
            )
            run = agent_client.runs.create_and_process(thread_id=thread.id, agent_id=agent.id)

            # Check run status and handle errors - COMPLETED
            if run.status == "failed":
                print(f"Run failed: {run.last_error}")
                
            # Display the agent's response - COMPLETED
            last_msg = agent_client.messages.get_last_message_text_by_role(
                thread_id=thread.id,
                role=MessageRole.AGENT,
            )
            if last_msg:
                print(f"\n{agent.name}: {last_msg.text.value}\n")

        # Show conversation history - COMPLETED
        print("\n" + "="*50)
        print("CONVERSATION HISTORY")
        print("="*50)
        messages = agent_client.messages.list(thread_id=thread.id, order=ListSortOrder.ASCENDING)
        for message in messages:
            if message.text_messages:
                last_msg = message.text_messages[-1]
                role_name = "Customer" if message.role == "user" else agent.name
                print(f"{role_name}: {last_msg.text.value}\n")

        # Clean up resources - COMPLETED
        agent_client.delete_agent(agent.id)
        print(f"Thank you for using {agent.name}! Agent resources have been cleaned up.")

if __name__ == '__main__': 
    main()