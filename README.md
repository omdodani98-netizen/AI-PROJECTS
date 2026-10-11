<<<<<<< HEAD
# AI Research Assistant

An AI-powered command-line research assistant.

## Features

- Accepts a research question
- Searches external web sources using Tavily
- Uses OpenAI to synthesize findings
- Produces structured output
- Includes source citations
- Handles errors
- Saves results as JSON

## Requirements

- Python 3.10 or newer
- OpenAI API key
- Tavily API key

## Installation

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it on Windows:

```bash
.venv\Scripts\activate
```

Activate it on macOS/Linux:

```bash
source .venv/bin/activate
```

Install packages:

```bash
pip install -r requirements.txt
```

## Configuration

Create a `.env` file in the project root:

```env
OPENAI_API_KEY=your_openai_api_key_here
TAVILY_API_KEY=your_tavily_api_key_here
OPENAI_MODEL=gpt-4o-mini
MAX_SEARCH_RESULTS=5
```

## Run

```bash
python app.py
```

Example question:

```text
What are the benefits and risks of artificial intelligence in education?
```

## Test

```bash
python -m pytest
```

## Output

The application displays:

- An answer
- Key findings
- Citation markers
- Source URLs

It also creates:

```text
research_output.json
```

## Important

Never upload `.env` to GitHub.
Use `.env.example` for sharing configuration format.
=======
# AI-PROJECTS
A modular Python framework for training, evaluating, and deploying machine learning models for [insert task, e.g., image classification / text analysis
>>>>>>> 4f6edff6d8447600be5241792808f7f62cd89ce5
