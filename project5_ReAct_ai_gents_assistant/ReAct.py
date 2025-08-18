#!/usr/bin/env python
# coding: utf-8

# <p style="text-align:center">
#     <a href="https://skills.network" target="_blank">
#     <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/assets/logos/SN_web_lightmode.png" width="200" alt="Skills Network Logo"  />
#     </a>
# </p>
# 

# # **ReAct: Build Reasoning and Acting AI Agents with LangGraph**
# 

# Estimated time needed: **90** minutes
# 

# You're a software engineer on a mission: build an AI agent that doesn't just respond—it thinks. In this lab, you'll step into the role of an AI architect, designing a smart assistant that solves tough problems by reasoning through them and taking purposeful actions.
# 
# Using the ReAct (Reasoning + Acting) framework, you'll teach your agent to think step by step, consult tools like search engines or calculators, and adapt on the fly. It’s not just about answers—it’s about how the agent gets there.
# 
# By the end of the lab, your AI will face a mystery that can’t be solved with knowledge alone. It will need logic, resourcefulness, and the ability to act—just like you, the engineer who built it.
# 
# ## What is ReAct?
# 
# **ReAct** stands for **Reasoning + Acting**. It's a framework that combines:
# 
# 1. **Reasoning**: The agent thinks through problems step by step, maintaining an internal dialogue about what it needs to do.
# 2. **Acting**: The agent can use external tools (search engines, calculators, APIs) to gather information or perform actions.
# 3. **Observing**: The agent processes the results from its actions and incorporates them into its reasoning.
# 
# This creates a powerful loop: **Think → Act → Observe → Think → Act → ...**
# 
# ### Why ReAct Matters
# 
# Traditional language models are limited by their training data cutoff and can't access real-time information. ReAct agents overcome this by:
# - Accessing current information through web searches
# - Performing calculations with specialized tools
# - Breaking down complex problems into manageable steps
# - Adapting their approach based on intermediate results
# 

# ## __Table of Contents__
# 
# <ol>
#     <li><a href="#Objectives">Objectives</a></li>
#     <li>
#         <a href="#Setup-&-Installation">Setup & Installation</a>
#         <ol>
#             <li><a href="#Installing-Required-Libraries">Installing Required Libraries</a></li>
#             <li><a href="#Importing-Required-Libraries">Importing Required Libraries</a></li>
#         </ol>
#     </li>
#     <li>
#         <a href="#Understanding-Tools-in-ReAct">Understanding Tools in ReAct</a>
#         <ol>
#             <li><a href="#1.-Web-Search-Tool">1. Web Search Tool</a></li>
#             <li><a href="#Theory-behind-Web-Search-Tools">Theory behind Web Search Tools</a></li>
#             <li><a href="#Testing-the-Search-Tool">Testing the Search Tool</a></li>
#             <li><a href="#2.-Clothing-Recommendation-Tool">2. Clothing Recommendation Tool</a></li>
#             <li><a href="#Why-this-Tool-Matters">Why this Tool Matters</a></li>
#             <li><a href="#Creating-the-tool-Registry">Creating the tool Registry</a></li>
#         </ol>
#     </li>
#     <li>
#         <a href="#Setting-up-the-Language-Model">Setting up the Language Model</a>
#         <ol>
#             <li><a href="#Initializing-the-AI-Model">Initializing the AI Model</a></li>
#             <li><a href="#Creating-the-System-Prompt">Creating the System Prompt</a></li>
#             <li><a href="#The-System-Prompt's-Role">The System Prompt's Role</a></li>
#             <li><a href="#Binding-Tools-to-the-Model">Binding Tools to the Model</a></li>
#             <li>
#                 <a href="#Understanding-Agent-State">Understanding Agent State</a>
#                 <ol>
#                     <li><a href="#What-is-Agent-State?">What is Agent State?</a></li>
#                     <li><a href="#Demonstrating-State-Management">Demonstrating State Management</a></li>
#                 </ol>
#             </li>
#             <li>
#                 <a href="#Manual-ReAct-Execution-(Understanding-the-Flow)">Manual ReAct Execution (Understanding the Flow)</a>
#                 <ol>
#                     <li><a href="#Step-1:-Initial-Query-Processing">Step 1: Initial Query Processing</a></li>
#                     <li><a href="#Step-2:-Tool-Execution">Step 2: Tool Execution</a></li>
#                     <li><a href="#Step-3:-Processing-Results-and-Next-Action">Step 3: Processing Results and Next Action</a></li>
#                     <li><a href="#Step-4:-Final-Response-Generation">Step 4: Final Response Generation</a></li>
#                 </ol>
#             </li>
#             <li>
#                 <a href="#Automating-ReAct-with-Graphs">Automating ReAct with Graphs</a>
#                 <ol>
#                     <li><a href="#Why-Use-Graphs?">Why Use Graphs?</a></li>
#                     <li><a href="#Building-the-Core-Functions">Building the Core Functions</a></li>
#                     <li><a href="#Constructing-the-State-Graph">Constructing the State Graph</a></li>
#                     <li><a href="#Visualizing-the-Graph">Visualizing the Graph</a></li>
#                 </ol>
#             </li>
#             <li>
#                 <a href="#Running-the-Complete-ReAct-Agent">Running the Complete ReAct Agent</a>
#                 <ol>
#                     <li><a href="#Final-Execution">Final Execution</a></li>
#                     <li><a href="#The-Complete-ReAct-Cycle">The Complete ReAct Cycle</a></li>
#                 </ol>
#             </li>
#         </ol>
#     </li>
#     <li>
#         <a href="#Key-Takeaways">Key Takeaways</a>
#         <ol>
#             <li><a href="#What-Makes-ReAct-Powerful">What Makes ReAct Powerful</a></li>
#             <li><a href="#Best-Practices">Best Practices</a></li>
#         </ol>
#     </li>
#     <li>
#         <a href="#Exercises">Exercises</a>
#         <ol>
#             <li><a href="#Exercise-1---Build-a-Calculator-Tool">Exercise 1 - Build a Calculator Tool</a></li>
#             <li><a href="#Exercise-2---Create-a-News-Summary-Tool">Exercise 2 - Create a News Summary Tool</a></li>
#         </ol>
#     </li>
#     <li><a href="#Testing-Your-Solutions">Testing Your Solutions</a></li>
#     <li><a href="#Authors">Authors</a></li>
# </ol>
# 

