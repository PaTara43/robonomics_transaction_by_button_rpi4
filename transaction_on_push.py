import logging
import os
import subprocess
import time
import yaml

from pyfirmata import Arduino, util
from pyfirmata.util import Iterator
from threading import Thread


global on_off


def callback():
    global on_off

    if on_off:
        program = "echo \"OFF\" | " + config['transaction']['path_to_robonomics_file'] + \
            " io write launch " + config['transaction']['remote'] + " -s " + config['transaction']['key'] + " -r " + config['transaction']['address']
        process = subprocess.Popen(program, shell=True, stdout=subprocess.PIPE)
        output = process.stdout.readline()
        logging.warning("OFF transaction hash is " + output.strip().decode('utf8'))
        on_off = False
    else:
        program = "echo \"ON\" | " + config['transaction']['path_to_robonomics_file'] + \
            " io write launch " + config['transaction']['remote'] + " -s " + config['transaction']['key'] + " -r " + config['transaction']['address']
        process = subprocess.Popen(program, shell=True, stdout=subprocess.PIPE)
        output = process.stdout.readline()
        logging.warning("ON transaction hash is " + output.strip().decode('utf8'))
        on_off = True


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

state = False
prev_state = False
on_off = False

board = Arduino('/dev/ttyACM0') #Select the correct port
it = util.Iterator(board)
it.start()
board.analog[2].enable_reporting()
while True:
    if board.analog[2].read() == None:
        continue
    prev_state = state
    state = (board.analog[2].read() <= 0.8)
    if state and not prev_state:
        callback_thread = Thread(target=callback, args=())
        callback_thread.start()
        time.sleep(8)
    else:
        time.sleep(0.1)
