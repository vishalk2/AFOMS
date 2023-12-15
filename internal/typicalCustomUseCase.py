"""
AFOMS: Ankle-Foot-Orthoses Misalignment Simulator

@Author: Badari Vishal Kandacharam
"""
# Imports
import customtkinter as ctk
import os
import sys
import traceback

from ui.getAfoModel import getAfoModel


# Function dealing with the custom use case
# where user inputs misalignments by manual typing
def typicalCustomUseCase(root):
    try:
        afoFigureLabel = getAfoModel(root)

    except Exception as e:
        print("Error occured while running AFOMS application.")
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
