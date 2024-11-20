#!/usr/bin/env python
import sys
import spacy
from collections import Counter, defaultdict

es_nlp = spacy.load('es_core_news_sm')
if sys.stdin.isatty():
    print("Didn't pass anything via STDIN")
    exit(1)
text = sys.stdin.read()

spanish = es_nlp(text.strip())
info = defaultdict(list)
counter = Counter([token.pos_ for token in spanish])
for token in spanish:
    if token.text:
        info[token.pos_].append(token.text)

for pos, words in info.items():
    count = counter[pos]
    sys.stdout.write(f'{pos} ({count}): {",".join(sorted(words))}' + '\n')

