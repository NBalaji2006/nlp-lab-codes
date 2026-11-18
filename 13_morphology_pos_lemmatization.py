"""Show simple morphological features and lemmatize tokens by POS."""
import sys

import nltk
from nltk.stem import WordNetLemmatizer


def to_wordnet_pos(tag: str) -> str:
    if tag.startswith("J"):
        return "a"
    if tag.startswith("V"):
        return "v"
    if tag.startswith("R"):
        return "r"
    return "n"


def main() -> None:
    text = " ".join(sys.argv[1:]) or input("Enter text: ")
    tagged = nltk.pos_tag(nltk.word_tokenize(text))
    lemmatizer = WordNetLemmatizer()
    for word, tag in tagged:
        lemma = lemmatizer.lemmatize(word, to_wordnet_pos(tag))
        print(f"{word:15} POS={tag:5} lemma={lemma}")


if __name__ == "__main__":
    try:
        main()
    except LookupError as exc:
        raise SystemExit(
            "Install NLTK data with: python -m nltk.downloader "
            "punkt punkt_tab averaged_perceptron_tagger averaged_perceptron_tagger_eng wordnet"
        ) from exc