# ## Objectives
# 
# After completing this lab you will be able to:
# 
#  - Use the ReAct framework to solve multi-step problems with external tools
#  - Teach an AI agent to reason step by step, take actions, and adapt based on results
#  - Build a smart assistant that can handle tasks requiring logic and tool use
# 

# ----
# 

# ## Setup & Installation
# 

# For this lab, we will be using the following libraries:
# 
# 
# - [`LangGraph`](https://www.langchain.com/langgraph): A framework for building stateful, multi-step AI applications using graphs.
# - [`LangChain`](https://www.langchain.com/): A toolkit that provides tools and abstractions for working with language models.
# - [`LangChain-OpenAI`](https://python.langchain.com/docs/integrations/llms/openai/): OpenAI integration for LangChain.
# - [`LangChain-Community`](https://python.langchain.com/api_reference/community/index.html): Community-contributed tools and integrations.
# 

# ### Installing Required Libraries
# 

# In[1]:


get_ipython().system('pip install -U langgraph langchain-openai')


# In[2]:


get_ipython().run_cell_magic('capture', '', '!pip install langgraph==0.3.34 langchain-openai==0.3.14 langchainhub==0.1.21 langchain==0.3.24 pygraphviz==1.14 langchain-community==0.3.23\n')


# ### Understanding Tools in ReAct
# 
# Tools are the "acting" part of ReAct. They give the agent capabilities beyond just generating text. Let's build two essential tools:
# 
# #### 1. Web Search Tool
# ### Tavily Search API Key Setup
# 
# We'll use Tavily search as our external research tool. You can get an API key at https://app.tavily.com/sign-in   
# 
# 
# **Disclaimer:** Signing up for Tavily provides you with free credits, more than enough for this project's needs. If you require additional credits for further use, please add them at your own discretion.
# 
# ![image.png](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/UjJx1-0vss4_3lwsUF8n0w/image.png)
# 
# You need to copy the key from Tavily's API website and paste the key on the line ```os.environ["TAVILY_API_KEY"] = "YOUR_KEY_HERE"```
# 

# In[3]:


import warnings 
warnings.filterwarnings('ignore')

from langchain_community.tools.tavily_search import TavilySearchResults
from langchain.tools import tool
import os
import json

os.environ["TAVILY_API_KEY"] = "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"

# Initialize the Tavily search tool
search = TavilySearchResults()

@tool
def search_tool(query: str):
    """
    Search the web for information using Tavily API.

    :param query: The search query string
    :return: Search results related to the query
    """
    return search.invoke(query)


# ### Theory behind Web Search Tools:
# - Enable real-time information retrieval
# - Overcome the knowledge cutoff limitation of language models
# - Return structured data that the agent can process and reason about
# 
# ### Testing the Search Tool
# 

# In[4]:


search_tool("What's the weather like in Tokyo today?")


# This test demonstrates how the agent can access current information that wasn't available during training.
# 
# #### 2. Clothing Recommendation Tool
# 

# In[5]:


@tool
def recommend_clothing(weather: str) -> str:
    """
    Returns a clothing recommendation based on the provided weather description.

    This function examines the input string for specific keywords or temperature indicators 
    (e.g., "snow", "freezing", "rain", "85°F") to suggest appropriate attire. It handles 
    common weather conditions like snow, rain, heat, and cold by providing simple and practical 
    clothing advice.

    :param weather: A brief description of the weather (e.g., "Overcast, 64.9°F")
    :return: A string with clothing recommendations suitable for the weather
    """
    weather = weather.lower()
    if "snow" in weather or "freezing" in weather:
        return "Wear a heavy coat, gloves, and boots."
    elif "rain" in weather or "wet" in weather:
        return "Bring a raincoat and waterproof shoes."
    elif "hot" in weather or "85" in weather:
        return "T-shirt, shorts, and sunscreen recommended."
    elif "cold" in weather or "50" in weather:
        return "Wear a warm jacket or sweater."
    else:
        return "A light jacket should be fine."


# **Why this Tool Matters:**
# - Demonstrates domain-specific reasoning
# - Shows how tools can process and interpret data from other tools
# - Illustrates the composability of ReAct systems
# 
# #### Creating the Tool Registry
# 

# In[6]:


tools=[search_tool,recommend_clothing]

tools_by_name={ tool.name:tool for tool in tools}


# This registry allows the agent to dynamically select and invoke the appropriate tool based on the task at hand.
# 
# ## Setting Up the Language Model
# 
# ### Initializing the AI Model
# 

# In[7]:


from langchain_openai import ChatOpenAI
from langchain_core.tools import tool

model = ChatOpenAI(model="gpt-4o-mini")


# We're using GPT-4o-mini as our reasoning engine. This model will:
# - Analyze user queries
# - Decide which tools to use
# - Process tool results
# - Generate final responses
# 
# ### Creating the System Prompt
# 

# In[8]:


from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import BaseMessage, HumanMessage, AIMessage, ToolMessage,SystemMessage

chat_prompt = ChatPromptTemplate.from_messages([
    ("system", """
You are a helpful AI assistant that thinks step-by-step and uses tools when needed.

When responding to queries:
1. First, think about what information you need
2. Use available tools if you need current data or specific capabilities  
3. Provide clear, helpful responses based on your reasoning and any tool results

Always explain your thinking process to help users understand your approach.
"""),
    MessagesPlaceholder(variable_name="scratch_pad")
])


