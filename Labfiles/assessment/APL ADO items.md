# Azure DevOps Work Items - Restaurant Order AI Agent

## Sprint Backlog - AI Agent Development Tasks

The following Azure DevOps work items have been assigned to you for the current sprint. These tasks involve implementing a restaurant order management AI agent using Azure AI Foundry and custom function tools.

---

### 🎯 **Epic: Restaurant Order Management AI Agent**
**Epic ID:** EPIC-2024-001  
**Assigned to:** Developer Team  
**Sprint:** Sprint 15  
**Priority:** High  

**Epic Description:**  
Develop an intelligent restaurant order management system using Azure AI agents that can interact with customers, process orders, calculate totals, and generate order receipts through natural language conversations.

---

### 📋 **Work Items:**

#### **User Story #1 - Azure AI Agent Infrastructure Setup**
**Work Item ID:** PBI-2024-045  
**Type:** Product Backlog Item  
**Assigned to:** You  
**Story Points:** 5  
**Priority:** 1  

**User Story:**  
As a developer, I need to set up the Azure AI Foundry infrastructure and establish connectivity so that I can build AI agents with custom function capabilities.

**Acceptance Criteria:**
- ✅ Azure AI Foundry project created with GPT-4o model deployment
- ✅ Project endpoint configured in environment variables  
- ✅ Azure authentication established using DefaultAzureCredential
- ✅ AgentsClient connection tested and verified

**Definition of Done:**
- Code successfully connects to Azure AI Foundry
- Authentication works without errors
- Environment configuration is properly set up

---

#### **Task #1 - Implement Order Processing Functions**
**Work Item ID:** TASK-2024-156  
**Type:** Task  
**Parent:** PBI-2024-045  
**Assigned to:** You  
**Remaining Work:** 4 hours  

**Task Description:**  
Implement custom Python functions for restaurant order processing that can be called by the AI agent.

**Technical Requirements:**
- Create `calculate_order_total()` function with menu pricing logic
- Implement `process_restaurant_order()` function for order workflow
- Functions must return JSON-formatted responses
- Include proper error handling for invalid menu items
- Generate unique order numbers using UUID

**Acceptance Criteria:**
- Functions accept correct parameters (customer info, items list)
- Order total calculations are mathematically correct
- Order files are saved to local filesystem
- Functions return proper JSON responses for agent consumption

---

#### **Task #2 - Configure AI Agent with Function Tools**
**Work Item ID:** TASK-2024-157  
**Type:** Task  
**Parent:** PBI-2024-045  
**Assigned to:** You  
**Remaining Work:** 3 hours  

**Task Description:**  
Configure Azure AI agent to discover and utilize custom functions as tools during conversations.

**Technical Requirements:**
- Import necessary Azure AI SDK classes (FunctionTool, ToolSet, etc.)
- Create FunctionTool from user-defined functions
- Configure ToolSet and enable auto function calls
- Write agent instructions for restaurant order context
- Set up conversation thread management

**Acceptance Criteria:**
- Agent automatically discovers available functions
- Agent chooses appropriate functions based on conversation context
- Function calls execute successfully during agent interactions
- Agent provides meaningful responses after function execution

---

#### **Bug #1 - Agent Response Threading Issue**
**Work Item ID:** BUG-2024-089  
**Type:** Bug  
**Assigned to:** You  
**Priority:** 2  
**Severity:** Medium  

**Bug Description:**  
During testing, the agent conversation thread sometimes loses context between messages, causing the agent to ask for information already provided by the customer.

**Steps to Reproduce:**
1. Start conversation with agent
2. Provide customer name and phone number
3. Add items to order
4. Agent asks for customer details again

**Expected Behavior:**  
Agent should maintain conversation state and remember previously provided information throughout the session.

**Acceptance Criteria:**
- Conversation thread maintains state across all interactions
- Agent doesn't repeat requests for already provided information
- Full conversation history is preserved and accessible

---

#### **Task #3 - Implement Error Handling and Cleanup**
**Work Item ID:** TASK-2024-158  
**Type:** Task  
**Parent:** PBI-2024-045  
**Assigned to:** You  
**Remaining Work:** 2 hours  

**Task Description:**  
Add comprehensive error handling and resource cleanup to ensure robust agent operation.

