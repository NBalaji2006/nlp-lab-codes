NLP Laboratory programs
=======================

Each numbered Python file is a separate answer to one question in NLP LAB PROGRAMS.docx.
Use Python 3.10 or newer. Install dependencies with:

    python -m pip install -r requirements.txt

NLTK resource setup (needed only by the corresponding NLTK programs):

    python -m nltk.downloader stopwords wordnet punkt punkt_tab
    python -m nltk.downloader averaged_perceptron_tagger averaged_perceptron_tagger_eng

Run an individual program from this folder, for example:

    python 03_count_nineteen_five.py
    python 01_extract_patterns.py input.txt
    python 18_vaccination_tweets_sentiment.py vaccination_tweets.csv
    python 19_sms_spam_detection.py spam.csv

The two CSV case studies expect labeled datasets. If the text/label columns are not
recognized automatically, provide them with --text-column and --label-column.
The sheep-talk program uses the example grammar documented at the top of its file.
The CYK program uses a small example CNF grammar that can be edited in that file.
