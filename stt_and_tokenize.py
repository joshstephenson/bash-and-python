#!/usr/bin/env bash

usage() {
    echo "Tokenizes audio or text files. Audio files will be converted to text first."
    echo "Usage: $0 FILE LANGUAGE"
    exit 1
}

if [ "$#" -lt 2 ]; then
    usage
fi

input="$1"
language="$2"

# If the input is not a txt file we need to convert it to one
if [[ ! "$input" =~ txt$ ]]; then

    # If it's also not a wav file, then we need to first convert it to a wav file before converting it to text
    if [[ ! "$input" =~ wav$ ]]; then
        output="${input%.*}.wav"
        if [ ! -f "$output" ]; then
            echo "Converting to wav..."
            ./convert.py -i "$input"
        fi

        # We should have a wav file now
        input="$output"
    fi

    # Now convert it to text using python script
    output="${input%.*}.txt"
    if [ ! -f "$output" ]; then
        echo "Converting to text..."
        ./stt.py -i "$input" -l "$language" > "$output"
    fi

    input="$output"
fi

# Tokenize and then pass to python to analyze
tr "[:upper:]" "[:lower:]" < "$input" \
    | ./tokenize.py

