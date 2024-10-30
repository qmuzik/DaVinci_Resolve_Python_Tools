#!/usr/bin/env python

"""
- Video Project Setup Script
- Script that automates a Video Project Setup with Imported Media to The Timeline
- By Quincy Muzik 10/30/2024
"""

class VideoProjectClass:

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
        introFileName = 'J:\\DaVinci Resolve Project Setup Files\\FPE Podcast\\Intro'
        #podcastFileName = 'J:\\DaVinci Resolve Project Setup Files\\FPE Podcast\\Podcast'

        # Import Starting Files
        #videoClips = mediaPool.ImportMedia(introFileName)#,podcastFileName)

        # Create a podcast with footage
        #timeline = mediaPool.CreateTimelineFromClips('Video',podcastClips)

        # Save the new Project
        newProject = projectManager.SaveProject()

        # Open the Edit Page to Start Editing
        startingPage = resolve.OpenPage("edit")

# SCRIPT EXECUTION 
VideoProjectClass.projectSetup()
