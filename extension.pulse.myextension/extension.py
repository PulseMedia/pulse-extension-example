#!/usr/bin/python
# -*- coding: utf-8 -*-
#

import xbmcaddon

addon = xbmcaddon.Addon('extension.pulse.myextension') #ExtensionID
initApiCall = addon.getSetting('apiCall') #Read out settings from Settings.xml with the respective id (id = "apiCall")

pulseapi = None
Tool = None

def Call(call, *args): #Wrapper Function
    global pulseapi
    argParsed = call
    for arg in args:
        argParsed = argParsed + "/" + str(arg)
    pulseapi(argParsed)

class Extension:

    def __init__(self, api, tools):
        global pulseapi #Making global variable "pulseapi" accessible
        global Tool #Making global variable "Tool" accessible

        pulseapi = api #Set PulseApi to the global variable (for caching)
        Tool = tools #Set Tools to the global variable (for caching)

        Call(initApiCall) #Run ApiCall which has been set in Settings.xml (and use Wrapper function)
        #Alternative can also be used:
        #pulseapi(initApiCall)

    def onPlay(self, url): #Will be called if Pulse try to start playing an Media which contains the extension Badge ([myextension])
        return url


    # FOR MORE INFORMATION VISIT: https://www.pulse-player.tv/extension
