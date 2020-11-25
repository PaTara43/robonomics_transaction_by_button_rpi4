# robonomics_transaction_by_button_rpi4
##panda edition

https://docs.platformio.org/en/latest/core/quickstart.html



```bash
curl -fsSL https://raw.githubusercontent.com/platformio/platformio-core-installer/master/get-platformio.py -o get-platformio.py
python3 get-platformio.py
export PATH=$PATH:~/.platformio/penv/bin
mkdir pio_firmata
cd pio_firmata/
pio project init --board leonardo
nano platformio.ini
```
https://platformio.org/lib/show/307/Firmata/installation

```bash
pio lib install "firmata/Firmata@^2.5.8"
cd src
touch StandardFirmata.ino
nano StandardFirmata.ino
```
https://platformio.org/lib/show/307/Firmata/examples

```bash
cd ..
pio lib install Servo
pio lib install SoftwareSerial
pio run
pio run --target upload
```

connect button to 5v and A2 pins
