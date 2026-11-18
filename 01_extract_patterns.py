"""Extract email addresses, dates, and phone numbers from a text file."""
import re
import sys
from pathlib import Path


PATTERNS = {
    "Email addresses": r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b",
    "Dates": r"\b(?:\d{1,2}[/-]\d{1,2}[/-]\d{2,4}|\d{4}-\d{2}-\d{2})\b",
    "Phone numbers": r"(?<!\w)(?:\+?\d{1,3}[-.\s]?)?(?:\(?\d{3,5}\)?[-.\s]?)\d{3,5}[-.\s]?\d{3,5}(?!\w)",
}


def main() -> None:
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("input.txt")
    if not path.is_file():
        raise SystemExit(f"Input file not found: {path}")
    text = path.read_text(encoding="utf-8")
    for label, pattern in PATTERNS.items():
        print(f"\n{label}:")
        matches = re.findall(pattern, text)
        print("\n".join(f"- {item}" for item in matches) if matches else "None found")


if __name__ == "__main__":
    main()
