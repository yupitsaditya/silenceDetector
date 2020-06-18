from pydub import AudioSegment
from pydub.silence import split_on_silence
import speech_recognition as sr
from collections import Counter
import sys
import os

def divideAudioIntoChunksBySilence(src):
    # Load your audio.
    audioData = AudioSegment.from_file(src)

    # Split track where the silence is 20 miliseconds or more and get chunks using 
    # the imported function.
    chunks = split_on_silence (
        # Use the loaded audio.
        audioData, 
        # Specify that a silent chunk must be at least 2 seconds or 2000 ms long.
        min_silence_len = 20,
        # Consider a chunk silent if it's quieter than -16 dBFS.
        # (You may want to adjust this parameter.)
        silence_thresh = -16#-16
    )

    # Process each chunk with your parameters
    print("Check output folder for individual word audio")
    for i, chunk in enumerate(chunks):
        # Create a silence chunk that's 0.5 seconds (or 500 ms) long for padding.
        silence_chunk = AudioSegment.silent(duration=500)

        # Add the padding chunk to beginning and end of the entire chunk.
        audio_chunk = silence_chunk + chunk + silence_chunk

        # Export the audio chunk with new bitrate.
        if not os.path.exists('output'):
            os.makedirs('output')
        # print("Exporting chunk{0}.mp3.".format(i))
        
        audio_chunk.export(
            "./output/chunk{0}.wav".format(i),
            bitrate = "192k",
            format = "wav"
        )
    print("Number of silences is ",len(chunks)-1)
    lenOfAudioInMin=len(audioData)/60000
    print("Number of words per minutes is ",len(chunks)/lenOfAudioInMin)
    # print("Duration of audio is ",)


def convertToWav(src):
    # convert wav to mp3                                                            
    sound = AudioSegment.from_file(src)
    sound.export('test.wav', format="wav")
    return "test.wav"

def transcribe(src):

    r = sr.Recognizer()
    audioFile = sr.AudioFile(src)
    with audioFile as source:
        audio = r.record(source)
    text=r.recognize_google(audio)
    return text






src = sys.argv[1]

# Using 20ms of silence, dividing the audio into chunks of words
divideAudioIntoChunksBySilence(src)



#using speech recognition library to convert audio into text to get word frequency
#speech library doesn't support mp3 or mp4, so converting to wav first

src=convertToWav(src)
try:
    text=transcribe(src)
    textList=text.split(' ')
    counts = Counter(textList)
    print(counts)
except Exception as e:
    print("Trascription failed so cannot print word frequency")
    raise e