**Technical Requirements:**
- Check run status for failures and display error messages
- Implement proper agent and thread cleanup
- Add input validation for user prompts
- Handle menu item not found scenarios gracefully

**Acceptance Criteria:**
- Failed runs display meaningful error messages
- Agent and thread resources are properly deleted after use
- Invalid menu items are handled without crashing
- Empty user inputs are validated and handled appropriately

---

#### **User Story #2 - Conversation History and Logging**
**Work Item ID:** PBI-2024-046  
**Type:** Product Backlog Item  
**Assigned to:** You  
**Story Points:** 3  
**Priority:** 2  

**User Story:**  
As a restaurant manager, I need to see the full conversation history between the agent and customers so that I can review order interactions and improve service quality.

**Acceptance Criteria:**
- ✅ Complete conversation log displayed at end of session
- ✅ Messages shown in chronological order
- ✅ Clear distinction between customer and agent messages
- ✅ Conversation history includes all function call results

**Definition of Done:**
- Conversation history is properly formatted and readable
- All message types (user, agent, function results) are captured
- History display works consistently across different conversation lengths

---

### 🚀 **Sprint Goals:**
1. Complete all assigned work items by end of sprint
2. Ensure 95% code coverage with unit tests
3. All acceptance criteria met and validated
4. Code reviewed and approved by senior developer
5. Deploy to development environment for QA testing

### 📝 **Notes:**
- Use the provided `app_end.py` and `user_functions_end.py` files as reference implementations
- Follow team coding standards and Azure best practices
- Document any assumptions or design decisions in code comments
- Update work item status in Azure DevOps as you progress

## Create an Azure AI Foundry project

Let's start by creating an Azure AI Foundry project for our restaurant order agent.

