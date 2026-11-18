"""Recognize sentences with the example context-free grammar using CYK.

The grammar is in Chomsky Normal Form. Edit the production tables to use a
different grammar.
"""

LEXICON = {
    "Det": {"the", "a"},
    "N": {"cat", "dog", "mouse"},
    "V": {"sees", "likes", "chases"},
}
RULES = {
    ("NP", "VP"): {"S"},
    ("Det", "N"): {"NP"},
    ("V", "NP"): {"VP"},
}


def cyk(words: list[str]) -> tuple[bool, list[list[set[str]]]]:
    size = len(words)
    if not size:
        return False, []
    table = [[set() for _ in range(size)] for _ in range(size)]
    for index, word in enumerate(words):
        for category, vocabulary in LEXICON.items():
            if word in vocabulary:
                table[index][index].add(category)
    for span in range(2, size + 1):
        for start in range(size - span + 1):
            end = start + span - 1
            for split in range(start, end):
                for left in table[start][split]:
                    for right in table[split + 1][end]:
                        table[start][end].update(RULES.get((left, right), set()))
    return "S" in table[0][size - 1], table


def main() -> None:
    words = input("Enter a sentence (example: the cat sees a dog): ").lower().split()
    accepted, table = cyk(words)
    print("String belongs to the grammar." if accepted else "String does not belong to the grammar.")
    if table:
        print("CYK table:")
        for row in table:
            print(row)


if __name__ == "__main__":
    main()
