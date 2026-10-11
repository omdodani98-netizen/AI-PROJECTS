import os

from dotenv import load_dotenv


load_dotenv()


def get_required_setting(name: str) -> str:
    value = os.getenv(name)

    if not value or not value.strip():
        raise ValueError(
            f"Missing {name}. Add it to your .env file."
        )

    return value.strip()


OPENAI_API_KEY = get_required_setting("OPENAI_API_KEY")
TAVILY_API_KEY = get_required_setting("TAVILY_API_KEY")

OPENAI_MODEL = os.getenv(
    "OPENAI_MODEL",
    "gpt-4o-mini"
)

try:
    MAX_SEARCH_RESULTS = int(
        os.getenv("MAX_SEARCH_RESULTS", "5")
    )
except ValueError:
    MAX_SEARCH_RESULTS = 5

if MAX_SEARCH_RESULTS < 1:
    MAX_SEARCH_RESULTS = 1

if MAX_SEARCH_RESULTS > 10:
    MAX_SEARCH_RESULTS = 10