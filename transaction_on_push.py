import logging
import os
import subprocess
import time
import yaml

from pyfirmata import Arduino, util


global pressed

def button_callback(channel):
    global pressed
    if pressed == True:
        program = "echo \"OFF\" | " + config['transaction']['path_to_robonomics_file'] + \
            " io write launch -s " + config['transaction']['key'] + " -r " + config['transaction']['address']
        process = subprocess.Popen(program, shell=True, stdout=subprocess.PIPE)
        output = process.stdout.readline()
        logging.warning("OFF transaction hash is " + output.strip().decode('utf8'))
        pressed = False
    else:
        program = "echo \"ON\" | " + config['transaction']['path_to_robonomics_file'] + \
            " io write launch -s " + config['transaction']['key'] + " -r " + config['transaction']['address']
        process = subprocess.Popen(program, shell=True, stdout=subprocess.PIPE)
        output = process.stdout.readline()
        logging.warning("ON transaction hash is " + output.strip().decode('utf8'))
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

board = Arduino('/dev/ttyACM0') #Select the correct port
board.get_pin('d:9:i')
thread = util.Iterator(board)
thread.start()

time.sleep(1)

while True:
    if board.analog[2].read()== True:
        print('!!!')
   else:
        print('No one')
   time.sleep(0.5)