1. In a web browser, open the [Azure AI Foundry portal](https://ai.azure.com) at `https://ai.azure.com` and sign in using your Azure credentials. Close any tips or quick start panes that are opened the first time you sign in, and if necessary use the **Azure AI Foundry** logo at the top left to navigate to the home page.

2. In the home page, select **Create an agent**.

3. When prompted to create a project, enter a valid name for your project and expand **Advanced options**.

4. Confirm the following settings for your project:
    - **Azure AI Foundry resource**: *A valid name for your Azure AI Foundry resource*
    - **Subscription**: *Your Azure subscription*
    - **Resource group**: *Create or select a resource group*
    - **Region**: *Select any **AI Foundry recommended***\*

    > \* Some Azure AI resources are constrained by regional model quotas. In the event of a quota limit being exceeded later in the exercise, there's a possibility you may need to create another resource in a different region.

5. Select **Create** and wait for your project to be created.

6. If prompted, deploy a **gpt-4o** model using either the *Global Standard* or *Standard* deployment option (depending on your quota availability).

    >**Note**: If quota is available, a GPT-4o base model may be deployed automatically when creating your Agent and project.

7. When your project is created, the Agents playground will be opened.

8. In the navigation pane on the left, select **Overview** to see the main page for your project.

9. Copy the **Azure AI Foundry project endpoint** values to a notepad, as you'll use them to connect to your project in a client application.

## Develop a restaurant order agent with function tools

Now let's develop an application that implements a restaurant order agent using custom function tools.

### Clone and setup the lab files

1. Open a new browser tab (keeping the Azure AI Foundry portal open in the existing tab). Then in the new tab, browse to the [Azure portal](https://portal.azure.com) at `https://portal.azure.com`; signing in with your Azure credentials if prompted.

2. Use the **[\>_]** button to the right of the search bar at the top of the page to create a new Cloud Shell in the Azure portal, selecting a ***PowerShell*** environment.

3. In the cloud shell pane, navigate to the lab files directory:

    ```
    cd ai-agents/Labfiles/03b-restaurant-order-agent/Python
    ls -a -l
    ```

    The provided files include application templates and configuration files that you'll complete.

### Configure the application settings

1. In the cloud shell command-line pane, enter the following command to install the libraries you'll use:

    ```
    python -m venv labenv
    ./labenv/bin/Activate.ps1
    pip install -r requirements.txt
    ```

    >**Note:** You can ignore any warning or error messages displayed during the library installation.

2. Enter the following command to edit the configuration file:

    ```
    code .env
    ```

3. Replace the **your_project_endpoint** placeholder with the endpoint for your project (copied from the project **Overview** page in the Azure AI Foundry portal) and ensure that the MODEL_DEPLOYMENT_NAME variable is set to your model deployment name (which should be *gpt-4o*).

4. Save your changes (**CTRL+S**) and close the code editor (**CTRL+Q**).

### Define custom functions for restaurant orders

1. Enter the following command to edit the function code file:

    ```
    code user_functions.py
    ```

2. **STUDENT TASK**: Find the comment **TODO: Create a function to calculate order total** and implement the `calculate_order_total` function. This function should:
   - Take a list of menu items as a parameter
   - Calculate the total cost using the provided MENU_ITEMS dictionary
   - Return a JSON string with the total amount and itemized breakdown

    **Expected Implementation**:
    ```python
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
    ```

3. **STUDENT TASK**: Find the comment **TODO: Create a function to process a restaurant order** and implement the `process_restaurant_order` function. This function should:
   - Take customer_name, phone_number, and items as parameters
   - Generate a unique order number using uuid
   - Calculate the total using your calculate_order_total function
   - Save the order details to a text file
   - Return a JSON confirmation message

    **Expected Implementation**:
    ```python
    def process_restaurant_order(customer_name: str, phone_number: str, items: list) -> str:
        script_dir = Path(__file__).parent
        order_number = str(uuid.uuid4()).replace('-', '')[:8]
        file_name = f"order-{order_number}.txt"
        file_path = script_dir / file_name
        
        # Calculate total
        order_calc = json.loads(calculate_order_total(items))
        
        # Create order text
        order_text = f"Restaurant Order: {order_number}\\n"
        order_text += f"Customer: {customer_name}\\n"
        order_text += f"Phone: {phone_number}\\n"
        order_text += f"Items ordered:\\n"
        
        for item in order_calc['items']:
            order_text += f"  - {item['item']}: ${item['price']:.2f}\\n"
        
        order_text += f"\\nTotal: ${order_calc['total']:.2f}\\n"
        order_text += f"Order placed at: {Path(__file__).parent}"
        
        # Save order
        file_path.write_text(order_text)
        
        message = {
            "message": f"Order {order_number} processed successfully! Total: ${order_calc['total']:.2f}. Order saved as {file_name}",
            "order_number": order_number,
            "total": order_calc['total']
        }
        return json.dumps(message)
    ```

4. **STUDENT TASK**: Find the comment **TODO: Define a set of callable functions** and create the user_functions set:

    **Expected Implementation**:
    ```python
    user_functions: Set[Callable[..., Any]] = {
        calculate_order_total,
        process_restaurant_order
    }
    ```

5. Save the file (**CTRL+S**).

### Implement the restaurant order agent

1. Enter the following command to edit the agent code:

    ```
    code agent.py
    ```

2. **STUDENT TASK**: Find the comment **TODO: Add references** and add the necessary imports:

    **Expected Implementation**:
    ```python
    from azure.identity import DefaultAzureCredential
    from azure.ai.agents import AgentsClient
    from azure.ai.agents.models import FunctionTool, ToolSet, ListSortOrder, MessageRole
    from user_functions import user_functions
    ```

3. **STUDENT TASK**: Find the comment **TODO: Connect to the Agent client** and create the Azure connection:

    **Expected Implementation**:
    ```python
    agent_client = AgentsClient(
        endpoint=project_endpoint,
        credential=DefaultAzureCredential(
            exclude_environment_credential=True,
            exclude_managed_identity_credential=True)
    )
    ```

4. **STUDENT TASK**: Find the comment **TODO: Define an agent that can use the custom functions** and implement the agent setup:

    **Expected Implementation**:
    ```python
    with agent_client:
        # Create function tools
        functions = FunctionTool(user_functions)
        toolset = ToolSet()
        toolset.add(functions)
        agent_client.enable_auto_function_calls(toolset)
        
        # Create the restaurant order agent
        agent = agent_client.create_agent(
            model=model_deployment,
            name="restaurant-order-agent",
            instructions=\"\"\"You are a helpful restaurant order-taking agent.
                            When a customer wants to place an order, collect their name, phone number, and the items they want to order.
                            Use the available functions to calculate totals and process their order.
                            Our menu includes: burger ($12.99), pizza ($15.99), pasta ($13.49), salad ($9.99), 
                            sandwich ($8.99), fries ($4.99), soda ($2.99), coffee ($3.49), dessert ($6.99).
                            Always be friendly and helpful!\"\"\",
            toolset=toolset
        )
        
        # Create conversation thread
        thread = agent_client.threads.create()
        print(f"Welcome! You're chatting with: {agent.name} ({agent.id})")
        print("I can help you place a restaurant order. Just tell me what you'd like!")
    ```

5. **STUDENT TASK**: Find the comment **TODO: Send a prompt to the agent** and implement message handling:

    **Expected Implementation**:
    ```python
    message = agent_client.messages.create(
        thread_id=thread.id,
        role="user",
        content=user_prompt
    )
    run = agent_client.runs.create_and_process(thread_id=thread.id, agent_id=agent.id)
    ```

6. **STUDENT TASK**: Find the comment **TODO: Check the run status for failures** and add error handling:

    **Expected Implementation**:
    ```python
    if run.status == "failed":
        print(f"Run failed: {run.last_error}")
    ```

7. **STUDENT TASK**: Find the comment **TODO: Show the latest response from the agent** and display the response:

    **Expected Implementation**:
    ```python
    last_msg = agent_client.messages.get_last_message_text_by_role(
        thread_id=thread.id,
        role=MessageRole.AGENT,
    )
    if last_msg:
        print(f"\\n{agent.name}: {last_msg.text.value}\\n")
    ```

8. **STUDENT TASK**: Find the comment **TODO: Get the conversation history** and implement conversation logging:

    **Expected Implementation**:
    ```python
    print("\\n" + "="*50)
    print("CONVERSATION HISTORY")
    print("="*50)
    messages = agent_client.messages.list(thread_id=thread.id, order=ListSortOrder.ASCENDING)
    for message in messages:
        if message.text_messages:
            last_msg = message.text_messages[-1]
            role_name = "Customer" if message.role == "user" else agent.name
            print(f"{role_name}: {last_msg.text.value}\\n")
    ```

9. **STUDENT TASK**: Find the comment **TODO: Clean up** and implement cleanup:

    **Expected Implementation**:
    ```python
    agent_client.delete_agent(agent.id)
    print(f"Thank you for using {agent.name}! Agent resources have been cleaned up.")
    ```

10. Save the code file (**CTRL+S**) when you have finished.

### Test your restaurant order agent

1. Sign into Azure in the cloud shell:

    ```
    az login
    ```

2. After signing in, run your restaurant order agent:

    ```
    python agent.py
    ```

3. Test the agent with prompts like:
   - "I'd like to place an order"
   - "I want a burger and fries, my name is John Smith and my phone is 555-1234"
   - "Can you calculate the total for pizza and soda?"

4. The agent should collect your information and use your custom functions to process orders and calculate totals.

5. Type `quit` when you're done testing.

6. Check that order files were created:

    ```
    ls order-*.txt
    cat order-*.txt
    ```

## Key Learning Points

This lab demonstrates several important concepts:

1. **Custom Function Definition**: How to create Python functions that AI agents can discover and use
2. **Function Tool Integration**: Using `FunctionTool` and `ToolSet` to make functions available to agents
3. **Agent Instructions**: Writing clear instructions that guide when and how to use functions
4. **Automatic Function Discovery**: How agents automatically choose appropriate functions based on context
5. **Stateful Conversations**: Managing conversation threads that maintain context across interactions

## Validation Checklist

Students should be able to demonstrate:
- ✅ Functions are properly defined with correct parameters and return types
- ✅ Agent successfully connects to Azure AI Foundry
- ✅ Agent can discover and call custom functions automatically
- ✅ Order processing works correctly with file generation
- ✅ Conversation state is maintained throughout the interaction
- ✅ Error handling and cleanup are implemented properly

## Clean up

When finished, delete the Azure resources to avoid unnecessary costs:

1. Open the [Azure portal](https://portal.azure.com)
2. Navigate to your resource group
3. Select **Delete resource group**
4. Enter the resource group name to confirm deletion