
import fluidsynth

def midi_to_wav(midi_path, output_wav_path, soundfont_path):
    fs = fluidsynth.Synth()
    fs.start(driver='file')
    sfid = fs.sfload(soundfont_path)
    fs.program_select(0, sfid, 0, 0)
    fs.midi_file_play(midi_path)
    fs.delete()
