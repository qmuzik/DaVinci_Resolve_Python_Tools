#!/usr/bin/env python

"""
- Slideshow Video Project Setup Script
- Script that automates a Slideshow Video Project Creation/Setup with Imported Media 
- By Quincy Muzik 11/24/2024
"""

class SlideshowVideoProjectClass:

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
        musicFolderName = 'J:\\DaVinci Resolve Project Setup Files\\Slideshow Video\\Music'
        imagesFolderName = 'J:\\DaVinci Resolve Project Setup Files\\Slideshow Video\\Images'

        # Import Starting Files
        slideshowMedia = mediaPool.ImportMedia(musicFolderName,imagesFolderName)

        # Create a timeline with project name
        timeline = mediaPool.CreateEmptyTimeline('Slideshow')

        # Save the new Project
        newProject = projectManager.SaveProject()

        # Open the Edit Page to Start Editing
        startingPage = resolve.OpenPage("edit")

# SCRIPT EXECUTION 
SlideshowVideoProjectClass.projectSetup()