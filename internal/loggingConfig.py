"""
AFOMS: Ankle-Foot-Orthoses Misalignment Simulator

@Author: Badari Vishal Kandacharam
"""

import os
import logging
import sys
import traceback


# Function to setup the logging configuration for AFOMS
def setup_logging():
    try:
        # Create the directory if it doesn't exist
        log_directory = "../AFOMS"
        os.makedirs(log_directory, exist_ok=True)
        log_filepath = os.path.join(log_directory, "logfile.txt")

        logging.basicConfig(
            filename=log_filepath,
            filemode="w",
            level=logging.INFO,
            format="%(asctime)s - %(levelname)s - %(message)s",
            datefmt="%H:%M:%S",
        )

    except Exception as e:
        print("Error occured while setting up logfile configuration for AFOMS.")
        print(
            "Error occured in the File: {}; Directory: {}".format(
                os.path.basename(__file__), os.path.dirname(os.path.abspath(__file__))
            )
        )
        print(
            "Error occured in the File: {} at Line: {}".format(
                os.path.basename(__file__),
                traceback.extract_tb(sys.exc_info()[-1])[-1][1],
            )
        )
        print("Error: {}".format(e))
