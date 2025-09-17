import os
from dotenv import load_dotenv
from typing import Any
from pathlib import Path

# TODO: Add references
# STUDENT TASK: Import the necessary Azure AI SDK classes and your custom functions
# You will need to import:
# - DefaultAzureCredential from azure.identity
# - AgentsClient from azure.ai.agents
# - FunctionTool, ToolSet, ListSortOrder, MessageRole from azure.ai.agents.models
# - user_functions from your user_functions.py file


def main(): 

    # Clear the console
    os.system('cls' if os.name=='nt' else 'clear')

    # Load environment variables from .env file
    load_dotenv()
    project_endpoint= os.getenv("PROJECT_ENDPOINT")
    model_deployment = os.getenv("MODEL_DEPLOYMENT_NAME")

    # TODO: Connect to the Agent client
    # STUDENT TASK: Create an AgentsClient connection using:
    # - The project_endpoint from environment variables
    # - DefaultAzureCredential for authentication
    # - Exclude environment and managed identity credentials
    

    # TODO: Define an agent that can use the custom functions
    # STUDENT TASK: Create an agent setup that includes:
    # 1. Create a FunctionTool from your user_functions
    # 2. Create a ToolSet and add the functions to it
    # 3. Enable auto function calls on the agent client
    # 4. Create an agent with:
    #    - The specified model deployment
    #    - Name: "restaurant-order-agent"
    #    - Instructions for a restaurant order-taking agent
    #    - The toolset you created
    # 5. Create a conversation thread
    # 6. Print the agent name and ID

    
    # Loop until the user types 'quit'
    while True:
        # Get input text
        user_prompt = input("Enter your order request (or type 'quit' to exit): ")
        if user_prompt.lower() == "quit":
            break
        if len(user_prompt) == 0:
            print("Please enter an order request.")
            continue

        # TODO: Send a prompt to the agent
        # STUDENT TASK: 
        # 1. Create a message with the user's prompt
        # 2. Run the thread using create_and_process method


        # TODO: Check the run status for failures
        # STUDENT TASK: Add error handling to check if the run failed
        # and print the error message if it did

            
        # TODO: Show the latest response from the agent
        # STUDENT TASK: Retrieve and display the last message from the agent


    # TODO: Get the conversation history
    # STUDENT TASK: Print the full conversation log in chronological order
    # Show both user and agent messages


    # TODO: Clean up
    # STUDENT TASK: Delete the agent and print confirmation



if __name__ == '__main__': 
    main()