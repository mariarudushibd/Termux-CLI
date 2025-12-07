#!/usr/bin/env python3
"""Basic usage example for Termux-CLI"""

from core.agent import Agent
from core.session import Session

def main():
    # Initialize agent with working directory
    agent = Agent(working_dir=".")
    
    # Create a session
    session = Session()
    
    # Example: Ask agent to analyze code
    response = agent.run("List all Python files in this directory")
    print(response)
    
    # Example: Ask agent to create a file
    response = agent.run("Create a hello.py file that prints 'Hello, World!'")
    print(response)

if __name__ == "__main__":
    main()
