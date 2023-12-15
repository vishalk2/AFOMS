"""
AFOMS: Ankle-Foot-Orthoses Misalignment Simulator

@Author: Badari Vishal Kandacharam
"""

from internal.typicalCustomUseCase import typicalCustomUseCase

# Backend Function for the "Go" button in AFOMS.py
def analysisSelectionGo(root, analysisSelectionTypes, 
                        analysisSelectionType, uiList):

    for child in root.winfo_children():
        if child not in uiList:
            child.destroy()
    selection = analysisSelectionType.get()
    analysisSelection(root, selection, analysisSelectionTypes)

# Function to initiate the selection-based analysis
def analysisSelection(root, selection, 
                      analysisSelectionTypes):
    
    if selection == analysisSelectionTypes[0]:
        typicalCustomUseCase(root)
    elif selection == analysisSelectionTypes[1]:
        print("Graphical")
    elif selection == analysisSelectionTypes[2]:
        print("Standard Test Cases")
    elif selection == analysisSelectionTypes[3]:
        print("Video Simulation")