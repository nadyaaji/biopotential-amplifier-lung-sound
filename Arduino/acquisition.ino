#include <TimerOne.h>

const int analogPin = A0;  // Pin analog yang akan dibaca
const unsigned long totalDuration = 21000;  // Durasi total pengukuran dalam milidetik (ms)
const int baudRate = 9600;  // Baudrate komunikasi serial
volatile unsigned long sampleCount = 0;
volatile bool measurementComplete = false;

const int samplingFrequency = 10000; // Frekuensi sampling yang lebih rendah
const int downsamplingFactor = 4;    // Faktor downsampling (44100 / 10000  4)

void setup() {
  Serial.begin(baudRate);
  delay(2000);  // Memberikan waktu untuk membuka Serial Monitor
  Serial.println("Starting measurement...");
  Timer1.initialize(1000000 / samplingFrequency);  // Set timer untuk 10000 Hz
  Timer1.attachInterrupt(takeSample);  // Pasang fungsi interrupt
}

void loop() {
  unsigned long startTime = millis();
  unsigned long endTime = startTime + totalDuration;

  while (millis() < endTime && !measurementComplete) {
    // Tidak melakukan apa-apa di loop utama, pengambilan sampel dilakukan di interrupt
  }

  Timer1.detachInterrupt();  // Hentikan timer
  Serial.println("Measurement Complete");
  while (true) {}  // Hentikan loop setelah durasi total tercapai
}

void takeSample() {
  static int downsampleCounter = 0;
  
  if (measurementComplete) {
    return;
  }

  if (downsampleCounter == 0) { // Ambil sampel setiap 4 kali interrupt
    int sensorValue = analogRead(analogPin);
    float voltage = sensorValue * (3.0 / 1023.0);  // Mengonversi nilai ADC ke tegangan
    Serial.println(voltage, 3);  // Menampilkan tegangan dengan 3 digit di belakang koma
    sampleCount++;
  }
  
  downsampleCounter = (downsampleCounter + 1) % downsamplingFactor;

  if (sampleCount >= (totalDuration * (samplingFrequency / 1000))) {  // totalDuration dalam ms
    measurementComplete = true;
  }
}
