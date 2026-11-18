"""A small Viterbi example for the sentence 'free workers'."""
from math import log


STATES = ("JJ", "NN", "NNS")
START = {"JJ": 0.1, "NN": 0.6, "NNS": 0.3}
TRANSITION = {
    "JJ": {"JJ": 0.05, "NN": 0.35, "NNS": 0.60},
    "NN": {"JJ": 0.20, "NN": 0.30, "NNS": 0.50},
    "NNS": {"JJ": 0.30, "NN": 0.20, "NNS": 0.50},
}
EMISSION = {
    "free": {"JJ": 0.70, "NN": 0.20, "NNS": 0.10},
    "workers": {"JJ": 0.01, "NN": 0.09, "NNS": 0.90},
}


def viterbi(words: list[str]) -> tuple[list[str], float]:
    scores = {state: log(START[state]) + log(EMISSION[words[0]][state]) for state in STATES}
    paths = {state: [state] for state in STATES}
    for word in words[1:]:
        next_scores, next_paths = {}, {}
        for current in STATES:
            choices = [
                (scores[previous] + log(TRANSITION[previous][current])
                 + log(EMISSION[word][current]), previous)
                for previous in STATES
            ]
            score, previous = max(choices)
            next_scores[current] = score
            next_paths[current] = paths[previous] + [current]
        scores, paths = next_scores, next_paths
    best = max(STATES, key=scores.get)
    return paths[best], scores[best]


def main() -> None:
    words = input("Enter sentence (default: free workers): ").lower().split() or ["free", "workers"]
    if any(word not in EMISSION for word in words):
        raise SystemExit("This demonstration's toy HMM supports only: free workers")
    tags, log_probability = viterbi(words)
    print("Most probable POS tags:", list(zip(words, tags)))
    print(f"Log probability: {log_probability:.4f}")


if __name__ == "__main__":
    main()