# **The System Prompt's Role:**
# - Defines the agent's behavior and personality
# - Establishes the reasoning pattern (think → act → observe)
# - Encourages transparency in the decision-making process
# 
# ### Binding Tools to the Model
# 

# In[9]:


model_react=chat_prompt|model.bind_tools(tools)


# This creates a model that can:
# - Understand when to use tools
# - Generate properly formatted tool calls
# - Process tool results in context
# 
# ## Understanding Agent State
# 
# ### What is Agent State?
# 
# In ReAct, state management is crucial, as the agent must maintain context across multiple reasoning and acting steps.
# 

# In[10]:


from typing import (Annotated,Sequence,TypedDict)
from langchain_core.messages import BaseMessage
from langgraph.graph.message import add_messages

class AgentState(TypedDict):
    """The state of the agent."""

    # add_messages is a reducer
    # See https://langchain-ai.github.io/langgraph/concepts/low_level/#reducers
    messages: Annotated[Sequence[BaseMessage], add_messages]


# **Key Concepts:**
# - **State**: Contains the conversation history and context.
# - **Reducer**: `add_messages` automatically handles adding new messages to the conversation.
# - **Type Safety**: TypedDict ensures our state structure is well-defined.
# 
# ### Demonstrating State Management
# 

# In[11]:


# Example conversation flow:
state: AgentState = {"messages": []}

# append a message using the reducer properly
state["messages"] = add_messages(state["messages"], [HumanMessage(content="Hi")])
print("After greeting:", state["messages"])

# add another message (e.g. a question)
state["messages"] = add_messages(state["messages"], [HumanMessage(content="Weather in NYC?")])
print("After question:", state)


# This demonstrates how the state accumulates context over the conversation.
# 

# ## Manual ReAct Execution (Understanding the Flow)
# 
# Before building the automated graph, let's manually step through a ReAct cycle to understand what happens:
# 
# ### Step 1: Initial Query Processing
# 

# In[12]:


dummy_state: AgentState = {
    "messages": [HumanMessage( "What's the weather like in Zurich, and what should I wear based on the temperature?")]}

response = model_react.invoke({"scratch_pad":dummy_state["messages"]})

dummy_state["messages"]=add_messages(dummy_state["messages"],[response])


# **What Happens Here:**
# 1. The user asks a complex question requiring current data.
# 2. The model analyzes the query and realizes it needs to search for weather information.
# 3. The model generates a tool call for the search.
# 

# ### Step 2: Tool Execution
# 

# In[13]:


tool_call = response.tool_calls[-1]
print("Tool call:", tool_call)

tool_result = tools_by_name[tool_call["name"]].invoke(tool_call["args"])
print("Tool result preview:", tool_result[0]['title'])

tool_message = ToolMessage(
    content=json.dumps(tool_result),
    name=tool_call["name"],
    tool_call_id=tool_call["id"]
)
dummy_state["messages"] = add_messages(dummy_state["messages"], [tool_message])


# **What Happens Here:**
# 1. Extract the tool call from the model's response.
# 2. Execute the tool using the specified arguments.
# 3. Create a ToolMessage containing the results.
# 4. Add the tool result to the conversation state.
# 

# ### Step 3: Processing Results and Next Action
# 

# In[14]:


response = model_react.invoke({"scratch_pad": dummy_state["messages"]})
dummy_state['messages'] = add_messages(dummy_state['messages'], [response])

# check if the model wants to use another tool
if response.tool_calls:
    tool_call = response.tool_calls[0]
    tool_result = tools_by_name[tool_call["name"]].invoke(tool_call["args"])
    tool_message = ToolMessage(
        content=json.dumps(tool_result),
        name=tool_call["name"],
        tool_call_id=tool_call["id"]
    )
    dummy_state['messages'] = add_messages(dummy_state['messages'], [tool_message])


# **What Happens Here:**
# 1. The model processes the search results.
# 2. It realizes it needs to use the clothing recommendation tool.
# 3. It extracts weather information and calls the clothing tool.
# 4. It receives clothing recommendations based on the weather data.
# 

# ### Step 4: Final Response Generation
# 

# In[15]:


response = model_react.invoke({"scratch_pad": dummy_state["messages"]})
print("Final response generated:", response.content is not None)
print("More tools needed:", bool(response.tool_calls))


# **What Happens Here:**
# 1. The model has all necessary information.
# 2. It synthesizes weather data and clothing recommendations.
# 3. It generates a comprehensive response to the user.
# 4. No more tool calls needed—the reasoning cycle is complete.
# 

# ## Automating ReAct with Graphs
# 
# ### Why Use Graphs?
# 
# Manual ReAct execution is educational but impractical for real applications. LangGraph automates this process with a state machine that handles the reasoning loop automatically.
# 
# ### Building the Core Functions
# 
# #### Tool Execution Node
# 

# In[16]:


def tool_node(state: AgentState):
    """Execute all tool calls from the last message in the state."""
    outputs = []
    for tool_call in state["messages"][-1].tool_calls:
        tool_result = tools_by_name[tool_call["name"]].invoke(tool_call["args"])
        outputs.append(
            ToolMessage(
                content=json.dumps(tool_result),
                name=tool_call["name"],
                tool_call_id=tool_call["id"],
            )
        )
    return {"messages": outputs}


# **Function Purpose:**
# - Automatically execute all tool calls from the model
# - Handle multiple simultaneous tool calls
# - Return properly formatted tool messages
# 

# #### Model Invocation Node
# 

# In[17]:


def call_model(state: AgentState):
    """Invoke the model with the current conversation state."""
    response = model_react.invoke({"scratch_pad": state["messages"]})
    return {"messages": [response]}


# **Function Purpose:**
# - Call the ReAct-enabled model
# - Pass the full conversation context
# - Return the model's response (which may include tool calls)
# 
# #### Decision Logic
# 

