import json
from typing import List

from openai import OpenAI

from config import OPENAI_API_KEY, OPENAI_MODEL
from models import ResearchAnswer, Source


class ResearchError(Exception):
    pass


def build_sources_text(
    sources: List[Source]
) -> str:
    blocks = []

    for source in sources:
        block = f"""
SOURCE ID: {source.id}
TITLE: {source.title}
URL: {source.url}
CONTENT:
{source.content}
"""

        blocks.append(block)

    return "\n".join(blocks)


def build_prompt(
    question: str,
    sources: List[Source]
) -> str:
    sources_text = build_sources_text(sources)

    return f"""
You are a careful AI research assistant.

Research question:
{question}

Use only the sources provided below.

Return valid JSON only.
Do not use Markdown code fences.

The JSON must have exactly these fields:
{{
  "answer": "A clear answer to the question.",
  "key_findings": [
    "Finding one with citation [1].",
    "Finding two with citation [2]."
  ],
  "source_ids_used": [1, 2]
}}

Rules:
1. Cite factual claims with [1], [2], or another valid source ID.
2. Use only source IDs that exist.
3. Do not invent facts or citations.
4. If sources disagree, explain the disagreement.
5. If evidence is insufficient, say so clearly.
6. Keep the answer concise and useful.

Available sources:
{sources_text}
"""


def generate_research_answer(
    question: str,
    sources: List[Source]
) -> ResearchAnswer:
    if not sources:
        raise ResearchError(
            "No sources are available for synthesis."
        )

    prompt = build_prompt(
        question,
        sources
    )

    try:
        client = OpenAI(
            api_key=OPENAI_API_KEY
        )

        response = client.responses.create(
            model=OPENAI_MODEL,
            input=prompt
        )

        raw_text = response.output_text.strip()

    except Exception as error:
        raise ResearchError(
            f"LLM request failed: {error}"
        ) from error

    if not raw_text:
        raise ResearchError(
            "The LLM returned an empty response."
        )

    try:
        parsed = json.loads(raw_text)

    except json.JSONDecodeError as error:
        raise ResearchError(
            "The LLM returned invalid JSON."
        ) from error

    answer = parsed.get("answer", "")
    key_findings = parsed.get(
        "key_findings",
        []
    )
    source_ids_used = parsed.get(
        "source_ids_used",
        []
    )

    if not isinstance(answer, str):
        raise ResearchError(
            "The answer field must be text."
        )

    if not isinstance(key_findings, list):
        raise ResearchError(
            "The key_findings field must be a list."
        )

    if not isinstance(source_ids_used, list):
        raise ResearchError(
            "The source_ids_used field must be a list."
        )

    return ResearchAnswer(
        question=question,
        answer=answer,
        key_findings=key_findings,
        source_ids_used=source_ids_used,
        sources=sources
    )