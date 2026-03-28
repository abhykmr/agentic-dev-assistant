# Agentic Dev Assistant

AI developer assistant built using agentic architecture.

## Features

- AI Agent using LLM
- Tool-based architecture
- Browser automation using Playwright
- File system tools
- Memory system (vector database)

## Tech Stack

Python  
LangChain  
Playwright  
ChromaDB  
OpenAI API

## Project Structure

agents/
tools/
memory/
config/

## Running Local LLM

Install Ollama

ollama pull deepseek-coder

Start model

ollama run deepseek-coder

## Run Project

pip install -r requirements.txt

playwright install

python main.py
