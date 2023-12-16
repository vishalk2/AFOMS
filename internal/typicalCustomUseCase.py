"""
AFOMS: Ankle-Foot-Orthoses Misalignment Simulator

@Author: Badari Vishal Kandacharam
"""
# Imports
import customtkinter as ctk
import os
import sys
import traceback
import logging

from ui.getAfoModel import getAfoModel
from ui.getFrameAndLabel import getFrameAndLabel
from ui.dataSelectionUI import dataSelection


# Function dealing with the custom use case
# where user inputs misalignments by manual typing
def typicalCustomUseCase(root):
    try:
        ## UI : AFO Figure, Title & Label
        afoFigureLabel = getAfoModel(root)
        afoModelLabel = ctk.CTkLabel(root, fg_color="#353935",
                                     text="AFO Simulation Model & Conventions",
                                     text_color="#FFFFFF",
                                     font=ctk.CTkFont("Times New Roman",
                                                      size=30, weight="normal"),
                                     corner_radius=10,
                                     width=450, height=40)
        afoModelLabel.place(x=700, y=540)
        
        dataSelection(root)
        ##

    except Exception as e:
        print("Error occured while running AFOMS application.")
        logging.error("Error occured while running AFOMS application.")
        print(
            "Error occured in the File: {}; Directory: {}".format(
                os.path.basename(__file__), os.path.dirname(os.path.abspath(__file__))
            )
        )
        logging.error(
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
        logging.error(
            "Error occured in the File: {} at Line: {}".format(
                os.path.basename(__file__),
                traceback.extract_tb(sys.exc_info()[-1])[-1][1],
            )
        )
        print("Error: {}".format(e))
        logging.error("Error: {}".format(e))
