import json
from pathlib import Path

from models import ResearchAnswer


def print_result(
    result: ResearchAnswer
) -> None:
    print("\n" + "=" * 70)
    print("ANSWER")
    print("=" * 70)
    print(result.answer)

    print("\n" + "=" * 70)
    print("KEY FINDINGS")
    print("=" * 70)

    if result.key_findings:
        for finding in result.key_findings:
            print(f"- {finding}")
    else:
        print("No key findings were returned.")

    print("\n" + "=" * 70)
    print("SOURCES")
    print("=" * 70)

    for source in result.sources:
        used = ""

        if source.id in result.source_ids_used:
            used = " [used]"

        print(
            f"[{source.id}] "
            f"{source.title}{used}"
        )

        print(f"    {source.url}")

    print("=" * 70)


def save_result(
    result: ResearchAnswer,
    filename: str = "research_output.json"
) -> None:
    output_path = Path(filename)

    output_path.write_text(
        result.model_dump_json(
            indent=2
        ),
        encoding="utf-8"
    )


def save_error(
    message: str,
    filename: str = "research_output.json"
) -> None:
    error_data = {
        "success": False,
        "error": message
    }

    output_path = Path(filename)

    output_path.write_text(
        json.dumps(
            error_data,
            indent=2
        ),
        encoding="utf-8"
    )