"""Extract noun-phrase-like chunks from a sentence with NLTK chunking."""
import sys

import nltk


def main() -> None:
    sentence = " ".join(sys.argv[1:]) or input("Enter a sentence: ")
    tokens = nltk.word_tokenize(sentence)
    tagged = nltk.pos_tag(tokens)
    grammar = r"""
        NP: {<DT>?<JJ.*>*<NN.*>+}
        VP: {<VB.*><NP|PP>*}
    """
    chunks = nltk.RegexpParser(grammar).parse(tagged)
    print(chunks)
    print("Noun phrases:", [" ".join(word for word, _ in subtree.leaves())
                            for subtree in chunks.subtrees(lambda node: node.label() == "NP")])


if __name__ == "__main__":
    try:
        main()
    except LookupError as exc:
        raise SystemExit(
            "NLTK tokenizer/tagger data is missing. Run: "
            "python -m nltk.downloader punkt punkt_tab averaged_perceptron_tagger "
            "averaged_perceptron_tagger_eng"
        ) from exc
