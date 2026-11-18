"""Print word n-grams after removing English stop words."""
import re
import sys

from nltk.corpus import stopwords
from nltk.util import ngrams


def main() -> None:
    text = " ".join(sys.argv[1:]) or input("Enter text: ")
    try:
        ignored = set(stopwords.words("english"))
    except LookupError as exc:
        raise SystemExit("Install NLTK data with: python -m nltk.downloader stopwords") from exc
    words = [word for word in re.findall(r"\b[\w']+\b", text.lower()) if word not in ignored]
    n = int(input("Enter n for n-grams: "))
    if n < 1:
        raise SystemExit("n must be a positive integer.")
    print(list(ngrams(words, n)))


if __name__ == "__main__":
    main()
