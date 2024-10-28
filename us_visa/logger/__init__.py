# Below is our custom logging code
# We have created a python inbuilt logging package.
# whenever we will execute this log file, instaed of replacing the same file again and again, it will create different log files with different time stamp.
# lets do a demo and check the logger code.

import logging
import os

from from_root import from_root
from datetime import datetime

LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

log_dir = 'logs'

logs_path = os.path.join(from_root(), log_dir, LOG_FILE)

os.makedirs(log_dir, exist_ok=True)


logging.basicConfig(
    filename=logs_path,
    format="[ %(asctime)s ] %(name)s - %(levelname)s - %(message)s",
    level=logging.DEBUG,
)


# This logger code is used by the rest of the project to log messages.
# First time when we ran it, it created a new logs folder. and evertime we run it , it will create a new log file with different timestamp.
# We used demo.py file to test our logger code.
# We can use this logger code in other python projects.

# used below code in demo.py file:

'''
from us_visa.logger import logging

logging.info("Welcome to our custom log")
'''
