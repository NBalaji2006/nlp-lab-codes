"""Recognize sheep-talk strings using a regular-expression FSA.

This example defines a sheep utterance as one or more 'b' characters followed by
at least one 'a', optionally followed by whitespace-separated utterances.
"""
import re


SHEEPTALK = re.compile(r"^(?:ba+)(?:\s+ba+)*$", re.IGNORECASE)


def main() -> None:
    text = input("Enter a sheep-talk string (for example, 'baa baaa'): ").strip()
    print("Accepted" if SHEEPTALK.fullmatch(text) else "Rejected")


if __name__ == "__main__":
    main()
