import torchaudio
import torch

audio_input, _ = torchaudio.load(TEST_AUDIO_PATH) # Load waveform using torchaudio

s2st_model = torch.jit.load("unity_on_device.ptl")

with torch.no_grad():
    text, units, waveform = s2st_model(audio_input, tgt_lang=TGT_LANG) # S2ST model also returns waveform

print(text)
torchaudio.save(f"{OUTPUT_FOLDER}/result.wav", waveform.unsqueeze(0), sample_rate=16000) # Save output waveform to local file
