#!/usr/bin/python
# -*- coding: utf-8 -*-
#

import xbmcaddon

addon = xbmcaddon.Addon('extension.pulse.myextension') #ExtensionID
initApiCall = addon.getSetting('apiCall') #Read out settings from Settings.xml with the respective id (id = "apiCall")

pulseapi = None #PulseApi caching

def Call(call, *args): #Wrapper Function
    global pulseapi
    argParsed = call
    for arg in args:
        argParsed = argParsed + "/" + str(arg)  
    pulseapi(argParsed)

class Extension:

    def __init__(self, api):
        global pulseapi #Making global variable "pulseapi" accessible
        pulseapi = api #Set PulseApi to the global variable (for caching)
        
        Call(initApiCall) #Run ApiCall which has been set in Settings.xml (and use Wrapper function)
        #Alternative can also be used:
        #pulseapi(initApiCall)