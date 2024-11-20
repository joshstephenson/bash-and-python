#!/usr/bin/env python
import sys
import spacy
from collections import Counter, defaultdict
import argparse

parser = argparse.ArgumentParser()
group = parser.add_mutually_exclusive_group(required=True)
group.add_argument('-f', '--file', type=str)
group.add_argument('-i', '--stdin', action='store_true')
args = parser.parse_args()
print(args)

es_nlp = spacy.load('es_core_news_sm')
if args.file is not None:
    with open(args.file) as f:
        text = f.read()
elif args.stdin:
    text = sys.stdin.read()

spanish = es_nlp(text.strip())
info = defaultdict(list)
counter = Counter([token.pos_ for token in spanish])
for token in spanish:
    if token.text:
        info[token.pos_].append(token.text)

for pos, words in info.items():
    count = counter[pos]
    sys.stdout.write(f'{pos} ({count}): {sorted(words)}' + '\n')

