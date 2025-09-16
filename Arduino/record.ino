import csv
import serial
import datetime

# Serial port settings
port = 'COM10'
baudrate = 9600
timeout = 1  # Set a timeout for the serial port

# CSV file path
csv_file = 'biooo.csv'

ser = None  # Initialize the serial variable

try:
    # Open the serial port
    ser = serial.Serial(port, baudrate, timeout=timeout)
    
    # Check if the CSV file exists
    file_exists = False
    try:
        with open(csv_file, 'r'):
            file_exists = True
    except FileNotFoundError:
        pass

    # Create the CSV file if it doesn't exist
    if not file_exists:
        with open(csv_file, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['nilai'])  # Add header row

    # Append serial monitor data to the CSV file
    with open(csv_file, 'a', newline='') as file:
        writer = csv.writer(file)
        print("Start reading data. Press Ctrl+C to stop.")
        while True:
            try:
                raw_data = ser.readline()
                try:
                    data = raw_data.decode().strip()
                    if data:
                        writer.writerow([data])
                except UnicodeDecodeError as e:
                    print(f"Decode error: {e}")
                    continue
            except serial.SerialException as e:
                print(f"Serial exception: {e}")
                break
            except Exception as e:
                print(f"Unexpected exception: {e}")
                break

except serial.SerialException as e:
    print(f"Could not open serial port {port}: {e}")
finally:
    if ser and ser.is_open:
        ser.close()
    print("Serial port closed.")
