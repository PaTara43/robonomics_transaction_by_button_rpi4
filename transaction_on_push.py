import RPi.GPIO as GPIO
import logging
import os
import subprocess
import time
import yaml


global pressed

def button_callback(channel):
    global pressed
    if pressed == True:
        program = "echo \"OFF\" | " + config['transaction']['path_to_robonomics_file'] + \
            " io write launch -s " + config['transaction']['key'] + " -r " + config['transaction']['address']
        process = subprocess.Popen(program, shell=True, stdout=subprocess.PIPE)
        output = process.stdout.readline()
        logging.warning("Transaction hash is " + output.strip().decode('utf8'))
        pressed = False
    else:
        program = "echo \"ON\" | " + config['transaction']['path_to_robonomics_file'] + \
            " io write launch -s " + config['transaction']['key'] + " -r " + config['transaction']['address']
        process = subprocess.Popen(program, shell=True, stdout=subprocess.PIPE)
        output = process.stdout.readline()
        logging.warning("Transaction hash is " + output.strip().decode('utf8'))
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
GPIO.add_event_detect(18,GPIO.RISING,callback=button_callback, bouncetime=2000) # Setup event on pin 12 rising edge

message = input("Waiting fo button to be pressed\n\n") # Run until someone presses enter
GPIO.cleanup() # Clean up
