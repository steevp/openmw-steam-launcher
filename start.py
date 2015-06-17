#!/usr/bin/env python2 
import os, sys
from ctypes import CDLL

os.environ['SteamAppId'] = '22320'

# Steam Overlay
os.environ['LD_PRELOAD'] = os.getenv('HOME') + '/.local/share/Steam/ubuntu12_64/gameoverlayrenderer.so'

steam_api = CDLL('./libsteam_api.so')
try:
    steam_api.SteamAPI_Init()
except:
    print 'Failed to initialize Steam API'
    sys.exit(1)

os.system('openmw')