# In[18]:


def should_continue(state: AgentState):
    """Determine whether to continue with tool use or end the conversation."""
    messages = state["messages"]
    last_message = messages[-1]
    # If there is no function call, then we finish
    if not last_message.tool_calls:
        return "end"
    # Otherwise if there is, we continue
    else:
        return "continue"


# **Function Purpose:**
# - Implement the control flow logic
# - Decide whether the agent needs to use more tools
# - Route the conversation to either tool execution or completion
# 
# ### Constructing the State Graph
# 

# In[19]:


from langgraph.graph import StateGraph, END

# Define a new graph
workflow = StateGraph(AgentState)

# Define the two nodes we will cycle between
workflow.add_node("agent", call_model)
workflow.add_node("tools", tool_node)

# Add edges between nodes
workflow.add_edge("tools", "agent")  # After tools, always go back to agent

# Add conditional logic
workflow.add_conditional_edges(
    "agent",
    should_continue,
    {
        "continue": "tools",  # If tools needed, go to tools node
        "end": END,          # If done, end the conversation
    },
)

# Set entry point
workflow.set_entry_point("agent")

# Compile the graph
graph = workflow.compile()


# **Graph Structure Explained:**
# 1. **Agent Node**: Where reasoning happens and tool calls are generated.
# 2. **Tools Node**: Where tool execution occurs.
# 3. **Conditional Edge**: Determines whether to continue or finish.
# 4. **Entry Point**: Conversation always starts with the agent reasoning.
# ### Visualizing the Graph
# 

# In[20]:


from IPython.display import Image, display

try:
    display(Image(graph.get_graph().draw_mermaid_png()))
except Exception:
    # This requires some extra dependencies and is optional
    pass


# This visualization shows the flow: Agent → Decision → Tools → Agent → Decision → End
# 

# ## Running the Complete ReAct Agent
# 
# ### Final Execution
# 

# In[21]:


def print_stream(stream):
    """Helper function for formatting the stream nicely."""
    for s in stream:
        message = s["messages"][-1]
        if isinstance(message, tuple):
            print(message)
        else:
            message.pretty_print()

inputs = {"messages": [HumanMessage(content="What's the weather like in Zurich, and what should I wear based on the temperature?")]}

print_stream(graph.stream(inputs, stream_mode="values"))


# **What You'll See:**
# 1. **Initial Reasoning**: Agent analyzes the query.
# 2. **Tool Call 1**: Searches for Zurich weather.
# 3. **Tool Result Processing**: Agent examines weather data.
# 4. **Tool Call 2**: Gets clothing recommendations.
# 5. **Final Synthesis**: Agent combines all information into a helpful response.
# 

# ### The Complete ReAct Cycle
# 
# The final execution demonstrates the full ReAct pattern:
# 
# 1. **Reasoning**: "I need current weather data for Zurich".
# 2. **Acting**: Calls search_tool("Zurich weather today").
# 3. **Observing**: Processes search results, extracts temperature.
# 4. **Reasoning**: "Now I need clothing recommendations for this temperature".
# 5. **Acting**: Calls recommend_clothing("temperature from search").
# 6. **Observing**: Gets clothing suggestions.
# 7. **Reasoning**: "I can now provide a complete answer".
# 8. **Final Response**: Synthesizes weather info and clothing recommendations.
# 

# ## Key Takeaways
# 

# ### What Makes ReAct Powerful
# 
# 1. **Transparency**: You can see the agent's reasoning process.
# 2. **Adaptability**: The agent can handle unexpected results and change course.
# 3. **Extensibility**: It's easy to add new tools and capabilities.
# 4. **Reliability**: The structured approach reduces hallucination and improves accuracy
# 

# ### Best Practices
# 
# 1. **Tool Design**: Make tools focused and reliable.
# 2. **Error Handling**: Plan for tool failures and unexpected results.
# 3. **Context Management**: Keep state manageable and relevant.
# 4. **User Experience**: Provide clear feedback about what the agent is doing.
# 
# The ReAct framework represents a significant step toward more capable and trustworthy AI agents that can reason through complex problems and take meaningful actions in the real world.
# 

# # Exercises
# 
# Now it's time to put your ReAct knowledge into practice! These exercises will help you build your own tools and extend the agent's capabilities.
# 

# ## Exercise 1 - Build a Calculator Tool
# 
# **Objective:** Create a mathematical calculator tool that can handle complex calculations.
# 
# Your task is to create a calculator tool that can perform mathematical operations. This tool should be able to handle expressions like "2 + 3 * 4", "sqrt(16)", and "sin(π/2)".
# 
# ### Instructions:
# 1. Create a tool called `calculator_tool` using the `@tool` decorator.
# 2. The tool should accept a mathematical expression as a string.
# 3. Use Python's `eval()` function carefully (or better yet, use the `ast` module for safety).
# 4. Test your tool with various mathematical expressions.
# 5. Add your tool to the tools list and test it with the ReAct agent.
# 
# ### Starter Code:
# 

# In[22]:


import math
import ast
import operator

@tool
def calculator_tool(expression: str) -> str:
    """
    Safely evaluate mathematical expressions.
    
    :param expression: A mathematical expression as a string (e.g., "2 + 3 * 4")
    :return: The result of the calculation
    """
    # TODO: Implement safe mathematical evaluation
    # Hint: You can use ast.literal_eval for simple expressions
    # or create a safe evaluator for more complex math
    pass

# TODO: Add calculator_tool to your tools list
# TODO: Test with the agent: "What's 15% of 250 plus the square root of 144?"


# In[32]:


import math
import ast
import operator

# Safe mathematical operations mapping
SAFE_OPERATIONS = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.FloorDiv: operator.floordiv,
    ast.Mod: operator.mod,
    ast.Pow: operator.pow,
    ast.USub: operator.neg,
    ast.UAdd: operator.pos,
}

