"""
AFOMS: Ankle-Foot-Orthoses Misalignment Simulator

@Author: Badari Vishal Kandacharam
"""

import os
import sys
import traceback

from internal.typicalCustomUseCase import typicalCustomUseCase


# Backend Function for the "Go" button in AFOMS.py
def analysisSelectionGo(root, analysisSelectionTypes, analysisSelectionType, uiList):
    try:
        # Destroy all the other unnecessary child windows
        for child in root.winfo_children():
            if child not in uiList:
                child.destroy()

        # Get the user-selected analysis selection
        selection = analysisSelectionType.get()

        # Sending for further analysis retrospective
        analysisSelection(root, selection, analysisSelectionTypes)

    except Exception as e:
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


# Function to initiate the selection-based analysis
def analysisSelection(root, selection, analysisSelectionTypes):
    try:
        if selection == analysisSelectionTypes[0]:
            typicalCustomUseCase(root)
        elif selection == analysisSelectionTypes[1]:
            print("Graphical")
        elif selection == analysisSelectionTypes[2]:
            print("Standard Test Cases")
        elif selection == analysisSelectionTypes[3]:
            print("Video Simulation")

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
