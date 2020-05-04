https://arduino.github.io/arduino-cli/getting-started/

arduino-cli core update-index

arduino-cli board list

arduino-cli core install arduino:avr

sudo arduino-cli compile --fqbn arduino:avr:uno PowerRelay

sudo arduino-cli upload -p /dev/ttyACM0 --fqbn arduino:avr:uno PowerRelay
