import speech_recognition as sr
import pyaudio
import wave

def record():
    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 2
    RATE = 44100
    WAVE_OUTPUT_FILENAME = "output.wav"
    audio = pyaudio.PyAudio()
    stream = audio.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)
    frames = []
    print("start record")
    try:
        while True:
            data = stream.read(CHUNK)
            frames.append(data)
    except KeyboardInterrupt:
        print("end record")
        pass

    stream.stop_stream()
    stream.close()
    audio.terminate()

    sound_file = wave.open(WAVE_OUTPUT_FILENAME, "wb")
    sound_file.setnchannels(CHANNELS)
    sound_file.setsampwidth(audio.get_sample_size(FORMAT))
    sound_file.setframerate(RATE)
    sound_file.writeframes(b''.join(frames))
    sound_file.close()

    return WAVE_OUTPUT_FILENAME

def readText(filePath):
  recognizer = sr.Recognizer()
  audioFile = sr.AudioFile(filePath)
  with audioFile as source:
    audio = recognizer.record(source)
  if (audioFile.DURATION == None):
    return

  return recognizer.recognize_google(audio, language='Ko-KR')
