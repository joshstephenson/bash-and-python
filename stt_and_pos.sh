#!/usr/bin/env bash

usage() {
    echo "Usage: $0 AUDIO_FILE LANGUAGE"
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
        wavfile="${input%.*}.wav"
        if [ ! -f "$wavfile" ]; then
            echo "Converting to wav..."
            ./convert.py -i "$input"
        fi

        # We should have a wav file now
        input="$wavfile"
    fi

    # Now convert it to text using python script
    txtfile="${input%.*}.txt"
    if [ ! -f "$txtfile" ]; then
        echo "Converting to text..."
        ./stt.py -i "$input" -l "$language" > "$txtfile"
    fi

    input="$txtfile"
fi


# We can write data to a file and then pass it to python
tr "[:upper:]" "[:lower:]" < "$input" > /tmp/output.txt
./pos_tagger.py -f /tmp/output.txt

# Or we can just pass the data via a pipe
tr "[:upper:]" "[:lower:]" < "$input" | ./pos_tagger.py

