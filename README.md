# AI Research Assistant

An AI-powered research assistant that accepts a research question, searches the live web using Tavily, uses OpenAI to synthesize findings, and produces structured output with verifiable source citations.

## Features

- Accepts a research question from the command line
- Searches external web sources using Tavily API
- Uses OpenAI to synthesize findings into structured JSON
- Includes source citations and tracks used sources
- Robust error handling for empty searches or API issues
- Automatically saves structured results as JSON

## Requirements

- Python 3.10 or newer
- OpenAI API key
- Tavily API key

## Installation

1. Clone the repository and navigate into the project folder.
2. Create and activate a virtual environment:
   ```bash
   python -m venv .venv
   
