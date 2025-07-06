
import librosa

def extract_melody(audio_path):
    y, sr = librosa.load(audio_path)
    pitches, mags = librosa.piptrack(y=y, sr=sr)
    melody = []
    for t in range(pitches.shape[1]):
        idx = mags[:, t].argmax()
        pitch = pitches[idx, t]
        melody.append(pitch if pitch > 0 else 0)
    return melody, sr
