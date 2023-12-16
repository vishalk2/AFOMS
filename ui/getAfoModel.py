"""
AFOMS: Ankle-Foot-Orthoses Misalignment Simulator

@Author: Badari Vishal Kandacharam
"""

# Imports
import customtkinter as ctk
from PIL import Image
import os
import sys
import traceback
import logging


# Function to display the AFO figure on the application UI
def getAfoModel(root):
    try:
        imagePath = os.path.join("..", "AFOMS", "figures", "AFO.png")

        afoFigure = ctk.CTkImage(Image.open(imagePath), size=(770, 450))

        afoFigureLabel = ctk.CTkLabel(
            root,
            image=afoFigure,
            text="",
            compound="left",
            width=790,
            height=470,
            fg_color="#353935",
            corner_radius=10,
        )
        afoFigureLabel.place(x=550, y=65)

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

    # return the Label consisting of the AFO figure
    return afoFigureLabel
