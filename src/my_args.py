# arguments for l2race client and server
import os

from src.globals import *
import logging

from src.track import list_tracks

logger = logging.getLogger(__name__)

def client_args(parser):
    # check and add prefix if running script in subfolder

    # general arguments for output folder, overwriting, etc
    clientServerGroup = parser.add_argument_group('Server options:')
    clientServerGroup.add_argument("--host", type=str, default=SERVER_HOST, help="IP address or DNS name of model server.")
    clientServerGroup.add_argument("--port", type=int, default=SERVER_PORT, help="Server port address for initiating connections.")
    clientServerGroup.add_argument("--timeout_s", type=float, default=SERVER_TIMEOUT_SEC, help="Socket timeout in seconds for communication with model server.")

    clientInterfaceGroup = parser.add_argument_group('Interface arguments:')
    clientInterfaceGroup.add_argument("--fps", type=int, default=FPS, help="Frame rate on client side (server always sets time to real time).")
    clientInterfaceGroup.add_argument("--joystick", type=int, default=JOYSTICK_NUMBER, help="Desired joystick number, starting with 0.")

    clientOutputGroup = parser.add_argument_group('Output options:')
    clientOutputGroup.add_argument("--record", action='store_true', help="record data to date-stamped filename, e.g. --record will write datestamped files named '{}-XXX.csv' in folder '{}, where XXX is a date/timestamp\'.".format(DATA_FILENAME_BASE, DATA_FOLDER_NAME))
    try:
        # make hopefully unique car name
        import socket,getpass,random,string
        hostname=socket.gethostname()
        username=getpass.getuser()
        car_name=str(hostname)+':'+str(username)+'-'
        car_name+=''.join(random.choices(string.ascii_uppercase, k=2)) #https://stackoverflow.com/questions/2257441/random-string-generation-with-upper-case-letters-and-digits
    except:
        car_name=CAR_NAME

    clientTrackCarMode = parser.add_argument_group('Track car/spectate options:')
    clientTrackCarMode.add_argument("--track_name", type=str, default=TRACK_NAME, help="Name of track. Available tracks are in the 'media/tracks' folder. Available tracks are "+str(list_tracks()))
    clientTrackCarMode.add_argument("--car_name", type=str, default=car_name, help="Name of this car (last 2 letters are randomly chosen each time).")
    clientTrackCarMode.add_argument("--spectate", action='store_true', help="Just be a spectator on the cars on the track.")

    # other options
    parser.add_argument('--log',type=str,default=str(logging.getLevelName(LOGGING_LEVEL)),help='Set logging level. From most to least verbose, choices are "DEBUG", "INFO", "WARNING".')
    return parser

def server_args(parser):
    # check and add prefix if running script in subfolder

    serverGroup = parser.add_argument_group('Server arguments:')
    serverGroup.add_argument("--allow_off_track", action='store_true', help="ignore when car goes off track (for testing car dynamics more easily)")
    serverGroup.add_argument('--log',type=str,default=str(logging.getLevelName(LOGGING_LEVEL)),help='Set logging level. From most to least verbose, choices are "DEBUG", "INFO", "WARNING".')
    # serverGroup.add_argument("--timeout_s", type=int, default=CLIENT_TIMEOUT_SEC, help="server timeout in seconds before it ends thread for handling a car model")
    # serverGroup.add_argument("--model", type=str, default=src.car_model.MODEL, help="server timeout in seconds before it ends thread for handling a car model")

    return parser

def write_args_info(args, path)-> str:
    '''
    Writes arguments to logger and file named from startup __main__
    Parameters
    ----------
    args: parser.parse_args()

    Returns
    -------
    full path to file
    '''
    import __main__
    arguments_list = 'arguments:\n'
    for arg, value in args._get_kwargs():
        arguments_list += "{}:\t{}\n".format(arg, value)
    logger.info(arguments_list)
    basename = os.path.basename(__main__.__file__)
    argsFilename = basename.strip('.py') + '-args.txt'
    filepath = os.path.join(path, argsFilename)
    with open(filepath, "w") as f:
        f.write(arguments_list)
    return filepath


