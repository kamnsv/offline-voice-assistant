import torch
import sounddevice as sd
import time

file_model = 'ru_v3.pt'
sample_rate = 48000 # 48000
speaker = 'random' # aidar, baya, kseniya, xenia, random
put_accent = True
put_yo = False
device = torch.device('cpu') # cpu или gpu

model = torch.package.PackageImporter(file_model).load_pickle("tts_models", "model")
model.to(device)


# воспроизводим
def va_speak(what: str):
    audio = model.apply_tts(text=what+"..",
                            speaker=speaker,
                            sample_rate=sample_rate,
                            put_accent=put_accent,
                            put_yo=put_yo)

    sd.play(audio, sample_rate * 1.05)
    time.sleep((len(audio) / sample_rate) + 0.5)
    sd.stop()

# sd.play(audio, sample_rate)
# time.sleep(len(audio) / sample_rate)
# sd.stop()