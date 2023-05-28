import os
import sys
import logging
import traceback
from datetime import datetime
sys.path.append('/home/dev/debug/')
path = '/home/dev/log_files/'

def create_log_file():
    try:
        current_date = datetime.now()
        log_file_path = '{}_{}'.format(path, current_date.strftime('%Y%m%d%H%M%S'))
        #create a logs directory if not exist
        if not os.path.exists(path):
            os.mkdir(path)
        for handler in logging.root.handlers[:]:
            logging.root.removeHandler(handler)
        logging.basicConfig(
            filename=log_file_path,
            filemode='w',
            level=logging.INFO,
            format='%(asctime)s : %(levelname)s - %(message)s'
                            )
    except Exception:
        print(traceback.format_exc())
    return log_file_path
def log_debug(msg):
    try:
        log = logging.getLogger(__name__)
        log.debug(msg.encode('utf-8'))
    except Exception:
        print(traceback.format_exc())

def log_info(msg):
    try:
        log = logging.getLogger(__name__)
        log.info(msg.encode('utf-8'))
    except Exception:
        print(traceback.format_exc())

def log_warning(msg):
    try:
        log = logging.getLogger()
        log.warning(msg.encode('utf-8'))
    except Exception:
        print(traceback.format_exc())
def log_error(msg):
    try:
        log = logging.getLogger(__name__)
        log.error(msg.encode('utf-8'))
    except Exception:
        print(traceback.format_exc())

def log_critical(msg):
    try:
        log = logging.getLogger(__name__)
        log.critical(msg.encode('utf-8'))
    except Exception:
        print(traceback.format_exc())