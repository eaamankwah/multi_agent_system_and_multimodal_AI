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

---

## 🚀 Project Portfolio

This repository showcases a comprehensive collection of Agentic AI projects, each demonstrating different aspects of Multi-Agent Systems and advanced AI implementation. These projects build upon the foundational coursework and represent practical applications of cutting-edge AI technologies.

---

## 📦 Project 1: AI NourishBot - Multi-Agent Nutrition Coach

AI NourishBot is an intelligent nutrition coaching application that leverages **Multi-Agent Systems (MAS)** and **advanced multimodal AI** to provide personalized dietary guidance. This project demonstrates the practical implementation of cutting-edge Agentic AI concepts, combining computer vision, natural language processing, and intelligent decision-making in a cohesive real-world application.

## 🎯 Project 1: AI NourishBot Features

## 🎯 Key Features

### 🔍 **Intelligent Food Analysis**
* **Computer Vision Integration**: Utilizes Meta's Llama 3.2 90B Vision-Instruct model for accurate food identification
* **Comprehensive Nutrition Breakdown**: Provides detailed analysis of calories, macronutrients, and micronutrients
* **Real-time Processing**: Instant analysis of uploaded food images

### 🤖 **Multi-Agent Architecture**
* **Vision Agent**: Processes visual input and identifies food items
* **Nutrition Agent**: Analyzes nutritional content and health metrics  
* **Recipe Agent**: Generates personalized recipe suggestions based on dietary preferences
* **Orchestrator Agent**: Coordinates workflow between specialized agents

### 🍽️ **Personalized Dietary Management**
* **Dietary Restriction Support**: Vegan, Vegetarian, Gluten-free, Keto options
* **Intelligent Filtering**: Automatically excludes incompatible ingredients
* **Health Evaluation**: Provides actionable insights for nutritional improvement

### 🌐 **User-Friendly Interface**
* **Gradio Web Interface**: Intuitive, accessible design for seamless user interaction
* **Dual Workflow Options**: Choose between Recipe Generation or Nutritional Analysis
* **Cross-platform Compatibility**: Works across desktop and mobile devices

## 🏗️ Project 1: Technical Architecture

### **Multi-Agent System Design**
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

## 📚 Educational Foundation

This project is built upon comprehensive coursework in **Introduction to Agentic AI**, covering:

### **Module 1: AI Agent Fundamentals**
* Generative vs Agentic AI distinctions
* AI Agent types and classification
* Workflow vs Agent architectures
* Strategic agent deployment decisions

### **Module 2: Tool Calling & MCP**
* AI-powered SQL agents implementation
* LLM tool calling mechanisms
* Manual vs automated tool selection
* Model Context Protocol (MCP) integration

### **Module 3: Advanced Agent Systems**
* Agentic RAG (Retrieval-Augmented Generation)
* Multi-Agent Systems fundamentals
* Orchestrator agent design patterns
* Risk assessment and mitigation in Agentic AI

## 🛠️ Project 1: Installation & Setup

### Prerequisites
```bash
Python 3.8+
Flask
Gradio
Required AI model access (Llama 3.2 90B)
```

### Quick Start
```bash
# Clone the repository
git clone [repository-url]
cd ai-nourishbot

# Install dependencies
pip install -r requirements.txt

# Run the application
python app.py
```

### Configuration
```python
# Configure your AI model endpoint
MODEL_ENDPOINT = "your-llama-endpoint"
API_KEY = "your-api-key"
```

## 📖 Project 1: Usage Guide

### **Recipe Workflow**
1. Upload a food image
2. Specify dietary restrictions (optional)
3. Select "Recipe" workflow
4. Receive personalized recipe suggestions using detected ingredients

### **Analysis Workflow**
1. Upload a food image
2. Select "Analysis" workflow
3. Get comprehensive nutritional breakdown and health insights

## 🎯 Capabilities Demonstrated

### **Advanced AI Integration**
* **Multimodal Processing**: Seamless handling of visual and textual data
* **Agent Collaboration**: Sophisticated inter-agent communication protocols
* **Dynamic Decision Making**: Context-aware response generation

### **Real-World Application**
* **Practical Problem Solving**: Addresses genuine dietary management challenges
* **User Experience Focus**: Intuitive interface design with professional polish
* **Scalable Architecture**: Designed for potential cloud deployment and broader accessibility

### **Technical Proficiency**
* **Modern AI Frameworks**: Implementation of state-of-the-art AI technologies
* **System Architecture**: Well-structured, maintainable codebase
* **Integration Skills**: Successful combination of multiple complex technologies

