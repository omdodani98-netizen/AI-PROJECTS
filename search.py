from typing import List

from tavily import TavilyClient

from config import MAX_SEARCH_RESULTS, TAVILY_API_KEY
from models import Source


class SearchError(Exception):
    pass


def search_web(question: str) -> List[Source]:
    if not question.strip():
        raise SearchError(
            "The search question cannot be empty."
        )

    try:
        tavily_client = TavilyClient(
            api_key=TAVILY_API_KEY
        )

        response = tavily_client.search(
            query=question,
            search_depth="basic",
            max_results=MAX_SEARCH_RESULTS,
            include_answer=False
        )

    except Exception as error:
        raise SearchError(
            f"Web search failed: {error}"
        ) from error

    results = response.get("results", [])

    if not results:
        return []

    sources = []

    for index, result in enumerate(results, start=1):
        title = str(
            result.get(
                "title",
                "Untitled source"
            )
        )

        url = str(
            result.get(
                "url",
                ""
            )
        )

        content = str(
            result.get(
                "content",
                ""
            )
        )

        if not url:
            continue

        source = Source(
            id=index,
            title=title,
            url=url,
            content=content
        )

        sources.append(source)

    return sources