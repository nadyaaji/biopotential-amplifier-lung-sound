# 🔬 Biopotential Amplifier for Lung Sound Acquisition

[![Arduino](https://img.shields.io/badge/Arduino-IDE-blue?logo=arduino)](https://www.arduino.cc/)
[![Python](https://img.shields.io/badge/Python-3.x-yellow?logo=python)](https://www.python.org/)
[![LTSpice](https://img.shields.io/badge/LTSpice-Simulation-orange)](https://www.analog.com/en/resources/design-tools-and-calculators/ltspice-simulator.html)

## 📖 Overview
This project is the implementation of a **biopotential amplifier** for **lung sound acquisition**.  
It combines **analog front-end (AFE) design**, **signal acquisition using Arduino**,  **signal analysis in Python**, and **PCB prototyping**.  

---

## 🏗️ System Architecture
![Block Diagram](https://github.com/nadyaaji/biopotential-amplifier-lung-sound/blob/0727da38429028e13e63f532fe13943e6e9a88ea/Block%20Diagram%20System.png)

Main stages:
1. **Chestpiece + Microphone** → capture lung sound  
2. **Instrumentation Amplifier (MAX4194)** → amplify weak signal  
3. **Active Filter (100–2000 Hz)** → remove unwanted noise  
4. **Arduino ADC** → convert to digital  
5. **Signal Processing (FFT, RMS, Inspiration/Expiration Quantification)**  

---

## ⚙️ Specifications
- Gain: **12×**  
- Bandwidth: **80 – 2000 Hz**  
- CMRR: **~70 dB**  
- Sampling: **Arduino UNO (10-bit ADC)**  

---

## 📂 Repository Structure
```
biopotential-amplifier-lung-sound/
│
├── Arduino/ # Arduino IDE codes
│ ├── acquisition.ino
│ ├── record.ino
│ ├── fft_rms.ino
│
├── Python/ # Signal processing scripts
│ ├── plot_response.py
│ ├── stats_analysis.py
│ ├── inspi_expi_quant.py
│
├── LTSpice/ # Circuit simulations
│ ├── amplifier.asc
│ ├── filter.asc
│
├── PCB/ # Eagle PCB design files
│ ├── schematic.sch
│ ├── layout.brd
│
├── Data/ # Example signals
│ ├── subject1_inspi.csv
│ ├── subject1_expi.csv
│
├── Results/ # Plots & experiment results
│ ├── fft_example.png
│ ├── rms_plot.png
│ ├── gain_vs_freq.png
│
├── Docs/ # Documentation
│ ├── block_diagram.png
│ ├── summary.pdf
│
├── LICENSE
└── README.md
```
---

## 🚀 How to Run

### 1️⃣ Acquire Data
1. Upload `acquisition.ino` to Arduino UNO.  
2. Connect chestpiece & amplifier circuit.  
3. Record lung sound → stored as `.csv`.  

### 2️⃣ Process Data
```bash
python Python/plot_response.py Data/subject1_inspi.csv
```

### 3️⃣ Analyze
- fft_rms.ino → run FFT & RMS on Arduino.
- stats_analysis.py → compute mean & std deviation.
- inspi_expi_quant.py → quantify inspiration & expiration phases.

### 📊 Example Results
Lung sound acquisition and analysis:
| Domain          | Plot Example                     |
| --------------- | -------------------------------- |
| Time Domain     | ![time](Results/time_domain.png) |
| Frequency (FFT) | ![fft](Results/fft_example.png)  |
| RMS Analysis    | ![rms](Results/rms_plot.png)     |

### 🌟 Features
- Real-time lung sound acquisition with Arduino
- Bandpass filtering (100–2000 Hz)
- FFT & RMS analysis for signal quality check
- Inspiration/expiration quantification
- LTSpice simulation + PCB design

### 🛠️ Tools Used
1. Arduino UNO (data acquisition & FFT)
2. LTSpice XVII (circuit simulation)
3. Eagle CAD (PCB design)
4. Python (NumPy, Matplotlib) (signal processing)

### 📌 Future Improvements
1. Integration with digital filters (Python or embedded DSP).
2. Wireless lung sound acquisition.
3. Larger dataset for validation.

### 📜 License
This project is released under the MIT License.
Feel free to use, modify, and distribute with attribution.

### 👩‍💻 Author: Nadya Aji Salsabilla
