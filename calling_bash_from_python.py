#!/usr/bin/env python

import subprocess

def main():
    foo = subprocess.run(['date'], capture_output=True)
    print(foo.stdout.decode('utf-8'))

main()