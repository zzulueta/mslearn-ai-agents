import os
from dotenv import load_dotenv
from typing import Any
from pathlib import Path

# TODO: Add Azure AI SDK imports
# STUDENT TASK: Import these classes for Azure AI agent functionality:
from azure.identity import DefaultAzureCredential
from azure.ai.agents import AgentsClient
# TODO: Import FunctionTool, ToolSet, ListSortOrder, MessageRole from azure.ai.agents.models
# TODO: Import user_functions from your user_functions.py file (this should be the Set you create)


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

    # TODO: Create agent with function tools
    # STUDENT TASK: Complete the agent setup:
    with agent_client:
        # TODO: 1. Create a FunctionTool from your user_functions
        # functions = FunctionTool(user_functions)
        
        # TODO: 2. Create ToolSet and add functions, enable auto function calls
        # toolset = ToolSet()
        # toolset.add(functions)
        # agent_client.enable_auto_function_calls(toolset)
        
        # TODO: 3. Create the agent with proper instructions and toolset
        # agent = agent_client.create_agent(
        #     model=model_deployment,
        #     name="restaurant-order-agent",
        #     instructions="Your restaurant agent instructions here...",
        #     toolset=toolset
        # )
        
        # TODO: 4. Create conversation thread and print welcome message
        # thread = agent_client.threads.create()
        # print(f"Welcome! You're chatting with: {agent.name} ({agent.id}}")
        # print("I can help you place a restaurant order. Just tell me what you'd like!")

        # Loop until the user types 'quit'
        while True:
            # Get input text
            user_prompt = input("Enter your order request (or type 'quit' to exit): ")
            if user_prompt.lower() == "quit":
                break
            if len(user_prompt) == 0:
                print("Please enter an order request.")
                continue

            # TODO: Send message to agent and get response
            # STUDENT TASK: 
            # message = agent_client.messages.create(thread_id=thread.id, role="user", content=user_prompt)
            # run = agent_client.runs.create_and_process(thread_id=thread.id, agent_id=agent.id)

            # TODO: Check run status and handle errors
            # STUDENT TASK: Add error handling
            # if run.status == "failed":
            #     print(f"Run failed: {run.last_error}")
                
            # TODO: Display the agent's response
            # STUDENT TASK: Get and show the latest agent message
            # last_msg = agent_client.messages.get_last_message_text_by_role(
            #     thread_id=thread.id, role=MessageRole.AGENT)
            # if last_msg:
            #     print(f"\n{agent.name}: {last_msg.text.value}\n")

        # TODO: Show conversation history
        # STUDENT TASK: Display complete conversation log
        # print("\n" + "="*50)
        # print("CONVERSATION HISTORY") 
        # print("="*50)
        # messages = agent_client.messages.list(thread_id=thread.id, order=ListSortOrder.ASCENDING)
        # for message in messages:
        #     if message.text_messages:
        #         last_msg = message.text_messages[-1]
        #         role_name = "Customer" if message.role == "user" else agent.name
        #         print(f"{role_name}: {last_msg.text.value}\n")

        # TODO: Clean up resources
        # STUDENT TASK: Delete agent and confirm cleanup
        # agent_client.delete_agent(agent.id)
        # print(f"Thank you for using {agent.name}! Agent resources have been cleaned up.")



if __name__ == '__main__': 
    main()