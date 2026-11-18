"""Count bigrams in a collection of three documents and show the top five."""
import re
from collections import Counter


def main() -> None:
    documents = []
    for index in range(1, 4):
        documents.append(input(f"Enter document {index}: "))
    counts: Counter[tuple[str, str]] = Counter()
    for document in documents:
        words = re.findall(r"\b[\w']+\b", document.lower())
        counts.update(zip(words, words[1:]))
    print("Distinct bigrams:", len(counts))
    print("Top five:")
    for bigram, frequency in counts.most_common(5):
        print(f"{' '.join(bigram)}: {frequency}")


if __name__ == "__main__":
    main()
