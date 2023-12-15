"""
AFOMS: Ankle-Foot-Orthoses Misalignment Simulator

@Author: Badari Vishal Kandacharam
"""
# Imports
import customtkinter as ctk
from PIL import Image
import os

def getAfoModel(root):

    imagePath = os.path.join('..','AFOMS', 'figures', 'AFO.png')

    afoFigure = ctk.CTkImage(Image.open(imagePath), size=(770, 450))

    afoFigureLabel = ctk.CTkLabel(root, image=afoFigure,
                                  text="", compound="left",
                                  width=790, height=470,
                                  fg_color="#353935",
                                  corner_radius=10)
    afoFigureLabel.place(x=550, y=65)

    return afoFigureLabel