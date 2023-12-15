"""
AFOMS: Ankle-Foot-Orthoses Misalignment Simulator

@Author: Badari Vishal Kandacharam
"""

import customtkinter as ctk

# Function to create a custom Frame and a Label inside it
def getFrameAndLabel(window_frame, frame_fg_color, 
                     frameDimensions, frameGrids,
                     label_fg_color, labeltext, 
                     fontProperties, text_color,
                     labelCoordinates,sticky=None):
    
    # Frame
    frame = ctk.CTkFrame(window_frame, fg_color=frame_fg_color,
                         width=frameDimensions[0],
                         height=frameDimensions[1])
    frame.grid(padx = frameGrids[0], pady = frameGrids[1],sticky=sticky)

    # Label
    label = ctk.CTkLabel(frame, fg_color=label_fg_color,
                         text=labeltext, text_color=text_color,
                         font=ctk.CTkFont(fontProperties["style"],
                                          size=fontProperties["size"],
                                          weight=fontProperties["weight"]))
    label.place(x = labelCoordinates[0], y = labelCoordinates[1])

    # return the custom created frame and label
    return [frame, label]