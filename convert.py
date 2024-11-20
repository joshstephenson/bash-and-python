#!/usr/bin/env python
from pydub import AudioSegment

def main(filename):
    """
    Assumes the extension is also the source file format. May not be a good assumption.
    """
    source = filename.split('.')[-1]
    output = filename.replace(source, 'wav')
    sound = AudioSegment.from_file(filename, format=source)
    file_handle = sound.export(output, format='wav')
    return output

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", '--file', required=True, type=str)
    args = parser.parse_args()
    main(args.file)
