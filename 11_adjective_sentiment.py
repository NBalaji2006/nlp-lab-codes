"""Extract nouns/adjectives and score extracted adjectives with TextBlob."""
import sys

import nltk
from textblob import TextBlob


def main() -> None:
    sentence = " ".join(sys.argv[1:]) or input("Enter a sentence: ")
    tagged = nltk.pos_tag(nltk.word_tokenize(sentence))
    nouns = [word for word, tag in tagged if tag.startswith("NN")]
    adjectives = [word for word, tag in tagged if tag.startswith("JJ")]
    scores = [(word, TextBlob(word).sentiment.polarity) for word in adjectives]
    overall = sum(score for _, score in scores) / len(scores) if scores else 0.0
    print("Nouns:", nouns)
    print("Adjectives:", adjectives)
    print("Adjective sentiment scores:", scores)
    print(f"Overall adjective sentiment: {overall:.3f}")


if __name__ == "__main__":
    try:
        main()
    except LookupError as exc:
        raise SystemExit(
            "NLTK tokenizer/tagger data is missing. Run: "
            "python -m nltk.downloader punkt punkt_tab averaged_perceptron_tagger "
            "averaged_perceptron_tagger_eng"
        ) from exc
