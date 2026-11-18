"""Tokenize text, remove stop words, and stem the remaining words."""
import re
import sys

from nltk.corpus import stopwords
from nltk.stem import PorterStemmer


def main() -> None:
    text = " ".join(sys.argv[1:]) or input("Enter text: ")
    tokens = re.findall(r"\b[\w']+\b", text.lower())
    try:
        ignored = set(stopwords.words("english"))
    except LookupError as exc:
        raise SystemExit("Install NLTK data with: python -m nltk.downloader stopwords") from exc
    filtered = [word for word in tokens if word not in ignored]
    stemmer = PorterStemmer()
    print("Tokens:", tokens)
    print("Without stop words:", filtered)
    print("Stemmed:", [stemmer.stem(word) for word in filtered])


if __name__ == "__main__":
    main()
