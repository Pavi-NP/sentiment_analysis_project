import logging
import sys

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",

    handlers=[
        logging.FileHandler(filename='logs.log', mode='w'), 
        logging.StreamHandler(sys.stdout)
    ]
)
# filehandler: save log messages as a file 
# StreamHandler: display the logs on command prompt or terminal 
#stdout : standard out 
