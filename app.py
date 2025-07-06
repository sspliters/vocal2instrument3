
from flask import Flask, request, render_template, send_from_directory, jsonify
import os
from audio_processing.stem_splitter import split_stems
from audio_processing.melody_extractor import extract_melody
from audio_processing.instrument_synth import melody_to_midi
from audio_processing.midi_to_wav import midi_to_wav

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
OUTPUT_FOLDER = 'outputs'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_audio():
    file = request.files['audio']
    file_path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(file_path)

    stem_dir = split_stems(file_path)
    vocal_path = os.path.join(stem_dir, 'vocals.wav')

    melody, sr = extract_melody(vocal_path)
    midi_path = melody_to_midi(melody, sr, file.filename)
    wav_path = midi_path.replace('.mid', '.wav')

    soundfont = 'assets/soundfonts/FluidR3_GM.sf2'
    midi_to_wav(midi_path, wav_path, soundfont)

    return jsonify({
        'midi_url': '/outputs/' + os.path.basename(midi_path),
        'wav_url': '/outputs/' + os.path.basename(wav_path)
    })

@app.route('/outputs/<filename>')
def serve_output(filename):
    return send_from_directory('outputs', filename)

if __name__ == '__main__':
    app.run(debug=True)
