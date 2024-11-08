# Template Generator for DaVinci Resolve 1.0
# By Quincy Muzik
# Allows a user to select premade template that contains starting files, settings, and layout

import sys
import os

ui = fusion.UIManager()
dispatcher = bmd.UIDispatcher(ui)

# Universal header font for the whole project 
headerFont = ui.Font({'Family': 'Helvetica', 'PointSize': 16, 'Bold': True})

#class NameProject:



#class ProjectType:



#class ImportFiles:


# TODO 
# 1. Create the main the UI
# 2. Create a class for each function in the UI
# 3. Check for existing instance 