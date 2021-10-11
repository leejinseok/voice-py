import speech_recognition
from record import record

# r = sr.Recognizer()
# print(r)
# harvard = sr.AudioFile('test.wav')
# with harvard as source:
#   audio = r.record(source)
#   print(r.recognize_google(audio))

def main():
  fileName = record()
  print(fileName)


main()