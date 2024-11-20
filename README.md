# bash-and-python

## Setup the environment
First, create an environment with `python -m venv <directory>` or `conda create -n test_env python=3.12 <name>` and activate with `source <directory>/bin/activate` or `conda activate <name>` respectively.
Next install the requirements with:
`pip install -r requirements.yml`

## Passing data from terminal to python
You can write a python script to take data with command-line arguments 
1. See `stt_and_pos.sh` (Speech-to-text and part-of-speech tagger)
```
./stt_and_pos.sh files/english.mp3 en-US
```
OR
```
./stt_and_pos.sh files/spanish.mpa es-LA
```
See `stt_and_tokenize.sh` (Speach-to-text and tokenize)


## Calling a unix command from python
See `calling_bash_from_python.py`
