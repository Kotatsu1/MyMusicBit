import torch
from controllers.ai import chat

def sound_ai(q):
    device = torch.device('cpu')
    torch.set_num_threads(4)
    local_file = '/src/models/model.pt'

    model = torch.package.PackageImporter(local_file).load_pickle("tts_models", "model")
    model.to(device)

    ex = chat(q)

    sample_rate = 48000
    speaker='xenia' # aidar, baya, kseniya, xenia, eugene, random

    audio_paths = model.save_wav(text=ex,
                                speaker=speaker,
                                sample_rate=sample_rate)
    
    return audio_paths