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

win_id = "TemplateGeneratorPython"

# Check for instance 
win = ui.FindWindow(win_id)
if win:
    win.Show()
    win.Raise()
    exit()

default_config = {
    "window": {
        "ID": win_id,
        "Geometry": [100,100,600,500],
        "WindowTitle": "Template Generator Tool"
    }
}

examples = [NameProject()]
win = dispatcher.AddWindow(default_config['window'],ui.VGroup({'Spacing':5,}, [
    example.get_ui() for example in examples
    ])
)

def close(ev):
    dispatcher.ExitLoop()

win.On[win_id].Close = close

for example in examples:
    example.connect_handlers(win)

win.Show()
dispatcher.RunLoop()

# TODO 
# 1. Create the main the UI
# 2. Create a class for each function in the UI
# 3. Check for existing instance