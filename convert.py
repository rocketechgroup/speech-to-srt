import subprocess

subprocess.call(['avconv', '-i', 'example.wav', '-y', '-ar', '48000', '-ac', '1', 'example.flac'])
