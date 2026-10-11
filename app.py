from config import OPENAI_MODEL, MAX_SEARCH_RESULTS
from researcher import ResearchError, generate_research_answer
from search import SearchError, search_web
from utils import print_result, save_error, save_result


def get_question() -> str:
    print("=" * 70)
    print("AI RESEARCH ASSISTANT")
    print("=" * 70)
    print(f"Model: {OPENAI_MODEL}")
    print(f"Maximum search results: {MAX_SEARCH_RESULTS}")
    print()

    return input("Enter your research question: ").strip()


def main() -> None:
    try:
        question = get_question()

        if not question:
            message = "Question cannot be empty."
            print(f"\nError: {message}")
            save_error(message)
            return

        print("\nSearching external sources...")
        sources = search_web(question)

        if not sources:
            message = (
                "No search results found. "
                "Try using a more specific question."
            )
            print(f"\nError: {message}")
            save_error(message)
            return

        print(f"Found {len(sources)} source(s).")
        print("Generating structured answer...")

        result = generate_research_answer(
            question=question,
            sources=sources
        )

        print_result(result)
        save_result(result)

        print("\nSaved result to research_output.json")

    except SearchError as error:
        print(f"\nSearch error: {error}")
        save_error(str(error))

    except ResearchError as error:
        print(f"\nResearch error: {error}")
        save_error(str(error))

    except KeyboardInterrupt:
        print("\n\nProgram cancelled by user.")

    except Exception as error:
        print(f"\nUnexpected error: {error}")
        save_error(str(error))


if __name__ == "__main__":
    main()