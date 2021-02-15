import RPi.GPIO as GPIO
import logging
import os
import subprocess
import time
import yaml

from threading import Thread

global pressed

def idling():
    while True:
        time.sleep(60)

def button_callback(channel):
    #logging.warning("Button pressed")
    time.sleep(0.1)
    if GPIO.input(channel):
        return False
    #logging.warning("long press")
    global pressed
    if pressed == True:
        program = "echo \"OFF\" | " + config['transaction']['path_to_robonomics_file'] + \
            " io write launch " + config['transaction']['remote'] + " -s " + config['transaction']['key']
 + " -r " + config['transaction']['address']
        process = subprocess.Popen(program, shell=True, stdout=subprocess.PIPE)
        output = process.stdout.readline()
        logging.warning("OFF transaction hash is " + output.strip().decode('utf8'))
        #logging.warning('OFF')
        pressed = False

    else:
        program = "echo \"ON\" | " + config['transaction']['path_to_robonomics_file'] + \
            " io write launch " + config['transaction']['remote'] + " -s " + config['transaction']['key'] + " -r " + config['transaction']['address']
        process = subprocess.Popen(program, shell=True, stdout=subprocess.PIPE)
        output = process.stdout.readline()
        logging.warning("ON transaction hash is " + output.strip().decode('utf8'))
        #logging.warning('ON')
        pressed = True

def read_configuration(dirname) -> dict:

    config_path = dirname + '/config.yaml'
    logging.debug(config_path)

    try:
        with open(config_path) as f:
            content = f.read()
            config = yaml.load(content, Loader=yaml.FullLoader)
            logging.debug(f"Configuration dict: {content}")
            return config
    except Exception as e:
        while True:
            logging.error("Error in configuration file!")
            logging.error(e)
            exit()

class Error(Exception):
    pass


dirname = os.path.dirname(os.path.abspath(__file__))
config = read_configuration(dirname)

pressed = False

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.add_event_detect(18,GPIO.RISING,callback=button_callback, bouncetime=1000) # Setup event on pin 12 rising edge

input("Waiting for button to be pressed") # Run until someone presses enter
GPIO.cleanup() # Clean up

#start_idling_thread = Thread(target=idling, args=())
#start_idling_thread.start()
