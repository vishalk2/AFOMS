"""
AFOMS: Ankle-Foot-Orthoses Misalignment Simulator

@Author: Badari Vishal Kandacharam
"""

# Imports
import customtkinter as ctk

from ui.getFrameAndLabel import getFrameAndLabel

# UI
root = ctk.CTk() # Main Window Object
root_width = root.winfo_screenwidth() # Screen width
root_height = root.winfo_screenheight() # Screen height
root.title("AFOMS") # Window title
root.geometry("{}x{}+0+0".format(root_width,root_height)) # Window geometry

## UI: Title labelling & placement
[title_frame, title_label] = getFrameAndLabel(root, "#FF7800",
                                              [780, 35], [280, 10],
                                              "AFOMS: Ankle-Foot-Orthosis Misalignment Simulator",
                                              30, [60, 0])



root.mainloop()
# End