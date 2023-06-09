import wave
import sys
import json
from vosk import KaldiRecognizer, SetLogLevel
import vosk

def recognition():

    SetLogLevel(-1)

    wf = wave.open('mono.wav', "rb")
    if wf.getnchannels() != 1 or wf.getsampwidth() != 2 or wf.getcomptype() != "NONE":
        print("Audio file must be WAV format mono PCM.")
        sys.exit(1)

    model_path = '/src/models/model_small'
    model = vosk.Model(model_path)


    rec = KaldiRecognizer(model, wf.getframerate())
    rec.SetWords(True)
    rec.SetPartialWords(True)

    while True:
        data = wf.readframes(4000)
        if len(data) == 0:
            break
        if rec.AcceptWaveform(data):
            pass


    x = json.loads(rec.FinalResult())["text"]

    return x