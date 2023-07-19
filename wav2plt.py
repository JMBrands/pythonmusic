import matplotlib.pyplot as plt
import numpy as np
from scipy.io.wavfile import read

rate, data = read("idol1.wav")
plt.plot(np.arange(len(data))/rate,data)
plt.show()