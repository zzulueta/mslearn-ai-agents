import os
from dotenv import load_dotenv
from typing import Any
from pathlib import Path


# Add references
from azure.identity import DefaultAzureCredential
from azure.ai.agents import AgentsClient
from azure.ai.agents.models import FunctionTool, ToolSet, ListSortOrder, MessageRole, FilePurpose
from user_functions import user_functions

def main(): 

    # Clear the console
    os.system('cls' if os.name=='nt' else 'clear')

    # Load environment variables from .env file
    load_dotenv()
    project_endpoint= os.getenv("PROJECT_ENDPOINT")
    model_deployment = os.getenv("MODEL_DEPLOYMENT_NAME")

    # Display the URLs to be analyzed
    script_dir = Path(__file__).parent  # Get the directory of the script
    file_path = script_dir / 'url.txt'

    with file_path.open('r') as file:
        data = file.read() + "\n"
        print(data)

    # Connect to the Agent client
    agent_client = AgentsClient(
        endpoint=project_endpoint,
        credential=DefaultAzureCredential
            (exclude_environment_credential=True,
                exclude_managed_identity_credential=True)
    )
    
    # Define an agent that can use the custom functions
    with agent_client:

        functions = FunctionTool(user_functions)
        toolset = ToolSet()
        toolset.add(functions)
        agent_client.enable_auto_function_calls(toolset)
            
        instructions = f"""Given a subject matter and a list of URLs, fetch the content of the provided web page and extract all visible text. 
            Search through the extracted content to find information relevant to the specified subject matter. 
            Return a concise summary or the most relevant text related to the subject, including the source URL. 
            Ignore advertisements, navigation menus, and unrelated content. 
            If the subject matter is not found, respond with an appropriate message. 
            Handle errors gracefully, such as invalid URLs, network issues, or missing content.

            List of URLs to analyze:
            {data}
            """

        agent = agent_client.create_agent(
            model=model_deployment,
            name="webscraper-agent",
            instructions=instructions,
            toolset=toolset
        )

        thread = agent_client.threads.create()
        print(f"You're chatting with: {agent.name} ({agent.id})")

    
        # Loop until the user types 'quit'
        while True:
            # Get input text
            user_prompt = input("Enter a prompt (or type 'quit' to exit): ")
            if user_prompt.lower() == "quit":
                break
            if len(user_prompt) == 0:
                print("Please enter a prompt.")
                continue

            # Send a prompt to the agent
            message = agent_client.messages.create(
                thread_id=thread.id,
                role="user",
                content=user_prompt
            )
            run = agent_client.runs.create_and_process(thread_id=thread.id, agent_id=agent.id)


            # Check the run status for failures
            if run.status == "failed":
                print(f"Run failed: {run.last_error}")

                
            # Show the latest response from the agent
            last_msg = agent_client.messages.get_last_message_text_by_role(
                thread_id=thread.id,
                role=MessageRole.AGENT,
            )
            if last_msg:
                print(f"Last Message: {last_msg.text.value}")


        # Get the conversation history
        print("\nConversation Log:\n")
        messages = agent_client.messages.list(thread_id=thread.id, order=ListSortOrder.ASCENDING)
        for message in messages:
            if message.text_messages:
                last_msg = message.text_messages[-1]
                print(f"{message.role}: {last_msg.text.value}\n")


        # Clean up
        agent_client.delete_agent(agent.id)
        print("Deleted agent")

    



if __name__ == '__main__': 
    main()
