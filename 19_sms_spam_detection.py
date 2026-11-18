"""Train an SMS spam classifier from a labeled spam.csv dataset.

Usage: python 19_sms_spam_detection.py spam.csv
Automatically supports the common Kaggle columns v1 (label), v2 (message).
"""
import argparse
from pathlib import Path

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline


def find_column(columns: list[str], preferred: list[str]) -> str | None:
    normalized = {column.lower().strip(): column for column in columns}
    return next((normalized[name] for name in preferred if name in normalized), None)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("csv", nargs="?", default="spam.csv")
    parser.add_argument("--text-column")
    parser.add_argument("--label-column")
    args = parser.parse_args()
    path = Path(args.csv)
    if not path.is_file():
        raise SystemExit(f"CSV file not found: {path}")
    data = pd.read_csv(path, encoding="latin-1")
    text_column = args.text_column or find_column(
        list(data.columns), ["v2", "message", "sms", "text"]
    )
    label_column = args.label_column or find_column(
        list(data.columns), ["v1", "label", "category", "class", "target"]
    )
    if not text_column or not label_column:
        raise SystemExit(
            f"Could not identify message and label columns. CSV columns: {list(data.columns)}. "
            "Pass --text-column and --label-column."
        )
    data = data[[text_column, label_column]].dropna()
    labels = data[label_column].astype(str)
    if labels.nunique() < 2:
        raise SystemExit("At least two classes (for example, ham and spam) are required.")
    x_train, x_test, y_train, y_test = train_test_split(
        data[text_column].astype(str), labels, test_size=0.2, random_state=42, stratify=labels
    )
    model = Pipeline([
        ("tfidf", TfidfVectorizer(lowercase=True, stop_words="english")),
        ("classifier", LogisticRegression(max_iter=1000)),
    ])
    model.fit(x_train, y_train)
    predictions = model.predict(x_test)
    print("Confusion matrix (rows=true, columns=predicted):")
    print(confusion_matrix(y_test, predictions, labels=sorted(labels.unique())))
    print(classification_report(y_test, predictions, zero_division=0))
    for message, label in zip(
        data[text_column].astype(str).head(5),
        model.predict(data[text_column].astype(str).head(5)),
    ):
        print(f"{label}: {message[:160]}")


if __name__ == "__main__":
    main()
