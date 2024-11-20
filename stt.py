#!/usr/bin/env python

import speech_recognition as sr
import sys
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-f", '--file', required=True, type=str)
parser.add_argument('-l', '--language', required=True, type=str, default='es-LA',
                    help='Choose a language code from: https://www.science.co.il/language/Locale-codes.php')
args = parser.parse_args()
if not args.file.endswith('wav'):
    parser.error('file must be wave file')

r = sr.Recognizer()
with sr.AudioFile(args.file) as source:
    d = r.record(source)
    text = r.recognize_google(d, language=args.language)
    sys.stdout.write(text + '\n')

