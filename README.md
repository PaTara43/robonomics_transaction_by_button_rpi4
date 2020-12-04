# Robonomics_transaction_by_button_rpi4
## Send Transactions By pressing button with Raspberry Pi4

Connect button to 5V (PIN4), GND(PIN6) and GPIO18 (PIN12) (in this example) pins on Raspberry Pi
![Raspberry](https://www.raspberrypi.org/documentation/usage/gpio/images/GPIO-Pinout-Diagram-2.png "Raspberry")

To avoid voltage bounce and fake button presses use this scheme where "PIN8" is your LattePanda's A2 pins
![scheme](https://github.com/PaTara43/media/blob/master/button_panda?raw=true "scheme")

Then on Raspberry Pi:
```bash
git clone https://github.com/PaTara43/robonomics_transaction_by_button_rpi4
cd robonomics_transaction_by_button_rpi4
pip install -r requirements.txt
nano config.yaml
```

Fill in all the required info. More info about accounts [here](https://wiki.robonomics.network/docs/create-account-in-dapp/)
Watch out for lines 56, 58 of `transaction_on_push.py` if your pin differs.

Launch the script by `python3 transaction_on_push.py`

Press button to send transactions in network.
