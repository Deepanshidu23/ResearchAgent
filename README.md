# Raw Agent Using Groq

A simple AI Agent built from scratch using the Groq API and Python.

This project demonstrates the core concept behind modern AI agent frameworks such as LangGraph, CrewAI, OpenAI Agents SDK, and Claude Code.

## Features

* Raw Agent Loop
* Function / Tool Calling
* File Read Tool
* File Write Tool
* Multi-Step Reasoning
* Agent Execution Trace

## Tech Stack

* Python
* Groq API
* Llama 3.3 70B Versatile

## Project Structure

```text
ResearchAgent/
│
├── main.py
├── requirements.txt
├── README.md
├── .gitignore
└── venv/
```

## Agent Flow

```text
User Request
     ↓
Groq LLM
     ↓
Tool Call
     ↓
Execute Tool
     ↓
Tool Result
     ↓
LLM Reasoning
     ↓
Final Answer
```

# Tools Implemented

# web_search()

Searches for information.

# write_file()

Writes content to a file.

# read_file()

Reads content from a file.

#Example Task

Research prompt chaining, save findings to a file, read the file, and generate a summary.

# Learning Outcomes

This project helped me understand:

* Agent Architecture
* Tool Calling
* Message History
* Agent Loops
* AI Engineering Fundamentals

# Future Improvements

* Real Web Search (Tavily API)
* Memory Support
* RAG Integration
* LangGraph Implementation
* Multi-Agent System


Learning AI Engineering one project at a time.
