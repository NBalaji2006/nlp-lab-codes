"""POS-tag a sentence and display its shallow parsed tree."""
import sys

import nltk


def main() -> None:
    sentence = " ".join(sys.argv[1:]) or input("Enter a sentence: ")
    tagged = nltk.pos_tag(nltk.word_tokenize(sentence))
    print("POS tags:", tagged)
    grammar = r"""
        NP: {<DT>?<JJ.*>*<NN.*>+}
        VP: {<VB.*><NP|PP>*}
        PP: {<IN><NP>}
    """
    tree = nltk.RegexpParser(grammar).parse(tagged)
    print("Parsed tree:")
    print(tree)
    tree.draw()


if __name__ == "__main__":
    try:
        main()
    except LookupError as exc:
        raise SystemExit(
            "NLTK tokenizer/tagger data is missing. Run: "
            "python -m nltk.downloader punkt punkt_tab averaged_perceptron_tagger "
            "averaged_perceptron_tagger_eng"
        ) from exc
