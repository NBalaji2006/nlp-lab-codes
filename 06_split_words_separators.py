"""Split text into word and separator lists, preserving comma-space separators."""
import re


def split_words_and_separators(text: str) -> tuple[list[str], list[str]]:
    words = re.findall(r"[A-Za-z]+(?:'[A-Za-z]+)*\.?", text)
    separators = re.findall(r"[, ]+", text)
    return words, separators


def main() -> None:
    text = input("Enter words separated by commas and spaces: ")
    words, separators = split_words_and_separators(text)
    print([words, separators])


if __name__ == "__main__":
    main()
