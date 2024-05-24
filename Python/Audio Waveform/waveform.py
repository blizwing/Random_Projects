import librosa
import matplotlib.pyplot as plt
from tkinter import Tk
from tkinter.filedialog import askopenfilename

# Only Audio Files are Supported.
Tk().withdraw()
filename = askopenfilename()
print(filename)

# Load the audio file
y, sr = librosa.load(filename)

# Plotting the waveform
plt.figure(figsize=(14, 5))
librosa.display.waveshow(y, sr=sr)
plt.title('Audio Waveform')
plt.show()
