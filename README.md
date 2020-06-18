# silenceDetector
Divide an Audio file into chunks of word

[Web App For The Same](https://ict-ai-position.herokuapp.com/)

The program takes an audio file, uses pydub library to split the audio file into chunks.

The program uses speech recognition library to transcribe the audio file into text.


## Set-up

* Clone the repository

* pip install pydub

* pip install SpeechRecognition

* Also, may have to set up [ffmpeg.](https://ffmpeg.org/)

* Also, add ffmpeg to system variable list.


## Run

python main.py [audio filename]

ex: python main.py aditya.mp4


Sample audio file aditya.mp4 present in the repository.


## Output

On command line, you will get:

* The number of silences in the audio file.

* The speed in words/minute

* The word frequency


In output folder, you will get the audio files generated using silence between words.


### Check research.txt for more detail.

