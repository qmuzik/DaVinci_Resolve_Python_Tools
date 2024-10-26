#!/usr/bin/env python

"""
- FPE Project Setup Script
- Script that automates a FPE Podcast Project Creation/Setup with Imported Media to The Timeline
- By Quincy Muzik 10/25/2024
"""

class FPEPodcastProjectClass:

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
        podcastFileName = 'J:\\DaVinci Resolve Project Setup Files\\FPE Podcast\\Podcast'

        # Import Starting Files
        podcastClips = mediaPool.ImportMedia(introFileName,podcastFileName)

        # Create a podcast with footage
        timeline = mediaPool.CreateTimelineFromClips('Podcast',podcastClips)

        # Save the new Project
        newProject = projectManager.SaveProject()

        # Open the Edit Page to Start Editing
        startingPage = resolve.OpenPage("edit")

# SCRIPT EXECUTION 
FPEPodcastProjectClass.projectSetup()