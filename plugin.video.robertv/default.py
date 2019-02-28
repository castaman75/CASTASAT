# -*- coding: utf-8 -*-
#------------------------------------------------------------
# http://www.youtube.com/channel/UCGVXCP8-soIb79aQx9bkYSw
#------------------------------------------------------------
# License: GPL (http://www.gnu.org/licenses/gpl-3.0.html)
# Based on code from youtube addon
#------------------------------------------------------------

import os
import sys
import plugintools
import xbmc,xbmcaddon
from addon.common.addon import Addon

addonID = 'plugin.video.robertv'
addon = Addon(addonID, sys.argv)
local = xbmcaddon.Addon(id=addonID)
icon = local.getAddonInfo('icon')

YOUTUBE_CHANNEL_ID1 = "videoblogdeiker"
YOUTUBE_CHANNEL_ID2 = "mundodesconocido"
YOUTUBE_CHANNEL_ID3 = "UC6lJZ9Ctx1vcmRY9cFEPyww"
YOUTUBE_CHANNEL_ID4 = "lagranjahumana"
YOUTUBE_CHANNEL_ID5 = "VMGranmisterio"
YOUTUBE_CHANNEL_ID6 = "TheZOKEproductions"



# Entry point
def run():
    plugintools.log("robertv.run")
    
    # Get params
    params = plugintools.get_params()
    
    if params.get("action") is None:
        main_list(params)
    else:
        pass
    
    plugintools.close_item_list()

# Main menu
def main_list(params):
    plugintools.log("robertv.main_list "+repr(params))

    plugintools.add_item( 
        #action="", 
        title="VIDEOBLOG IKER",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID1+"/",
        thumbnail="https://yt3.ggpht.com/a-/AAuE7mDeEFY66ZhqzQq4J2v1i7ho473TMZLX3NjUmA=s288-mo-c-c0xffffffff-rj-k-no",
        folder=True )
    plugintools.add_item(
        #action="", 
        title="MUNDO DESCONOCIDO",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID2+"/",
        thumbnail="https://yt3.ggpht.com/a-/AAuE7mDgtDW5dCWXvG0Ly4qtA1ewaZi8LfNVZV5b3w=s176-c-k-c0x00ffffff-no-rj-mo",
        folder=True )
    plugintools.add_item(
        #action="", 
        title="LA VIDA MODERNA",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID3+"/",
        thumbnail="https://yt3.ggpht.com/a-/AAuE7mCJSRIhqT_2_ytQS0JO_wJYHCTYOnFr6vITKA=s288-mo-c-c0xffffffff-rj-k-no",
        folder=True )
    plugintools.add_item(
        #action="", 
        title="LA GRANJA HUMANA",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID4+"/",
        thumbnail="https://yt3.ggpht.com/a-/AAuE7mBgfJozTz8vsZgo9cFsGCibG85HngSpPy5Lxw=s288-mo-c-c0xffffffff-rj-k-no",
        folder=True )
    plugintools.add_item(
        #action="", 
        title="VM GRAN MISTERIO",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID5+"/",
        thumbnail="https://yt3.ggpht.com/a-/AAuE7mDbRGFljdJmm7CTRHQuxjVmADGUXpxfyMhZbQ=s288-mo-c-c0xffffffff-rj-k-no",
        folder=True )
    plugintools.add_item(
        #action="", 
        title="ATRAVIESA LO DESCONOCIDO",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID6+"/",
        thumbnail="https://yt3.ggpht.com/a-/AAuE7mBITgHrtaALMdcZ4mKzQRi4x5fwlUqumKCKvg=s288-mo-c-c0xffffffff-rj-k-no",
        folder=True )
	
	
	
run()
