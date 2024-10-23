#!/usr/bin/env python

# Project Template Generator Version 1.0 
# By Quincy Muzik
# App that allows a user to have automatic setup workspaces for DaVinci Resolve

# Outline of Program Operation:
# 1. Script Runs (Either a Tool shelf or via Terminal)
# 2. User can select a project template type with different premade workspaces/media in media pool and timeline
# 3. User came name new project
# 4. Project will open with new media and pre-determined settings

# API's for DaVinci Resolve
import DaVinciResolveScript as dvr_script
import sys
import os
import shutil

class TemplateGenerator:

    # Assign Resolve
    # DO THIS AT THE START OF EVERY SCRIPT!!!
    resolve = dvr_script.scriptapp("Resolve")

    # ACCESSORS & MUTATORS

    # Get Project Manager 
    projectManager = resolve.GetProjectManager()

    # Get Current Project
    project = resolve.GetCurrentProject()

    # Get Media Pool
    mediaPool = resolve.GetMediaPool()

    # Get Media Storage
    mediaStorage = resolve.GetMediaStorage()

    # Get Current Timline 
    currentTimeline = resolve.GetCurrentTimeline()

    # METHODS & FUNCTIONS

    # Use Fusion to allow creation of GUI 

    # Select a Template
        #  If one does not exist, then allow the user to create one 

    # Create the Project with custom name
    projectName = input('Name for this project: ')
    newProject = projectManager.CreateProject(projectName)

    # Allow user to select Import Media for Project

    # Put the media on the Timeline in order

    # Close the GUI Window and Terminate the Script



# Main Method
TemplateGenerator()

# TODO FUTURE Updates:
# Have a GUI to make it easier for the user
# Allow the user to create a new template within the script
# Allow the user to delete pre existing templates
# Allow the user to select media import for template
