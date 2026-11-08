import re
import statistics
import sys
import time
from pathlib import Path

# Allow imports from the backend directory.
BACKEND_DIR = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(BACKEND_DIR))

from app.services.ai_extraction_service import (
    OLLAMA_MODEL,
    extract_assignment_details,
)

BENCHMARK_CASES = [
    {
        "name": "Clear assignment",
        "document": """
ASSIGNMENT 1: LIBRARY DATABASE DESIGN

Submission deadline: 20 November 2026

Requirements:
1. Design an ER diagram for a library database.
2. Create the database using MySQL.
3. Submit a report explaining your design.
""",
        "expected": {
            "title": "ASSIGNMENT 1: LIBRARY DATABASE DESIGN",
            "due_date": "2026-11-20",
            "requirements": [
                "1. Design an ER diagram for a library database.",
                "2. Create the database using MySQL.",
                "3. Submit a report explaining your design.",
            ],
        },
    },
    {
        "name": "Assignment without deadline",
        "document": """
WEB DEVELOPMENT MINI PROJECT

Presentation date: 18 November 2026

Requirements:
1. Build a responsive website using React.
2. Include a contact form.
3. Submit the project source code.
""",
        "expected": {
            "title": "WEB DEVELOPMENT MINI PROJECT",
            "due_date": None,
            "requirements": [
                "1. Build a responsive website using React.",
                "2. Include a contact form.",
                "3. Submit the project source code.",
            ],
        },
    },
    {
        "name": "Multiple dates",
        "document": """
MOBILE APP DEVELOPMENT ASSIGNMENT

Release date: 1 November 2026
Demo date: 15 November 2026
Submission deadline: 22 November 2026

Requirements:
1. Develop a mobile application prototype.
2. Prepare a demonstration of the application.
""",
        "expected": {
            "title": "MOBILE APP DEVELOPMENT ASSIGNMENT",
            "due_date": "2026-11-22",
            "requirements": [
                "1. Develop a mobile application prototype.",
                "2. Prepare a demonstration of the application.",
            ],
        },
    },
    {
        "name": "Non-assignment document",
        "document": """
STUDENT NOTICE

The campus library will close at 5 PM on 12 November 2026.

Students should return borrowed books before the closure.
""",
        "expected": {
            "title": None,
            "due_date": None,
            "requirements": [],
        },
    },
]


def normalize(value):
    """Normalize text for case-insensitive comparison."""
    return " ".join(str(value).casefold().split())


def normalize_requirement(value):
    """Ignore numbering and bullet markers during comparison."""
    value = normalize(value)
    return re.sub(r"^(?:\d+[.)]\s*|[-*•]\s*)", "", value)


def compare_result(actual, expected):
    """Compare accepted extraction fields against expected values."""

    actual_title = actual.title
    expected_title = expected["title"]

    title_correct = (
        normalize(actual_title) == normalize(expected_title)
        if actual_title is not None and expected_title is not None
        else actual_title is expected_title
    )

    actual_due_date = (
        actual.due_date.isoformat() if actual.due_date is not None else None
    )

    due_date_correct = actual_due_date == expected["due_date"]

    actual_requirements = [normalize_requirement(item) for item in actual.requirements]

    expected_requirements = [
        normalize_requirement(item) for item in expected["requirements"]
    ]

    requirements_correct = actual_requirements == expected_requirements

    return {
        "title": title_correct,
        "due_date": due_date_correct,
        "requirements": requirements_correct,
    }


def print_requirement_comparison(actual, expected):
    """Display actual and expected requirements."""

    actual_requirements = [normalize_requirement(item) for item in actual.requirements]

    expected_requirements = [
        normalize_requirement(item) for item in expected["requirements"]
    ]

    print("\n  Actual requirements:")

    if actual.requirements:
        for index, item in enumerate(actual.requirements, start=1):
            print(f"    {index}. {item}")
    else:
        print("    None")

    print("\n  Expected requirements:")

    if expected["requirements"]:
        for index, item in enumerate(expected["requirements"], start=1):
            print(f"    {index}. {item}")
    else:
        print("    None")

    print("\n  Requirement diagnosis:")

    missing = [
        item for item in expected_requirements if item not in actual_requirements
    ]

    unexpected = [
        item for item in actual_requirements if item not in expected_requirements
    ]

    if not missing and not unexpected:
        print("    All requirements match.")
    else:
        if missing:
            print("    Missing requirements:")
            for item in missing:
                print(f"      - {item}")

        if unexpected:
            print("    Unexpected or modified requirements:")
            for item in unexpected:
                print(f"      - {item}")


