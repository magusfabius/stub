# https://realpython.com/python-speech-recognition/


# Hidden Markov Model 
# 10 millisecond fragment
# NN are used to simplify the speech, feature transformation and dimensionality reduction
# Voice activity detectors (VADs) 
#   reduce an audio signal to only the portions that are likely to contain speech. This prevents the recognizer from wasting time analyzing unnecessary parts of the signal.


# speech recognition packages
"""
apiai
assemblyai
google-cloud-speech
pocketsphinx
SpeechRecognition
watson-developer-cloud
wit
"""

# PyAudio package is needed for capturing microphone input.


"""
recognize_bing(): Microsoft Bing Speech
recognize_google(): Google Web Speech API
recognize_google_cloud(): Google Cloud Speech - requires installation of the google-cloud-speech package
recognize_houndify(): Houndify by SoundHound
recognize_ibm(): IBM Speech to Text
recognize_sphinx(): CMU Sphinx - requires installing PocketSphinx
recognize_wit(): Wit.ai

Of the seven, only recognize_sphinx() works offline with the CMU Sphinx engine. The other six all require an internet connection.
"""

# pip install SpeechRecognition
import speech_recognition as sr