# Safe mathematical functions
SAFE_FUNCTIONS = {
    'abs': abs,
    'round': round,
    'min': min,
    'max': max,
    'sum': sum,
    'sqrt': math.sqrt,
    'sin': math.sin,
    'cos': math.cos,
    'tan': math.tan,
    'log': math.log,
    'log10': math.log10,
    'exp': math.exp,
    'ceil': math.ceil,
    'floor': math.floor,
    'pow': pow,
}

# Safe constants
SAFE_NAMES = {
    'pi': math.pi,
    'e': math.e,
}

def safe_eval_expression(node):
    """
    Safely evaluate an AST node representing a mathematical expression.
    """
    if isinstance(node, ast.Constant):  # Python 3.8+
        return node.value
    elif isinstance(node, ast.Num):  # Python < 3.8 compatibility
        return node.n
    elif isinstance(node, ast.Name):
        if node.id in SAFE_NAMES:
            return SAFE_NAMES[node.id]
        else:
            raise ValueError(f"Name '{node.id}' is not allowed")
    elif isinstance(node, ast.BinOp):
        left = safe_eval_expression(node.left)
        right = safe_eval_expression(node.right)
        op_type = type(node.op)
        if op_type in SAFE_OPERATIONS:
            if op_type == ast.Div and right == 0:
                raise ValueError("Division by zero")
            return SAFE_OPERATIONS[op_type](left, right)
        else:
            raise ValueError(f"Operation {op_type.__name__} is not allowed")
    elif isinstance(node, ast.UnaryOp):
        operand = safe_eval_expression(node.operand)
        op_type = type(node.op)
        if op_type in SAFE_OPERATIONS:
            return SAFE_OPERATIONS[op_type](operand)
        else:
            raise ValueError(f"Unary operation {op_type.__name__} is not allowed")
    elif isinstance(node, ast.Call):
        if isinstance(node.func, ast.Name) and node.func.id in SAFE_FUNCTIONS:
            args = [safe_eval_expression(arg) for arg in node.args]
            try:
                return SAFE_FUNCTIONS[node.func.id](*args)
            except (ValueError, TypeError, OverflowError) as e:
                raise ValueError(f"Error calling function {node.func.id}: {str(e)}")
        else:
            func_name = node.func.id if isinstance(node.func, ast.Name) else "unknown"
            raise ValueError(f"Function '{func_name}' is not allowed")
    elif isinstance(node, ast.Expression):
        return safe_eval_expression(node.body)
    else:
        raise ValueError(f"Node type {type(node).__name__} is not allowed")


# In[33]:


@tool
def calculator_tool(expression: str) -> str:
    """
    Safely evaluate mathematical expressions.
    
    :param expression: A mathematical expression as a string (e.g., "2 + 3 * 4")
    :return: The result of the calculation
    """
    try:
        # Remove whitespace and validate input
        expression = expression.strip()
        
        if not expression:
            return "Error: Empty expression"
        
        # Basic validation - check for potentially dangerous patterns
        dangerous_patterns = ['import', '__', 'exec', 'eval', 'open', 'file', 'compile']
        if any(pattern in expression.lower() for pattern in dangerous_patterns):
            return "Error: Expression contains potentially dangerous operations"
        
        # Parse the expression into an AST
        try:
            tree = ast.parse(expression, mode='eval')
        except SyntaxError as e:
            return f"Error: Invalid syntax in expression '{expression}': {str(e)}"
        
        # Safely evaluate the AST
        result = safe_eval_expression(tree)
        
        # Format the result nicely
        if isinstance(result, float):
            if result.is_integer():
                return str(int(result))
            else:
                # Round to avoid floating point precision issues
                return f"{result:.10g}"
        else:
            return str(result)
            
    except ValueError as e:
        return f"Error: {str(e)}"
    except ZeroDivisionError:
        return "Error: Division by zero"
    except OverflowError:
        return "Error: Result too large to compute"
    except Exception as e:
        return f"Error: Unexpected error occurred: {str(e)}"


# In[34]:


## add to the tool list
tools=[search_tool,recommend_clothing, calculator_tool]

tools_by_name={ tool.name:tool for tool in tools}


# ### test the calculator tool
# 

# In[35]:


if __name__ == "__main__":
    # Test cases
    test_expressions = [
        "2 + 3",
        "10 - 4",
        "6 * 7",
        "15 / 3",
        "2 ** 8",
        "10 % 3",
        "15 // 4",
        "(2 + 3) * 4",
        "2 + 3 * 4 - 1",
        "abs(-5)",
        "round(3.14159, 2)",
        "min(5, 3, 8, 1)",
        "max(5, 3, 8, 1)",
        "sqrt(16)",
        "sin(pi/2)",
        "cos(0)",
        "log10(100)",
        "exp(1)",
        "pi * 2",
        "e ** 2",
        "-5 + 3",
        "pow(2, 3)",
        "ceil(4.3)",
        "floor(4.7)",
        "5 / 0",  # Division by zero test
        "sqrt(-1)",  # Math domain error test
        "invalid_function(5)",  # Invalid function test
        "import os",  # Security test
        "",  # Empty expression test
        "2 + ",  # Syntax error test
    ]
    
    print("Testing Calculator Tool:")
    print("=" * 60)
    
    for expr in test_expressions:
        result = calculator_tool(expr)
        status = "✓" if not result.startswith("Error") else "✗"
        print(f"{status} {expr:<20} -> {result}")


# In[36]:


# test agent execution
def print_stream(stream):
    """Helper function for formatting the stream nicely."""
    for s in stream:
        message = s["messages"][-1]
        if isinstance(message, tuple):
            print(message)
        else:
            message.pretty_print()

inputs = {"messages": [HumanMessage(content="What's 15% of 250 plus the square root of 144?")]}

