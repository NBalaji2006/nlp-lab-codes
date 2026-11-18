"""Train and evaluate a text sentiment classifier on a labeled tweets CSV.

Usage: python 18_vaccination_tweets_sentiment.py vaccination_tweets.csv
The CSV must contain a tweet-text column and a sentiment/label column.
"""
import argparse
from pathlib import Path

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline


def find_column(columns: list[str], preferred: list[str]) -> str | None:
    normalized = {column.lower().strip(): column for column in columns}
    return next((normalized[name] for name in preferred if name in normalized), None)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("csv", nargs="?", default="vaccination_tweets.csv")
    parser.add_argument("--text-column")
    parser.add_argument("--label-column")
    args = parser.parse_args()
    path = Path(args.csv)
    if not path.is_file():
        raise SystemExit(f"CSV file not found: {path}")
    data = pd.read_csv(path)
    text_column = args.text_column or find_column(
        list(data.columns), ["text", "tweet", "tweets", "content"]
    )
    label_column = args.label_column or find_column(
        list(data.columns), ["sentiment", "label", "class", "target"]
    )
    if not text_column or not label_column:
        raise SystemExit(
            f"Could not identify text and sentiment columns. CSV columns: {list(data.columns)}. "
            "Pass --text-column and --label-column."
        )
    data = data[[text_column, label_column]].dropna()
    if data[label_column].nunique() < 2:
        raise SystemExit("At least two sentiment classes are required.")
    x_train, x_test, y_train, y_test = train_test_split(
        data[text_column].astype(str), data[label_column].astype(str),
        test_size=0.2, random_state=42, stratify=data[label_column].astype(str),
    )
    model = Pipeline([
        ("tfidf", TfidfVectorizer(stop_words="english", max_features=10000)),
        ("classifier", LogisticRegression(max_iter=1000)),
    ])
    model.fit(x_train, y_train)
    print(classification_report(y_test, model.predict(x_test), zero_division=0))
    for tweet, sentiment in zip(
        data[text_column].astype(str).head(5),
        model.predict(data[text_column].astype(str).head(5)),
    ):
        print(f"{sentiment}: {tweet[:160]}")


if __name__ == "__main__":
    main()
