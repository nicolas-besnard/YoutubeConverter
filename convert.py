import subprocess
import re

#process = subprocess.call(['D:/ffmpeg.exe', '-i', 'D:/1.mp4', '-ac', '2', '-ab', '128k', 'D:/toto.mp3'])
process = subprocess.Popen(['D:/ffmpeg.exe', '-i', 'D:/1.mp4'], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
stdout, stderr = process.communicate()
print stdout