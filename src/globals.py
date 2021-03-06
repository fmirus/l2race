""" global parameters"""
import logging


LOGGING_LEVEL=logging.INFO # set the overall default leval, change with --log option

import scipy.constants
G=scipy.constants.value('standard acceleration of gravity')

#######################################################
# client

# SERVER_HOST='telluridevm.iniforum.ch' # metanet 16-core model server
SERVER_HOST='localhost'
SERVER_PING_INTERVAL_S=1 # interval between trying for server
SERVER_TIMEOUT_SEC = 1 # timeout in seconds for UDP socket reads during game running

# your autodrive controller module (i.e. folder) and class name, must be a class that has read method that returns the car_command() object
AUTODRIVE_MODULE='src.pid_next_waypoint_car_controller'
AUTODRIVE_CLASS='pid_next_waypoint_car_controller'

#display
FPS=20 # frames per second for simulation and animation
GAME_FONT_NAME='Consolas' # local display font, default is Consolas
GAME_FONT_SIZE=16 # default is 16

# Joystick connectivity
CHECK_FOR_JOYSTICK_INTERVAL = 100 # check for missing joystick every this many cycles
JOYSTICK_NUMBER = 0 # in case multiple joysticks, use this to set the desired one, starts from zero

# recording data
DATA_FILENAME_BASE= 'l2race'
DATA_FOLDER_NAME= 'data'

# car and track options
CAR_NAME='l2racer' # label stuck on car
TRACK_NAME='oval_easy' # tracks are stored in the 'media' folder. Data for a track must be extracted using scripts in Track_Preparation before using in l2race
# Other possible track names:
# track_names = [
#          'Sebring',
#          'oval',
#          'oval_easy',
#          'track_1',
#          'track_2',
#          'track_3',
#          'track_4',
#          'track_5',
#          'track_6']
# track_name + '.png'
# track_name + '_map.npy'
# track_name + 'Info.npy'

#######################################################
#server and model settings. Client cannot affect these model server settings
#
# DO NOT CHANGE THESE VALUES
#########################
# DO NOT CHANGE UNLESS they are also changed on model server
# define screen area, track is scaled to fill this area, note 4:3 aspect ratio
SCREEN_WIDTH_PIXELS=1024 #  pixels
SCREEN_HEIGHT_PIXELS= 768 # pixels
# meters per screen pixel, e.g. 4m car would be 40 pixels, so about 4% of width
# increase M_PER_PIXEL to make cars smaller relative to track
M_PER_PIXEL=0.2

SERVER_PORT = 50000 # client starts game on this port on the SERVER_HOST
CLIENT_PORT_RANGE='50010-50020' # range of ports used for client that server uses for game
    # client needs to open this port range for receiving state from server and sending commands to server
KILL_ZOMBIE_TRACK_TIMEOUT_S=10 # if track process gets no input for this long, it terminates itself
FRICTION_FACTOR = .5 # overall friction parameter multiplier for some models
SAND_SLOWDOWN = 0.975  # If in sand, at every update the resulting velocity is multiplied by the slowdown factor
REVERSE_TO_FORWARD_GEAR = 0.5  # You get less acceleration on reverse gear than while moving forwards.
MODEL_UPDATE_RATE_HZ=100 # rate that server attempts to update all the car models for each track process (models run serially in each track process)
MAX_CARS_PER_TRACK=6 # only this many cars can run on each track
MAX_SPECTATORS_PER_TRACK=10 # only this many spectators can connect to each track
KS_TO_ST_SPEED_M_PER_SEC=2.0 # transistion speed from KS to ST model types

