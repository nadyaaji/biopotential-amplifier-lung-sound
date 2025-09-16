# Hitung rata-rata dari kedua sinyal
# combined_data = (data1 + data2) / 2
nadya = df_list[0]
# Frekuensi sampling asli
fs = 10000  # Frekuensi sampling asli 10 kHz

# Durasi data asli dalam detik
duration_original = len(nadya) / fs
print(f"Durasi Data Asli: {duration_original} detik")

df_list[3].values.shape

limit = 9000

t = np.arange(0,limit)/fs
t

# Plot FFT
plt.figure(figsize=(10, 6))
plt.plot(t,nadya[:limit], label ='Sinyal Suara Paru - Paru')
plt.xlabel('Time(s)')
plt.ylabel('Amplitude')
plt.title('Recording of Signal (Responden 3)')

# Tambahkan garis horizontal untuk nilai RMS

plt.legend()


plt.show()

nadya_fft = np.fft.fft(nadya)
nadya_freq = np.fft.fftfreq(len(nadya),1/fs)

rms_value = np.sqrt(np.mean(nadya**2))

peak_index = np.argmax(np.abs(nadya_fft[:len(nadya)//2]))
peak_frequency = nadya_freq[peak_index]
peak_amplitude = np.abs(nadya_fft[peak_index])

# Plot FFT
plt.figure(figsize=(10, 6))
plt.plot(nadya_freq[:len(nadya_freq)//2], np.abs(nadya_fft)[:len(nadya_fft)//2])
plt.xlabel('Frequency (Hz)')
plt.ylabel('Amplitude')
plt.title('FFT of Responden 3 Data')

# Tambahkan garis horizontal untuk nilai RMS
plt.axhline(y=rms_value, color='r', linestyle='--', label=f'RMS Value: {rms_value:.2f}')
plt.legend()

# Highlight peak frequency
plt.plot(peak_frequency, peak_amplitude, 'ro', label=f'Peak Frequency: {peak_frequency:.2f} Hz')

# Add text annotation for peak frequency
plt.text(peak_frequency, peak_amplitude, f'{peak_frequency:.2f} Hz', color='red', ha='left')

plt.show()
