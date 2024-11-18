#!/usr/bin/env python
import sys
import re

def main(opts):
    file = open(opts.file, 'r', encoding='utf-8') if type(opts.file) == str else opts.file
    words = re.split(r'\W+', file.read())
    uniq = list(set(words))
    sorted_uniq = sorted(uniq)
    file.close()
    for w in sorted_uniq:
        sys.stdout.write(w + '\n')


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--file', type=str, default=sys.stdin)
    args = parser.parse_args()
    main(args)
