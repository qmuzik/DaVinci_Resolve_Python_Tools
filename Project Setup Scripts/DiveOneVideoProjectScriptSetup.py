#!/usr/bin/env python

"""
- DiveOne Video Project Setup Script
- Script that automates a DiveOne Video Project Creation/Setup with Imported Media 
- By Quincy Muzik 11/24/2024
"""

class DiveOneVideProjectClass:

    def projectSetup():

        # ACCESSORS -----------------------------------------------------------------------------------------------
        # Get the Project Manager 
        projectManager = resolve.GetProjectManager()
        # Get the current project 
        project = projectManager.GetCurrentProject()
        # Get Media Pool
        mediaPool = project.GetMediaPool()
        # Get Media Storage
        mediaStorage = resolve.GetMediaStorage()

        # MAIN ----------------------------------------------------------------------------------------------------
        # Find and Name Starting Files
        musicFolderName = 'J:\\DaVinci Resolve Project Setup Files\\DiveOne Video\\Music'
        videoFolderName = 'J:\\DaVinci Resolve Project Setup Files\\DiveOne Video\\Videos'
        logoFolderName = 'J:\\DaVinci Resolve Project Setup Files\\DiveOne Video\\Logo'

        # Import Starting Files
        diveOneMedia = mediaPool.ImportMedia(musicFolderName,videoFolderName,logoFolderName)

        # Create a timeline with project name
        timeline = mediaPool.CreateEmptyTimeline('DiveOne Video')

        # Save the new Project
        newProject = projectManager.SaveProject()

        # Open the Edit Page to Start Editing
        startingPage = resolve.OpenPage("edit")

# SCRIPT EXECUTION 
DiveOneVideProjectClass.projectSetup()