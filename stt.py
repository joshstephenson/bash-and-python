#!/usr/bin/env python

import speech_recognition as sr
import sys

def get_text(filename, language_code):
    r = sr.Recognizer()
    with sr.AudioFile(filename) as source:
        d = r.record(source)
        text = r.recognize_google(d, language=language_code)
        sys.stdout.write(text + '\n')

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", '--input', required=True, type=str)
    parser.add_argument('-l', '--language', required=True, type=str, default='es-LA',
                        help='Choose a language code from: https://www.science.co.il/language/Locale-codes.php')
    args = parser.parse_args()
    filename = args.input
    if not filename.lower().endswith('wav'):
        raise BaseException('This file needs a wav audio file. Please use convert.py first.')
    get_text(filename,args.language)
