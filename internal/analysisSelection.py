
def analysisSelectionGo(root, analysisSelectionTypes, 
                        analysisSelectionType, uiList):

    for child in root.winfo_children():
        if child not in uiList:
            child.destroy()
    selection = analysisSelectionType.get()
    analysisSelection(root, selection, analysisSelectionTypes)


def analysisSelection(root, selection, 
                      analysisSelectionTypes):
    
    if selection == analysisSelectionTypes[0]:
        print("Typical")
    elif selection == analysisSelectionTypes[1]:
        print("Graphical")
    elif selection == analysisSelectionTypes[2]:
        print("Standard Test Cases")
    elif selection == analysisSelectionTypes[3]:
        print("Video Simulation")