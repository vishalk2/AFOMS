"""
AFOMS: Ankle-Foot-Orthoses Misalignment Simulator

@Author: Badari Vishal Kandacharam
"""

# Imports
import customtkinter as ctk
import PIL
import os
import sys
import traceback
import logging

from internal.loggingConfig import setup_logging
from ui.getFrameAndLabel import getFrameAndLabel
from internal.analysisSelection import analysisSelectionGo

try:
    # Setting up the logging configuration
    setup_logging()
    logging.info("Logfile configuration setup complete.")
    logging.info("AFOMS application has started.")

    # UI
    root = ctk.CTk()  # Main Window Object
    root_width = root.winfo_screenwidth()  # Screen width
    root_height = root.winfo_screenheight()  # Screen height
    root.title("AFOMS")  # Window title
    root.configure(fg_color="#1B1212")
    root.geometry("{}x{}+0+0".format(root_width, root_height))  # Window geometry

    ## UI: Title labelling & placement
    [titleFrame, titleLabel] = getFrameAndLabel(
        root,
        "#6082B6",
        [780, 35],
        [280, 10],
        "#6082B6",
        "AFOMS: Ankle-Foot-Orthosis Misalignment Simulator",
        {"style": "Times New Roman", "size": 30, "weight": "normal"},
        "#000000",
        [60, 0],
        sticky="nsw",
    )
    ##

    ## UI: Analysis Type Selection
    [analysisSelectionFrame, analysisSelectionLabel] = getFrameAndLabel(
        root,
        "#353935",
        [420, 50],
        [10, 10],
        "#353935",
        "Analysis Type :",
        {"style": "Arial", "size": 15, "weight": "bold"},
        "#F0FFFF",
        [10, 10],
        sticky="nsw",
    )

    analysisSelectionTypes = [
        "Custom Use Case (Typical)",
        "Custom Use Case (Graphical)",
        "Standard Test Cases",
        "Video Simulation",
    ]

    analysisSelectionType = ctk.StringVar(value=analysisSelectionTypes[0])

    analysisSelectionDropdown = ctk.CTkOptionMenu(
        analysisSelectionFrame,
        variable=analysisSelectionType,
        values=analysisSelectionTypes,
        width=230,
        height=37,
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
    analysisSelectionDropdown.place(x=120, y=5)

    analysisSelectionGoButton = ctk.CTkButton(
        analysisSelectionFrame,
        text="Go",
        fg_color="#074D6E",
        hover_color="#14B4FE",
        width=40,
        height=25,
        anchor="center",
        text_color="#FFFFFF",
        font=ctk.CTkFont("Arial", size=13, weight="bold", slant="italic"),
    )
    analysisSelectionGoButton.place(x=370, y=10)
    analysisSelectionGoButton.configure(
        command=lambda: analysisSelectionGo(
            root,
            analysisSelectionTypes,
            analysisSelectionType,
            [
                titleFrame,
                titleLabel,
                analysisSelectionFrame,
                analysisSelectionDropdown,
                analysisSelectionLabel,
                analysisSelectionGoButton,
            ],
        )
    )
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
            os.path.basename(__file__), traceback.extract_tb(sys.exc_info()[-1])[-1][1]
        )
    )
    logging.error(
        "Error occured in the File: {} at Line: {}".format(
            os.path.basename(__file__), traceback.extract_tb(sys.exc_info()[-1])[-1][1]
        )
    )
    print("Error: {}".format(e))
    logging.error("Error: {}".format(e))

finally:
    root.mainloop()
# End