## 📦 Project 2: CrewAI Content Creation Pipeline

A sophisticated **GenAI-powered content creation system** that transforms raw research into polished, insightful blog posts through collaborative agent workflows. This project demonstrates advanced **CrewAI framework implementation**, featuring a sequential multi-agent process where specialized agents work together autonomously to create high-quality content.

## 🎯 Project 2: Key Components

### **Multi-Agent Architecture**
* **Research Analyst Agent**: Leverages SerperDev API for real-time web search and cutting-edge information gathering
* **Content Strategist Agent**: Transforms technical research into engaging, audience-ready content  
* **Social Media Strategist Agent**: Creates platform-specific promotional content for content amplification
* **Sequential Workflow**: Demonstrates agent collaboration without manual intervention

### **Technical Implementation**
* **CrewAI Framework**: Professional multi-agent orchestration using Meta Llama 3.3 70B Instruct
* **Real-time Data Integration**: SerperDev Google Search API for current information access
* **Token Usage Analytics**: Performance monitoring and cost optimization
* **Dynamic Task Management**: Flexible topic-based content generation system

### **Advanced Features**
* **Autonomous Collaboration**: Agents work together without manual intervention
* **Research-to-Content Pipeline**: Complete automation from data gathering to publication-ready content
* **Platform-Specific Output**: Tailored content for different distribution channels
* **Performance Monitoring**: Comprehensive analytics and resource tracking

## 🛠️ Project 2: Technical Stack

### **Core Technologies**
* **Framework**: CrewAI 0.80.0 for multi-agent orchestration
* **LLM**: Meta Llama 3.3 70B Instruct for content generation
* **Search Integration**: SerperDev Google Search API for real-time information
* **Supporting Libraries**: LangChain 0.3.20, LangChain-Community 0.3.19

### **Agent Capabilities**
* **Tool Integration**: Seamless external API utilization
* **Task Coordination**: Sequential and hierarchical workflow management
* **Content Quality**: Professional-grade output generation
* **Scalability**: Modular architecture for easy expansion

This project showcases enterprise-level content automation capabilities and demonstrates proficiency in modern AI agent frameworks for scalable workflow automation.

## 🎯 Portfolio Capabilities Demonstrated

### **Advanced AI Integration**
* **Multimodal Processing**: Seamless handling of visual and textual data
* **Agent Collaboration**: Sophisticated inter-agent communication protocols
* **Dynamic Decision Making**: Context-aware response generation

### **Real-World Application**
* **Practical Problem Solving**: Addresses genuine dietary management challenges
* **User Experience Focus**: Intuitive interface design with professional polish
* **Scalable Architecture**: Designed for potential cloud deployment and broader accessibility

### **Technical Proficiency**
* **Modern AI Frameworks**: Implementation of state-of-the-art AI technologies
* **System Architecture**: Well-structured, maintainable codebase
* **Integration Skills**: Successful combination of multiple complex technologies

## ⚠️ Important Disclaimers

**Safety Notice**: This AI system provides automated nutritional suggestions based on image analysis. While designed for accuracy and safety, recommendations may not account for all dietary restrictions, allergens, or potentially harmful ingredients.

**Medical Advice**: Consult qualified healthcare providers for personalized dietary advice, especially if you have specific health concerns or allergies.

**User Responsibility**: Final responsibility for recipe safety and ingredient verification rests with the user.

## 🚀 Future Enhancements

* **Cloud Deployment**: Platform deployment for broader accessibility
* **Enhanced UI Customization**: Extended Gradio interface personalization
* **Additional Dietary Profiles**: Expanded restriction and preference support
* **Integration Capabilities**: API endpoints for third-party applications
* **Advanced Analytics**: Detailed nutrition tracking and progress monitoring

## 🏆 Project Significance

This project represents the successful integration of:
* **Cutting-edge AI Technologies**: LLMs and computer vision
* **Advanced System Design**: Multi-agent architectures
* **Practical Application Development**: Real-world problem-solving
* **User Experience Excellence**: Intuitive interface design

AI NourishBot and CrewAI Content Creation Pipeline showcase the transformative potential of Agentic AI in creating intelligent, personalized solutions for everyday challenges, demonstrating both technical expertise and innovative thinking in the rapidly evolving field of artificial intelligence.

---

*This project exemplifies the practical application of advanced AI concepts, demonstrating proficiency in multi-agent systems, multimodal AI integration, and modern application development practices.*
