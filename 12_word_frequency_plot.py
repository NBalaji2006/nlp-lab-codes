"""Plot word frequencies after removing English stop words and punctuation."""
import re
import sys
from collections import Counter

import matplotlib.pyplot as plt
from nltk.corpus import stopwords


def main() -> None:
    text = " ".join(sys.argv[1:]) or input("Enter text: ")
    try:
        ignored = set(stopwords.words("english"))
    except LookupError as exc:
        raise SystemExit("Install NLTK data with: python -m nltk.downloader stopwords") from exc
    words = [
        word for word in re.findall(r"\b[\w']+\b", text.lower())
        if word not in ignored and not word.isnumeric()
    ]
    counts = Counter(words)
    if not counts:
        raise SystemExit("No words remain after filtering.")
    common = counts.most_common(20)
    labels, frequencies = zip(*common)
    plt.figure(figsize=(10, 5))
    plt.bar(labels, frequencies)
    plt.xlabel("Word")
    plt.ylabel("Frequency")
    plt.title("Most frequent words (stop words and punctuation removed)")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
