# BASH + Python
There are times when you want to create a python script that acts like a command line tool (native unix command), and there are times when you want to call a native unix command from Python.

## Files
- `./convert.py` Python script that converts M4A or MP3 audio files to WAV (necessary for `stt.py`) using `pydub`.
- `./stt.py` Python script that converts speech to text using `SpeechRecognizer`.
- `./pos_tagger.py` Python script that tags parts of speech using `Spacy`.
- `./stt_and_pos.sh` BASH script that will first convert audio file to text (if necessary) and then pass to `pos_tagger.py`.
- `./calling_bash_from_python.py` Super basic python script that demonstrates how to run a unix command from python and retrieve the result.
- `./files/english.mp3` English audio sample.
- `./files/spanish.m4a` Spanish audio sample.

## Setup the environment
First, create an environment with `python -m venv <directory>` or `conda create -n test_env python=3.12 <name>` and activate with `source <directory>/bin/activate` or `conda activate <name>` respectively.
Next install the requirements with:
`pip install -r requirements.yml`

If that goes well, you have all the necessary packages to run the scripts.

## A Python Script that Takes Arguments like a Unix Tool
You can write a python script to take data with command-line arguments 
The script `stt.py` takes command line arguments for an input file (audio or text) and a corresponding language.
```
./stt.py -f files/english.wav -l en-US
```
In turn, this bash script can receive either an audio file (in roughly any format) or a text file. If it receives an audio file, then it uses the stt.py script to convert it to text first. Then it runs part-of-speech tagging on it.
```
./stt_and_pos.sh files/english.mp3 en-US
```
OR for Latin American spanish
```
./stt_and_pos.sh files/spanish.mpa es-LA
```


## Calling a unix command from python
See `calling_bash_from_python.py`
