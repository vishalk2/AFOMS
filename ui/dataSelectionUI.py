"""
AFOMS: Ankle-Foot-Orthoses Misalignment Simulator

@Author: Badari Vishal Kandacharam
"""

import customtkinter as ctk
import os
import sys
import traceback
import logging


# Function for setting up the data selection
def dataSelection(root):
    try:
        # UI : Data Selection Frame
        dataSelectionFrame = ctk.CTkFrame(
            root, fg_color="#353935", width=420, height=200
        )
        dataSelectionFrame.grid(padx=10, pady=10, sticky="nsw")

        ## UI : Subject Selection
        subjectSelectionLabel = ctk.CTkLabel(
            dataSelectionFrame,
            fg_color="#353935",
            text="Subject : ",
            text_color="#FFFFFF",
            font=ctk.CTkFont("Arial", size=15, weight="bold"),
        )
        subjectSelectionLabel.place(x=10, y=10)

        subjectsList = ["AB01", "AB02", "AB03", "AB04", "AB05"]
        subjectSelection = ctk.StringVar(value=subjectsList[0])

        subjectSelectionDropdown = ctk.CTkOptionMenu(
            dataSelectionFrame,
            variable=subjectSelection,
            values=subjectsList,
            width=200,
            height=32,
            corner_radius=0,
            bg_color="#6082B6",
            fg_color="#6082B6",
            button_color="#6082B6",
            hover=True,
            button_hover_color="#14B4FE",
            dropdown_fg_color="#6082B6",
            dropdown_hover_color="#14B4FE",
            anchor="center",
            text_color="#FFFFFF",
            font=ctk.CTkFont("Arial", size=13, weight="bold"),
        )
        subjectSelectionDropdown.place(x=120, y=5)
        ##

        #

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
