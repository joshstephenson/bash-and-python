# bash-and-python
## Files
- `./convert.py` Python script that converts M4A or MP3 audio files to WAV (necessary for stt.py) using `pydub`.
- `./stt.py` Python script that converts speech to text using `SpeechRecognizer`.
- `./pos_tagger.py` Python script that tags parts of speech using `Spacy`.
- `./stt_and_pos.sh` BASH script that will first convert audio file to text (if necessary) and then pass to `pos_tagger.py`
- `./calling_bash_from_python.py` Super basic python script that demonstrates how to run a unix command from python and retrieve the result
- `./files/english.mp3` English audio sample
- `./files/spanish.m4a` Spanish audio sample

## Setup the environment
First, create an environment with `python -m venv <directory>` or `conda create -n test_env python=3.12 <name>` and activate with `source <directory>/bin/activate` or `conda activate <name>` respectively.
Next install the requirements with:
`pip install -r requirements.yml`

If that goes well, you have all the necessary packages to run the scripts.

## Passing data from terminal to python
You can write a python script to take data with command-line arguments 
See `stt_and_pos.sh` (Speech-to-text and part-of-speech tagger)
```
./stt_and_pos.sh files/english.mp3 en-US
```
OR
```
./stt_and_pos.sh files/spanish.mpa es-LA
```

## Calling a unix command from python
See `calling_bash_from_python.py`
