
import pretty_midi
import librosa
import os

def melody_to_midi(melody, sr, original_filename):
    midi = pretty_midi.PrettyMIDI()
    inst = pretty_midi.Instrument(program=0)
    t = 0
    step = 0.1
    for pitch in melody:
        if pitch > 0:
            note = pretty_midi.Note(
                velocity=100,
                pitch=int(librosa.hz_to_midi(pitch)),
                start=t,
                end=t + step
            )
            inst.notes.append(note)
        t += step
    midi.instruments.append(inst)
    midi_path = os.path.join('outputs', original_filename.replace('.wav', '.mid').replace('.mp3', '.mid'))
    midi.write(midi_path)
    return midi_path
