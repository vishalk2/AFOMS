import customtkinter as ctk

# Function to create a custom Frame and a Label inside it
def getFrameAndLabel(window_frame, fg_color, 
                     frameDimensions, frameGrids,
                     labeltext, fontSize,
                     labelCoordinates):
    
    # Frame
    frame = ctk.CTkFrame(window_frame, fg_color=fg_color,
                         width=frameDimensions[0],
                         height=frameDimensions[1])
    frame.grid(padx = frameGrids[0], pady = frameGrids[1])

    # Label
    label = ctk.CTkLabel(frame, fg_color=fg_color,
                         text=labeltext,
                         font=("Times New Roman", fontSize))
    label.place(x = labelCoordinates[0], y = labelCoordinates[1])

    # return the custom created frame and label
    return [frame, label]