def print_evidence(actual):
    """Display evidence returned by the model."""

    print("\n  Evidence returned by model:")
    print(f"    Title evidence: {actual.title_evidence}")
    print(f"    Due-date evidence: {actual.due_date_evidence}")

    if actual.requirement_evidence:
        print("    Requirement evidence:")

        for index, evidence in enumerate(actual.requirement_evidence, start=1):
            print(f"      {index}. {evidence}")
    else:
        print("    Requirement evidence: None")


def main():
    results = []
    latencies = []

    print("=" * 65)
    print("DEADLINEOS - AI EXTRACTION BENCHMARK")
    print("=" * 65)
    print(f"Model: {OLLAMA_MODEL}")
    print(f"Test cases: {len(BENCHMARK_CASES)}")
    print()

    for index, case in enumerate(BENCHMARK_CASES, start=1):
        print(f"[{index}/{len(BENCHMARK_CASES)}] {case['name']}")

        start = time.perf_counter()

        try:
            actual = extract_assignment_details(case["document"])
            elapsed = time.perf_counter() - start
            latencies.append(elapsed)

            checks = compare_result(actual, case["expected"])
            passed = all(checks.values())

            result = {
                "name": case["name"],
                "passed": passed,
                "latency": elapsed,
                "checks": checks,
                "error": None,
            }

            print(f"  Result: {'PASS' if passed else 'FAIL'}")
            print(f"  Title correct: {checks['title']}")
            print(f"  Due date correct: {checks['due_date']}")
            print(f"  Requirements correct: {checks['requirements']}")

            if not checks["requirements"]:
                print_requirement_comparison(
                    actual,
                    case["expected"],
                )

            print_evidence(actual)

        except Exception as exc:  # noqa: BLE001
            # Record failures and continue running the remaining benchmark cases.
            elapsed = time.perf_counter() - start
            latencies.append(elapsed)

            result = {
                "name": case["name"],
                "passed": False,
                "latency": elapsed,
                "checks": {
                    "title": False,
                    "due_date": False,
                    "requirements": False,
                },
                "error": f"{type(exc).__name__}: {exc}",
            }

            print("  Result: ERROR")
            print(f"  Error: {result['error']}")

        print(f"\n  Response time: {elapsed:.2f} seconds")
        print("-" * 65)
        print()

        results.append(result)

    total = len(results)
    passed_count = sum(result["passed"] for result in results)
    error_count = sum(result["error"] is not None for result in results)

    field_names = ("title", "due_date", "requirements")

    field_totals = {
        field: sum(result["checks"][field] for result in results)
        for field in field_names
    }

    print("=" * 65)
    print("BENCHMARK SUMMARY")
    print("=" * 65)

    print(f"Total cases: {total}")
    print(f"Passed cases: {passed_count}")
    print(f"Failed cases: {total - passed_count}")
    print(f"Execution errors: {error_count}")
    print(f"Case success rate: {passed_count / total * 100:.1f}%")

    print("\nField accuracy:")

    for field, correct in field_totals.items():
        print(f"  {field}: {correct}/{total} ({correct / total * 100:.1f}%)")

    if latencies:
        print("\nResponse time:")
        print(f"  Average: {statistics.mean(latencies):.2f}s")
        print(f"  Median: {statistics.median(latencies):.2f}s")
        print(f"  Fastest: {min(latencies):.2f}s")
        print(f"  Slowest: {max(latencies):.2f}s")

    print("\nIndividual results:")

    for result in results:
        status = "PASS" if result["passed"] else "FAIL"

        print(f"  {status} | {result['name']} | {result['latency']:.2f}s")

    print("\nBenchmark completed.")


if __name__ == "__main__":
    main()
