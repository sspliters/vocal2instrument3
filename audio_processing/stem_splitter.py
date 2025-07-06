
import subprocess
import os

def split_stems(input_path, output_dir='outputs/stems'):
    os.makedirs(output_dir, exist_ok=True)
    command = ['demucs', input_path, '-o', output_dir]
    subprocess.run(command, check=True)
    song_name = os.path.splitext(os.path.basename(input_path))[0]
    return os.path.join(output_dir, 'htdemucs', song_name)