print_stream(graph.stream(inputs, stream_mode="values"))


# ## Exercise 2 - Create a News Summary Tool
# 
# **Objective:** Build a tool that can fetch and summarize recent news articles.
# 
# Create a news summarization tool that works with the existing search functionality. This tool should take search results and create concise summaries of news articles.
# 
# ### Instructions:
# 1. Create a `news_summarizer_tool` that takes news content and creates summaries.
# 2. The tool should extract key information: headline, date, main points.
# 3. Format the output in a readable way.
# 4. Test it by asking the agent to "search for recent AI news and summarize the top 3 articles".
# 
# ### Starter Code:
# 

# In[37]:


@tool
def news_summarizer_tool(news_content: str) -> str:
    """
    Summarize news articles from search results.
    
    :param news_content: Raw news content or search results
    :return: A formatted summary of the news
    """
    # TODO: Parse the news content
    # TODO: Extract key information (headlines, dates, main points)
    # TODO: Format into a readable summary
    # Hint: You might want to split by articles and process each one
    pass

# TODO: Add to tools list and test with:
# "Find recent news about artificial intelligence and give me a summary"


# In[39]:


import re
import json
from datetime import datetime
from typing import Dict, List, Any, Optional
from dataclasses import dataclass
from functools import wraps

def tool(name: str = None, description: str = None):
    """Tool decorator for marking functions as tools"""
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)
        wrapper._tool_name = name or func.__name__
        wrapper._tool_description = description or func.__doc__
        return wrapper
    return decorator

@dataclass
class NewsArticle:
    """Data class to represent a news article"""
    title: str
    content: str
    date: Optional[str] = None
    source: Optional[str] = None
    url: Optional[str] = None
    summary: Optional[str] = None

class NewsParser:
    """Parse different formats of news content"""
    
    def __init__(self):
        # Common patterns for extracting article information
        self.title_patterns = [
            r'(?:Title|Headline):\s*(.+?)(?:\n|$)',
            r'^(.+?)\n',  # First line as title
            r'<title>(.+?)</title>',  # HTML title
            r'# (.+?)(?:\n|$)',  # Markdown heading
        ]
        
        self.date_patterns = [
            r'(?:Date|Published|Posted):\s*([^\n]+)',
            r'(\d{4}-\d{2}-\d{2})',  # YYYY-MM-DD
            r'(\d{1,2}/\d{1,2}/\d{4})',  # MM/DD/YYYY
            r'([A-Za-z]+ \d{1,2}, \d{4})',  # Month DD, YYYY
        ]
        
        self.source_patterns = [
            r'(?:Source|By|Author):\s*([^\n]+)',
            r'- ([A-Za-z\s]+)$',  # Source at end with dash
        ]
        
        self.url_patterns = [
            r'(?:URL|Link):\s*(https?://[^\s]+)',
            r'(https?://[^\s]+)',
        ]
    
    def extract_articles_from_text(self, content: str) -> List[NewsArticle]:
        """Extract multiple articles from text content"""
        articles = []
        
        # Try to split by common delimiters
        article_separators = [
            r'\n---+\n',  # Horizontal rules
            r'\n={3,}\n',  # Equal signs
            r'\n#{2,}\s',  # Multiple hashtags
            r'\nArticle \d+:',  # Article numbering
            r'\n\d+\.\s',  # Numbered list
        ]
        
        article_chunks = [content]  # Start with full content
        
        # Try each separator
        for separator in article_separators:
            new_chunks = []
            for chunk in article_chunks:
                new_chunks.extend(re.split(separator, chunk))
            if len(new_chunks) > 1:
                article_chunks = new_chunks
                break
        
        # Process each chunk as a potential article
        for chunk in article_chunks:
            chunk = chunk.strip()
            if len(chunk) > 50:  # Minimum content length
                article = self.parse_single_article(chunk)
                if article and article.title:
                    articles.append(article)
        
        return articles if articles else [self.parse_single_article(content)]
    
    def parse_single_article(self, content: str) -> NewsArticle:
        """Parse a single article from content"""
        title = self._extract_title(content)
        date = self._extract_date(content)
        source = self._extract_source(content)
        url = self._extract_url(content)
        
        # Clean content by removing extracted metadata
        clean_content = self._clean_content(content, title, date, source, url)
        
        return NewsArticle(
            title=title or "Untitled Article",
            content=clean_content,
            date=date,
            source=source,
            url=url
        )
    
    def _extract_title(self, content: str) -> Optional[str]:
        """Extract title from content"""
        for pattern in self.title_patterns:
            match = re.search(pattern, content, re.IGNORECASE | re.MULTILINE)
            if match:
                title = match.group(1).strip()
                if len(title) > 5 and len(title) < 200:  # Reasonable title length
                    return title
        return None
    
    def _extract_date(self, content: str) -> Optional[str]:
        """Extract date from content"""
        for pattern in self.date_patterns:
            match = re.search(pattern, content, re.IGNORECASE)
            if match:
                return match.group(1).strip()
        return None
    
    def _extract_source(self, content: str) -> Optional[str]:
        """Extract source from content"""
        for pattern in self.source_patterns:
            match = re.search(pattern, content, re.IGNORECASE | re.MULTILINE)
            if match:
                source = match.group(1).strip()
                if len(source) > 2 and len(source) < 100:
                    return source
        return None
    
    def _extract_url(self, content: str) -> Optional[str]:
        """Extract URL from content"""
        for pattern in self.url_patterns:
            match = re.search(pattern, content)
            if match:
                return match.group(1).strip()
        return None
    
    def _clean_content(self, content: str, title: str, date: str, source: str, url: str) -> str:
        """Remove extracted metadata from content"""
        clean_content = content
        
        # Remove extracted elements
        elements_to_remove = [title, date, source, url]
        for element in elements_to_remove:
            if element:
                # Remove the element and common prefixes
                patterns_to_remove = [
                    rf'(?:Title|Headline):\s*{re.escape(element)}',
                    rf'(?:Date|Published|Posted):\s*{re.escape(element)}',
                    rf'(?:Source|By|Author):\s*{re.escape(element)}',
                    rf'(?:URL|Link):\s*{re.escape(element)}',
                    re.escape(element)
                ]
                
                for pattern in patterns_to_remove:
                    clean_content = re.sub(pattern, '', clean_content, flags=re.IGNORECASE)
        
        # Clean up extra whitespace
        clean_content = re.sub(r'\n\s*\n', '\n\n', clean_content)
        clean_content = clean_content.strip()
        
        return clean_content

