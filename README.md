# Robonomics_transaction_by_button_rpi4
## Panda edition
**This is for LattePanda with ubuntu installed**
### To set up LattePanda's Arduino board
```bash
curl -fsSL https://raw.githubusercontent.com/platformio/platformio-core-installer/master/get-platformio.py -o get-platformio.py
python3 get-platformio.py
export PATH=$PATH:~/.platformio/penv/bin
mkdir pio_firmata
cd pio_firmata/
pio project init --board leonardo
nano platformio.ini
```
Insert script from [here](https://platformio.org/lib/show/307/Firmata/installation)
```bash
pio lib install "firmata/Firmata@^2.5.8"
cd src
touch StandardFirmata.ino
nano StandardFirmata.ino
```
Insert script from [here](https://platformio.org/lib/show/307/Firmata/examples)
```bash
cd ..
pio lib install Servo
pio lib install SoftwareSerial
pio run
pio run --target upload
```
Connect button to 5G, GND and A2 pins on LattePanda
![LattePanda](https://core-electronics.com.au/media/wysiwyg/tutorials/sam/Pinout-Development-Support.png "LattePanda")

To avoid voltage bounce and fake button presses use this scheme where "PIN8" is your LattePanda's A2 pins
![scheme](https://github.com/PaTara43/media/blob/master/button_panda?raw=true "scheme")

Then on panda:
```bash
git clone -b panda https://github.com/PaTara43/robonomics_transaction_by_button_rpi4
cd robonomics_transaction_by_button_rpi4
pip install -r requirements.txt
nano config.yaml
```

Fill in all the required info. More info about accounts [here](https://wiki.robonomics.network/docs/create-account-in-dapp/)
Watch out for lines 63, 66, 68, 71 of `transaction_on_push.py` if your board device address or pin or voltage level differs.

Launch the script by `python3 transaction_on_push.py`

Press button to send transactions in network.
