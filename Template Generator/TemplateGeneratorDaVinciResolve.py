# Template Generator for DaVinci Resolve 1.0
# By Quincy Muzik
# Allows a user to select premade template that contains starting files, settings, and layout

import sys
import os

ui = fusion.UIManager
dispatcher = bmd.UIDispatcher(ui)

# Universal header font for the whole project 
headerFont = ui.Font({'Family': 'Helvetica', 'PointSize': 16, 'Bold': True})

class NameProject:
    # Constructor
    def __init__(self):
        self.name_id = f'name'

    # Creates the UI Layout
    #def get_ui(self):
        #return ui.VGroup({'Weight':0.1, 'Spacing': 5, }, [
            #ui.Label({'Text': 'Please name your project: ', 'Font': headerFont, 'Weight': 0}),
            #ui.HGroup({ 'Weight': 0 }, [
                #ui.TextEdit({'ID': self.name, 'Text': "Project Name"})
                #ui.HGap(0,0.9),
           # ]),
            #ui.VGap(0,0.05)
      #  ])
    
    def get_ui(self):
        return ui.VGroup({ 'Weight': 0.1, 'Spacing': 5, }, [
            ui.Label({ 'Text': 'Please name your project: ', 'Font': headerFont, 'Weight': 0 }),
            ui.HGroup({ 'Weight': 0 }, [
                ui.TextEdit({'ID': self.name_id, 'Text': 'Project Name'}),
                ui.HGap(0, 0.9),
            ]),
            ui.VGap(0, 0.05)
        ])
    
    # Event Handlers for UI
    

#class ProjectType:



#class ImportFiles:


# TODO 
# 1. Create the main the UI
# 2. Create a class for each function in the UI
# 3. Check for existing instance