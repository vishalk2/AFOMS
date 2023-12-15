"""
AFOMS: Ankle-Foot-Orthoses Misalignment Simulator

@Author: Badari Vishal Kandacharam
"""
# Imports
import customtkinter as ctk

from ui.getAfoModel import getAfoModel

def typicalCustomUseCase(root):

    afoFigureLabel = getAfoModel(root)