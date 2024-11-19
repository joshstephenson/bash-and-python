#!/usr/bin/env python
import sys
import spacy
from collections import Counter, defaultdict


def main(opts):
    es_nlp = spacy.load('es_core_news_sm')
    if opts.file is not None:
        with open(opts.file) as f:
            text = f.read()
    else:
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


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--file', type=str, required=False)
    args = parser.parse_args()
    main(args)
