# Robonomics_transaction_by_button_rpi4
## Send Transactions By pressing button with Raspberry Pi4

Connect button to 5V (PIN4), GND(PIN6) and GPIO18 (PIN12) (in this example) pins on Raspberry Pi
![Raspberry](https://www.bigmessowires.com/wp-content/uploads/2018/05/Raspberry-GPIO.jpg "Raspberry")

To avoid voltage bounce and fake button presses use this scheme where "PIN8" is your GPIO18 pin
![scheme](https://github.com/PaTara43/media/blob/master/button_panda?raw=true "scheme")

Then on Raspberry Pi:
```bash
git clone https://github.com/PaTara43/robonomics_transaction_by_button_rpi4
cd robonomics_transaction_by_button_rpi4
pip3 install -r requirements.txt
nano config.yaml
```
RPi.GPIO may not install properly, use `apt-get instead`

Fill in all the required info. More info about accounts [here](https://wiki.robonomics.network/docs/create-account-in-dapp/)
Watch out for lines 56, 58 of `transaction_on_push.py` if your pin differs.

Launch the script by `python3 transaction_on_push.py`

Press button to send transactions in network.

## Auto-start
You may want to auto-restart this script. To be able so, edit service file
```bash
nano services/transaction_by_button.service
```
and fill it with path to python3 and the script. Don't forget to fill in username. E.g.:
```
ExecStart=/usr/bin/python3 /home/ubuntu/robonomics_transaction_by_button_rpi4/transaction_on_push.py
User=ubuntu
```
Then move it to `/etc/systemd/system/` and run:
```bash
sudo mv services/transaction_by_button.service /etc/systemd/system/
systemctl enable transaction_by_button
systemctl start transaction_by_button
```
To check service status do:
```bash
systemctl -l status transaction_by_button
```
