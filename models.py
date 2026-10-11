from typing import List

from pydantic import BaseModel, Field


class Source(BaseModel):
    id: int
    title: str
    url: str
    content: str


class ResearchAnswer(BaseModel):
    question: str
    answer: str
    key_findings: List[str] = Field(
        default_factory=list
    )
    source_ids_used: List[int] = Field(
        default_factory=list
    )
    sources: List[Source] = Field(
        default_factory=list
    )