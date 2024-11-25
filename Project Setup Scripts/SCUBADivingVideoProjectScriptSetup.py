#!/usr/bin/env python

"""
- SCUBA Diving Video Project Setup Script
- Script that automates a SCUBA Diving Video Project Creation/Setup with Imported Media to the timeline
- By Quincy Muzik 11/25/2024
"""

class ScubaDivingVideoProjectClass:

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
        videosFolderName = 'J:\\DaVinci Resolve Project Setup Files\\SCUBA Video\\Videos'

        # Import Starting Files
        scubaMedia = mediaPool.ImportMedia(videosFolderName)

        # Create a timeline with project name
        timeline = mediaPool.CreateTimelineFromClips('SCUBA Dive',scubaMedia)

        # Save the new Project
        newProject = projectManager.SaveProject()

        # Open the Edit Page to Start Editing
        startingPage = resolve.OpenPage("edit")

# SCRIPT EXECUTION 
ScubaDivingVideoProjectClass.projectSetup()