class NewsSummarizer:
    """Summarize news articles"""
    
    def __init__(self):
        self.max_summary_sentences = 3
        self.min_sentence_length = 20
    
    def summarize_article(self, article: NewsArticle) -> str:
        """Generate a summary for a single article"""
        if not article.content:
            return "No content available for summary."
        
        # Split into sentences
        sentences = self._split_into_sentences(article.content)
        
        if not sentences:
            return "Unable to extract meaningful content."
        
        # Score sentences based on various factors
        scored_sentences = self._score_sentences(sentences, article.title)
        
        # Select top sentences for summary
        top_sentences = sorted(scored_sentences.items(), key=lambda x: x[1], reverse=True)
        summary_sentences = [sent for sent, score in top_sentences[:self.max_summary_sentences]]
        
        # Reconstruct summary maintaining original order
        original_order_summary = []
        for sentence in sentences:
            if sentence in summary_sentences:
                original_order_summary.append(sentence)
        
        return ' '.join(original_order_summary)
    
    def _split_into_sentences(self, text: str) -> List[str]:
        """Split text into sentences"""
        # Simple sentence splitting
        sentences = re.split(r'[.!?]+', text)
        
        # Clean and filter sentences
        clean_sentences = []
        for sentence in sentences:
            sentence = sentence.strip()
            if len(sentence) >= self.min_sentence_length:
                clean_sentences.append(sentence)
        
        return clean_sentences
    
    def _score_sentences(self, sentences: List[str], title: str = None) -> Dict[str, float]:
        """Score sentences for importance"""
        scores = {}
        
        # Calculate word frequencies
        all_words = ' '.join(sentences).lower()
        word_freq = {}
        for word in re.findall(r'\b[a-z]{3,}\b', all_words):
            word_freq[word] = word_freq.get(word, 0) + 1
        
        # Title words (if available) get bonus
        title_words = set()
        if title:
            title_words = set(re.findall(r'\b[a-z]{3,}\b', title.lower()))
        
        for sentence in sentences:
            score = 0.0
            words = re.findall(r'\b[a-z]{3,}\b', sentence.lower())
            
            if not words:
                scores[sentence] = 0.0
                continue
            
            # Base score: average word frequency
            score += sum(word_freq.get(word, 0) for word in words) / len(words)
            
            # Bonus for title words
            title_word_count = sum(1 for word in words if word in title_words)
            score += title_word_count * 2
            
            # Bonus for sentence position (first sentences often important)
            position_bonus = max(0, 2 - sentences.index(sentence) * 0.5)
            score += position_bonus
            
            # Penalty for very long sentences
            if len(sentence) > 200:
                score *= 0.8
            
            # Bonus for sentences with numbers/dates (often factual)
            if re.search(r'\b\d+\b', sentence):
                score += 1
            
            scores[sentence] = score
        
        return scores

@tool(name="news_summarizer", description="Summarize news articles from search results")
def news_summarizer_tool(news_content: str) -> str:
    """
    Summarize news articles from search results.
    
    :param news_content: Raw news content or search results
    :return: A formatted summary of the news
    """
    try:
        # Initialize parser and summarizer
        parser = NewsParser()
        summarizer = NewsSummarizer()
        
        # Parse articles from the content
        articles = parser.extract_articles_from_text(news_content)
        
        if not articles:
            return "No articles could be extracted from the provided content."
        
        # Generate summary for each article
        summaries = []
        for i, article in enumerate(articles, 1):
            summary = summarizer.summarize_article(article)
            article.summary = summary
            
            # Format the summary
            formatted_summary = f"**Article {i}: {article.title}**\n"
            
            if article.date:
                formatted_summary += f"*Date: {article.date}*\n"
            
            if article.source:
                formatted_summary += f"*Source: {article.source}*\n"
            
            formatted_summary += f"\n{summary}\n"
            
            if article.url:
                formatted_summary += f"*Read more: {article.url}*\n"
            
            summaries.append(formatted_summary)
        
        # Combine all summaries
        final_summary = f"**News Summary ({len(articles)} article{'s' if len(articles) > 1 else ''})**\n\n"
        final_summary += "\n---\n\n".join(summaries)
        
        return final_summary
        
    except Exception as e:
        return f"Error processing news content: {str(e)}"

