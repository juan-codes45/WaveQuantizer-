import numpy as np
import matplotlib.pyplot as plt

# Time range
t = np.linspace(0, 4.5e-3, 1000)

# 440 Hz sample wave
sample_wave = np.sin(2 * np.pi * 440 * t)

# Quantization wave
quantization_wave = np.round(sample_wave * 8) / 8

# Create the plot
plt.figure(figsize=(8, 6))
plt.plot(t, sample_wave, label='440 Hz Sample wave')
plt.plot(t, quantization_wave, label='Quantization wave')
plt.xlabel('time in seconds')
plt.ylabel('amplitude')
plt.title('440 Hz Sample Wave and Quantization Wave')
plt.legend()
plt.show()