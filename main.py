import queue, os, threading
import sounddevice as sd
import soundfile as sf
# from scipy.io.wavfile import write
import speech_recognition as sr

r = sr.Recognizer()
print(r)
# harvard = sr.AudioFile('test.wav')
# with harvard as source:
#   audio = r.record(source)
#   print(r.recognize_google(audio))
