"""Compare common NLTK stemmers with WordNet lemmatization."""
import sys

from nltk.stem import LancasterStemmer, PorterStemmer, SnowballStemmer, WordNetLemmatizer


def main() -> None:
    words = sys.argv[1:] or input("Enter words separated by spaces: ").split()
    porter, lancaster = PorterStemmer(), LancasterStemmer()
    snowball, lemmatizer = SnowballStemmer("english"), WordNetLemmatizer()
    try:
        for word in words:
            print(
                f"{word:15} Porter={porter.stem(word):12} "
                f"Lancaster={lancaster.stem(word):10} "
                f"Snowball={snowball.stem(word):12} "
                f"Lemma={lemmatizer.lemmatize(word)}"
            )
    except LookupError as exc:
        raise SystemExit(
            "Install the WordNet data with: python -m nltk.downloader wordnet"
        ) from exc


if __name__ == "__main__":
    main()