# Alternative implementation for JSON-formatted news
@tool(name="json_news_summarizer", description="Summarize news from JSON format")
def json_news_summarizer_tool(json_content: str) -> str:
    """
    Summarize news articles from JSON-formatted search results.
    
    :param json_content: JSON string containing news articles
    :return: A formatted summary of the news
    """
    try:
        # Try to parse as JSON
        data = json.loads(json_content)
        
        parser = NewsParser()
        summarizer = NewsSummarizer()
        articles = []
        
        # Handle different JSON structures
        if isinstance(data, list):
            # List of articles
            for item in data:
                article = NewsArticle(
                    title=item.get('title', 'Untitled'),
                    content=item.get('content', item.get('description', '')),
                    date=item.get('date', item.get('published_at')),
                    source=item.get('source', item.get('author')),
                    url=item.get('url', item.get('link'))
                )
                articles.append(article)
        
        elif isinstance(data, dict):
            if 'articles' in data:
                # Wrapped in articles key
                for item in data['articles']:
                    article = NewsArticle(
                        title=item.get('title', 'Untitled'),
                        content=item.get('content', item.get('description', '')),
                        date=item.get('date', item.get('published_at')),
                        source=item.get('source', item.get('author')),
                        url=item.get('url', item.get('link'))
                    )
                    articles.append(article)
            else:
                # Single article
                article = NewsArticle(
                    title=data.get('title', 'Untitled'),
                    content=data.get('content', data.get('description', '')),
                    date=data.get('date', data.get('published_at')),
                    source=data.get('source', data.get('author')),
                    url=data.get('url', data.get('link'))
                )
                articles.append(article)
        
        # Generate summaries
        summaries = []
        for i, article in enumerate(articles, 1):
            if article.content:
                summary = summarizer.summarize_article(article)
                
                formatted_summary = f"**{article.title}**\n"
                
                if article.date:
                    formatted_summary += f"*{article.date}*\n"
                if article.source:
                    formatted_summary += f"*{article.source}*\n"
                
                formatted_summary += f"\n{summary}\n"
                
                if article.url:
                    formatted_summary += f"[Read more]({article.url})\n"
                
                summaries.append(formatted_summary)
        
        if not summaries:
            return "No valid articles found in JSON content."
        
        final_summary = f"**News Summary ({len(summaries)} articles)**\n\n"
        final_summary += "\n---\n\n".join(summaries)
        
        return final_summary
        
    except json.JSONDecodeError:
        # Fall back to regular text parsing
        return news_summarizer_tool(json_content)
    except Exception as e:
        return f"Error processing JSON news content: {str(e)}"


# In[40]:


# add to the tool list
tools=[search_tool,recommend_clothing, calculator_tool,news_summarizer_tool]

tools_by_name={ tool.name:tool for tool in tools}


# In[41]:


# Test function
def test_news_summarizer():
    """Test the news summarizer with sample content"""
    
    # Sample news content
    sample_news = """
    Title: Tech Giant Announces Major AI Breakthrough
    Date: 2024-03-15
    Source: TechNews Daily
    URL: https://technews.com/ai-breakthrough
    
    A major technology company announced today a significant breakthrough in artificial intelligence that could revolutionize how we interact with computers. The new system demonstrates unprecedented capabilities in natural language understanding and generation.
    
    The breakthrough involves a novel architecture that combines multiple AI approaches. Researchers spent three years developing this technology. The system can perform complex reasoning tasks that were previously impossible for AI systems.
    
    Industry experts are calling this development a game-changer for the field of artificial intelligence. The company plans to integrate this technology into consumer products starting next year.
    
    ---
    
    Title: Climate Summit Reaches Historic Agreement
    Date: 2024-03-14
    Source: Global News Network
    
    World leaders at the international climate summit have reached a historic agreement on reducing carbon emissions. The deal includes commitments from 195 countries to achieve net-zero emissions by 2050.
    
    The agreement establishes a new international fund to help developing nations transition to clean energy. Wealthy nations have pledged $100 billion annually to support this transition. Environmental groups are cautiously optimistic about the deal.
    
    Critics argue that the timeline may be too ambitious and enforcement mechanisms are unclear. However, supporters believe this represents the most significant climate action in decades.
    """
    
    # Test the tool
    print("Testing News Summarizer Tool:")
    print("=" * 50)
    
    result = news_summarizer_tool(sample_news)
    print(result)
    
    # Test JSON format
    json_sample = """
    {
        "articles": [
            {
                "title": "Stock Market Hits Record High",
                "content": "The stock market reached an all-time high today as investors showed confidence in the economic recovery. Major indices gained over 2% in trading. Technology stocks led the rally with strong earnings reports. Market analysts attribute the growth to improved consumer spending and business investment.",
                "date": "2024-03-16",
                "source": "Financial Times",
                "url": "https://ft.com/market-high"
            }
        ]
    }
    """
    
    print("\n" + "=" * 50)
    print("Testing JSON News Summarizer:")
    print("=" * 50)
    
    json_result = json_news_summarizer_tool(json_sample)
    print(json_result)

if __name__ == "__main__":
    test_news_summarizer()


# ## Testing Your Solutions
# 
# For each exercise, test your implementation with these commands:
# 

# In[42]:


# Exercise 1 Test
inputs = {"messages": [HumanMessage(content="Calculate 15% of 250 plus the square root of 144")]}
print_stream(graph.stream(inputs, stream_mode="values"))


# In[43]:


# Exercise 2 Test  
inputs = {"messages": [HumanMessage(content="Find recent AI news and summarize the top 3 articles")]}
print_stream(graph.stream(inputs, stream_mode="values"))


# ## Authors
# 

# [Joseph Santarcangelo](https://author.skills.network/instructors/joseph_santarcangelo): Joseph has a Ph.D. in Electrical Engineering, his research focused on using machine learning, signal processing, and computer vision to determine how videos impact human cognition. Joseph has been working for IBM since he completed his PhD.
# 
# [Tenzin Migmar](https://author.skills.network/instructors/tenzin_migmar): Hi, I'm Tenzin. I'm a data scientist intern at IBM interested in applying machine learning to solve difficult problems. Prior to joining IBM, I worked as a research assistant on projects exploring perspectivism and personalization within large language models. In my free time, I enjoy recreational programming and learning to cook new recipes.
# 
# [Faranak Heidari](https://www.linkedin.com/in/faranakhdr/) is a data scientist and AI developer in IBM. 
# 

# <!--#### Change Log
# 

# <!--
# |Date (YYYY-MM-DD)|Version|Changed By|Change Description|
# |-|-|-|-|
# |2024-02-23|0.2|Elio Di Nino|Update library documentation|
# |2020-07-17|0.1|Sam|Create lab template|
# -->
# 

# Copyright © IBM Corporation. All rights reserved.
# 
