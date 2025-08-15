# Multi-Agent Course and Project: AI Applications

[![AI](https://img.shields.io/badge/AI-Multi--Agent%20System-blue)](https://github.com)
[![LLM](https://img.shields.io/badge/LLM-Llama%203.2%2090B-green)](https://github.com)
[![Framework](https://img.shields.io/badge/Framework-Gradio-orange)](https://github.com)
[![Vision](https://img.shields.io/badge/Computer%20Vision-Multimodal%20AI-purple)](https://github.com)

## 📚 Course Foundation: Introduction to Agentic AI

This project is built upon comprehensive coursework that provides deep understanding of Agentic AI principles and implementation:

### **Module 1: What is Agentic AI?**
**Lesson 1 - Let's Chat About Agents (AI-Powered)**
* 🎯 **Interactive Learning**: AI-powered lesson engagement (1 activity)
* 📊 **Generative vs Agentic AI**: Understanding fundamental distinctions (1 min)
* 🤖 **What Are AI Agents?**: Core concepts and definitions (1 min)
* 🔄 **AI Workflows vs Agents**: Architectural differences and use cases (1 min)
* 📋 **Types of AI Agents**: Classification and characteristics (1 min)
* ⚖️ **When (and When Not) to Use AI Agents**: Strategic implementation decisions (1 min)
* ✅ **Lesson 1 Quiz**: Knowledge validation (1 activity)

### **Module 2: Tool Calling & MCP**
**Lesson 2 - Interactive Learning Experience**
* 🎙️ **Interactive Podcast (AI-Powered)**: Immersive learning format (1 activity)
* 🔧 **Why Agents Need Tools**: Understanding tool integration necessity (1 min)
* 🗄️ **AI-Powered SQL Agents**: Database interaction capabilities (1 min)
* 📞 **Tool Calling for LLMs**: Implementation mechanisms (1 min)
* 🔧 **When to Call Tools Manually**: Decision-making frameworks (1 min)
* 🔗 **What is MCP?**: Model Context Protocol fundamentals (1 min)
* ✅ **Lesson 2 Quiz**: Competency assessment (1 activity)

### **Module 3: Agentic RAG & Multi-Agent Systems**
**Lesson 3 - Advanced Agent Architectures**
* 🎙️ **Interactive Podcast (AI-Powered)**: Advanced concept exploration (1 activity)
* 🔍 **Why RAG?**: Retrieval-Augmented Generation principles (1 min)
* 🤖 **Agentic RAG**: Agent-driven information retrieval (1 min)
* 🎼 **What are Orchestrator Agents**: Coordination and management patterns (1 min)
* 🏗️ **Multi-Agent Systems Fundamentals**: System design principles (1 min)
* ⚠️ **Risks of Agentic AI**: Safety and ethical considerations (1 min)
* ✅ **Lesson 3 Quiz**: Final knowledge verification (1 activity)

---

## 🚀 Project Portfolio

This repository showcases a comprehensive collection of Agentic AI projects, each demonstrating different aspects of Multi-Agent Systems and advanced AI implementation. These projects build upon the foundational coursework and represent practical applications of cutting-edge AI technologies.

---

## 📦 Project 1: AI NourishBot - Multi-Agent Nutrition Coach

AI NourishBot is an intelligent nutrition coaching application that leverages **Multi-Agent Systems (MAS)** and **advanced multimodal AI** to provide personalized dietary guidance. This project demonstrates the practical implementation of cutting-edge Agentic AI concepts, combining computer vision, natural language processing, and intelligent decision-making in a cohesive real-world application.

### 🎯 Project 1: Key Features

#### 🔍 **Intelligent Food Analysis**
* **Computer Vision Integration**: Utilizes Meta's Llama 3.2 90B Vision-Instruct model for accurate food identification
* **Comprehensive Nutrition Breakdown**: Provides detailed analysis of calories, macronutrients, and micronutrients
* **Real-time Processing**: Instant analysis of uploaded food images

#### 🤖 **Multi-Agent Architecture**
* **Vision Agent**: Processes visual input and identifies food items
* **Nutrition Agent**: Analyzes nutritional content and health metrics  
* **Recipe Agent**: Generates personalized recipe suggestions based on dietary preferences
* **Orchestrator Agent**: Coordinates workflow between specialized agents

#### 🍽️ **Personalized Dietary Management**
* **Dietary Restriction Support**: Vegan, Vegetarian, Gluten-free, Keto options
* **Intelligent Filtering**: Automatically excludes incompatible ingredients
* **Health Evaluation**: Provides actionable insights for nutritional improvement

#### 🌐 **User-Friendly Interface**
* **Gradio Web Interface**: Intuitive, accessible design for seamless user interaction
* **Dual Workflow Options**: Choose between Recipe Generation or Nutritional Analysis
* **Cross-platform Compatibility**: Works across desktop and mobile devices

### 🗏️ Project 1: Technical Architecture

#### **Multi-Agent System Design**
```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   Vision Agent  │    │ Nutrition Agent │    │  Recipe Agent   │
│                 │    │                 │    │                 │
│ • Image Analysis│    │ • Nutrient Calc │    │ • Recipe Gen    │
│ • Food ID       │    │ • Health Eval   │    │ • Diet Filter   │
└─────────────────┘    └─────────────────┘    └─────────────────┘
         │                       │                       │
         └───────────────────────┼───────────────────────┘
                                 │
                    ┌─────────────────┐
                    │ Orchestrator    │
                    │ Agent           │
                    │                 │
                    │ • Workflow Mgmt │
                    │ • Agent Coord   │
                    │ • Task Routing  │
                    └─────────────────┘
```

### **Technology Stack**
* **Core AI Model**: Meta Llama 3.2 90B Vision-Instruct
* **Backend Framework**: Flask
* **Frontend Interface**: Gradio
* **Agent Framework**: Custom Multi-Agent System implementation
* **Computer Vision**: Advanced multimodal AI processing
* **Tool Integration**: MCP (Model Context Protocol) for agent communication

## 📦 Project 2: CrewAI Content Creation Pipeline

A sophisticated **GenAI-powered content creation system** that transforms raw research into polished, insightful blog posts through collaborative agent workflows. This project demonstrates advanced **CrewAI framework implementation**, featuring a sequential multi-agent process where specialized agents work together autonomously to create high-quality content.

### 🎯 Project 2: Key Components

#### **Multi-Agent Architecture**
* **Research Analyst Agent**: Leverages SerperDev API for real-time web search and cutting-edge information gathering
* **Content Strategist Agent**: Transforms technical research into engaging, audience-ready content  
* **Social Media Strategist Agent**: Creates platform-specific promotional content for content amplification
* **Sequential Workflow**: Demonstrates agent collaboration without manual intervention

#### **Technical Implementation**
* **CrewAI Framework**: Professional multi-agent orchestration using Meta Llama 3.3 70B Instruct
* **Real-time Data Integration**: SerperDev Google Search API for current information access
* **Token Usage Analytics**: Performance monitoring and cost optimization
* **Dynamic Task Management**: Flexible topic-based content generation system

#### **Advanced Features**
* **Autonomous Collaboration**: Agents work together without manual intervention
* **Research-to-Content Pipeline**: Complete automation from data gathering to publication-ready content
* **Platform-Specific Output**: Tailored content for different distribution channels
* **Performance Monitoring**: Comprehensive analytics and resource tracking

### 🛠️ Project 2: Technical Stack

#### **Core Technologies**
* **Framework**: CrewAI 0.80.0 for multi-agent orchestration
* **LLM**: Meta Llama 3.3 70B Instruct for content generation
* **Search Integration**: SerperDev Google Search API for real-time information
* **Supporting Libraries**: LangChain 0.3.20, LangChain-Community 0.3.19

#### **Agent Capabilities**
* **Tool Integration**: Seamless external API utilization
* **Task Coordination**: Sequential and hierarchical workflow management
* **Content Quality**: Professional-grade output generation
* **Scalability**: Modular architecture for easy expansion

---

## 📦 Project 3: AI Math Assistant - LangChain Tool Calling System

An intelligent mathematical assistant that demonstrates **advanced tool calling capabilities** with LangChain agents. This project showcases the implementation of custom tools, multi-tool orchestration, and the integration of built-in tools for comprehensive problem-solving capabilities.

### 🎯 Project 3: Key Features

#### 🧮 **Mathematical Toolkit**
* **Custom Tool Creation**: Implements mathematical operations using both `Tool` class and `@tool` decorator
* **Comprehensive Operations**: Addition, subtraction, multiplication, division, and power calculations
* **Error Handling**: Robust input validation and edge case management
* **Flexible Input Parsing**: Handles various number formats and natural language inputs

#### 🔧 **Tool Calling Architecture**
* **LangChain Integration**: Utilizes IBM watsonx Granite and OpenAI GPT models
* **Multiple Agent Types**: Demonstrates `zero-shot-react-description`, `structured-chat-zero-shot-react-description`, and `openai-functions` agents
* **Tool Orchestration**: Intelligent tool selection based on user query context
* **LangGraph Implementation**: Modern agent execution using `create_react_agent`

#### 🌐 **External Tool Integration**
* **Built-in Tools**: Wikipedia search integration for factual information retrieval
* **Multi-step Problem Solving**: Combines information retrieval with mathematical computation
* **Extensible Framework**: Easy integration of additional LangChain community tools

#### 📊 **Testing & Validation**
* **Automated Test Suite**: Comprehensive test cases for all mathematical operations
* **Performance Monitoring**: Tool usage analytics and result validation
* **Error Case Handling**: Division by zero, invalid inputs, and edge case management

### 🗏️ Project 3: Technical Implementation

#### **Tool Creation Methods**
```python
# Method 1: Tool Class Wrapper
add_tool = Tool(
    name="AddTool",
    func=add_numbers,
    description="Adds a list of numbers and returns the result."
)

# Method 2: @tool Decorator (Recommended)
@tool
def add_numbers(inputs: str) -> dict:
    """Adds a list of numbers provided in the input string."""
    # Implementation with structured output
```

#### **Agent Architecture Comparison**
* **Classical Agents**: `initialize_agent` with ReAct framework
* **Modern Approach**: LangGraph's `create_react_agent` for enhanced flexibility
* **Model Compatibility**: Demonstrates integration with multiple LLM providers

#### **Technology Stack**
* **Core Framework**: LangChain 0.3.23, LangGraph 0.6.1
* **LLM Models**: IBM watsonx Granite 3.2, OpenAI GPT-4.1-nano
* **External APIs**: Wikipedia API for information retrieval
* **Supporting Libraries**: LangChain-Community, LangChain-OpenAI, LangChain-IBM

---

## 📦 Project 4: Manual Tool-Calling Agent - Advanced YouTube Analytics System

A comprehensive **YouTube interaction system** that demonstrates sophisticated tool calling capabilities with LangChain. This project showcases both manual and automated tool calling approaches, featuring custom YouTube tools for video analysis, content extraction, and intelligent summarization through recursive agent workflows.

### 🎯 Project 4: Key Features

#### 🔧 **Advanced Tool Architecture**
* **Custom Tool Creation**: Implements YouTube-specific tools using LangChain's `@tool` decorator
* **Video ID Extraction**: Intelligent parsing of various YouTube URL formats (standard, shortened, embedded)
* **Transcript Fetching**: Automated caption retrieval with multi-language support
* **Metadata Extraction**: Comprehensive video information including views, duration, likes, comments, and chapters
* **Search Integration**: Real-time YouTube search capabilities with result filtering

#### 🔄 **Manual vs Automated Tool Calling**
* **Manual Process Demonstration**: Step-by-step tool calling with explicit state management
* **Chain Automation**: Streamlined workflow using LangChain's chain functionality
* **Recursive Processing**: Dynamic tool calling that adapts to query complexity
* **Tool Call Orchestration**: Intelligent selection and sequencing of multiple tools

#### 🎬 **YouTube-Specific Capabilities**
* **Trending Videos Analysis**: Regional trending content discovery with metadata extraction
* **Thumbnail Retrieval**: Complete thumbnail collection across all available resolutions
* **Multi-language Support**: Transcript fetching in various language codes
* **Content Summarization**: AI-powered video content analysis and summary generation

#### 🔗 **Intelligent Workflow Management**
* **Sequential Chains**: Fixed-step workflows for predictable tool calling patterns
* **Recursive Chains**: Dynamic workflows that adapt to varying complexity requirements
* **State Management**: Comprehensive conversation history tracking with tool call linking
* **Error Handling**: Robust exception handling and graceful degradation

### 🗏️ Project 4: Technical Implementation

#### **Tool Ecosystem Architecture**
```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│  Video ID Tool  │    │ Transcript Tool │    │  Metadata Tool  │
│                 │    │                 │    │                 │
│ • URL Parsing   │    │ • Multi-lang    │    │ • Views/Likes   │
│ • Format Handle │    │ • Caption Fetch │    │ • Duration      │
└─────────────────┘    └─────────────────┘    └─────────────────┘
         │                       │                       │
         └───────────────────────┼───────────────────────┘
                                 │
    ┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
    │   Search Tool   │    │ Trending Tool   │    │ Thumbnail Tool  │
    │                 │    │                 │    │                 │
    │ • Query Search  │    │ • Regional Data │    │ • Multi-res     │
    │ • Result Filter │    │ • Top Videos    │    │ • URL Extract   │
    └─────────────────┘    └─────────────────┘    └─────────────────┘
```

#### **Recursive Chain Flow**
* **Dynamic Decision Making**: LLM-driven tool selection based on query context
* **Tool Call Execution**: Parallel processing of multiple tool requests
* **State Preservation**: Comprehensive conversation history with tool call linking
* **Termination Logic**: Intelligent stopping conditions for workflow completion

#### **Technology Stack**
* **Core Framework**: LangChain 0.3.23 for tool orchestration and chaining
* **LLM Integration**: OpenAI GPT-4o-mini for intelligent tool selection
* **YouTube Libraries**: PyTube, yt-dlp, youtube-transcript-api for comprehensive video access
* **Data Processing**: JSON handling, regex parsing, and structured data extraction
* **Chain Architecture**: RunnablePassthrough, RunnableLambda for workflow automation

#### **Advanced Features**
* **Tool Mapping System**: Dynamic tool lookup and execution architecture
* **Message History Management**: Complete conversation context preservation
* **Parallel Tool Execution**: Efficient processing of multiple simultaneous tool calls
* **Universal Query Handling**: Adaptable system for diverse YouTube-related requests

---

## 🎯 Portfolio Capabilities Demonstrated

### **Advanced AI Integration**
* **Multimodal Processing**: Seamless handling of visual and textual data
* **Agent Collaboration**: Sophisticated inter-agent communication protocols
* **Dynamic Decision Making**: Context-aware response generation
* **Tool Orchestration**: Intelligent selection and coordination of specialized tools

### **Real-World Application**
* **Practical Problem Solving**: Addresses genuine challenges across nutrition, content creation, and mathematical computation
* **User Experience Focus**: Intuitive interface design with professional polish
* **Scalable Architecture**: Designed for potential cloud deployment and broader accessibility

### **Technical Proficiency**
* **Modern AI Frameworks**: Implementation of state-of-the-art AI technologies including CrewAI, LangChain, and LangGraph
* **System Architecture**: Well-structured, maintainable codebase across multiple project types
* **Integration Skills**: Successful combination of multiple complex technologies and external APIs

## ⚠️ Important Disclaimers

**Safety Notice**: These AI systems provide automated suggestions based on their respective inputs. While designed for accuracy and safety, recommendations should be validated by users, especially for health-related (Project 1) or financial/business decisions (Project 2).

**Medical Advice**: Consult qualified healthcare providers for personalized dietary advice, especially if you have specific health concerns or allergies.

**User Responsibility**: Final responsibility for implementation safety and accuracy verification rests with the user across all project applications.

## 🚀 Future Enhancements & Project Expansion

### **Planned Projects**
* **Project 5**: Simple ReAct Agent from Scratch
* **Project 6**: Agentic AI Workflow Design Patterns with LangGraph
* **Project 7**: MultiAgent Healthcare Chatbot with AG2
* **Project 8**: Customer Support Agent with PydanticAI
* **Project 9**: Document Chat via Agentic RAG

### **Portfolio Improvements**
* **Cloud Deployment**: Platform deployment for broader accessibility
* **Enhanced UI Customization**: Extended interface personalization across projects
* **Advanced Analytics**: Detailed performance tracking and optimization
* **Integration Capabilities**: API endpoints for third-party applications
* **Cross-Project Synergies**: Shared components and unified architecture patterns

## 🏆 Project Significance

This expanding portfolio represents the successful integration of:
* **Cutting-edge AI Technologies**: LLMs, computer vision, and advanced reasoning systems
* **Diverse System Designs**: Multi-agent architectures, tool calling frameworks, and content automation
* **Practical Application Development**: Real-world problem-solving across multiple domains
* **User Experience Excellence**: Intuitive interface design and professional implementation

The AI NourishBot, CrewAI Content Creation Pipeline, AI Math Assistant, and Manual Tool-Calling Agent projects collectively showcase the transformative potential of Agentic AI in creating intelligent, specialized solutions for diverse challenges, demonstrating both technical expertise and innovative thinking in the rapidly evolving field of artificial intelligence.

---

*This project portfolio exemplifies the practical application of advanced AI concepts, demonstrating proficiency in multi-agent systems, multimodal AI integration, tool calling frameworks, and modern application development practices across diverse problem domains.*
