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
YOUTUBE_CHANNEL_ID2 = "UC6lJZ9Ctx1vcmRY9cFEPyww"
YOUTUBE_CHANNEL_ID3 = "UCMHb51gmuIuP8dVpsHr-uEw"
YOUTUBE_CHANNEL_ID4 = "UCvosUrZ7hXpzAyobhfztg4w"
YOUTUBE_CHANNEL_ID5 = "UC2MXy4PrVCDt9nduHrdPtuQ"
YOUTUBE_CHANNEL_ID6 = "PirofanWeb1"
YOUTUBE_CHANNEL_ID7 = "mundodesconocido"
YOUTUBE_CHANNEL_ID8 = "UCxIPSNY9-OEP80AKNPvUC8Q"
YOUTUBE_CHANNEL_ID9 = "laf1es"


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
        title="MILENIO LIVE",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID1+"/",
        thumbnail="https://dl.dropbox.com/s/ducxvg4dfmact2v/milenio.jpg",
        folder=True )
    plugintools.add_item(
        #action="", 
        title="LA VIDA MODERNA",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID2+"/",
        thumbnail="https://yt3.ggpht.com/a-/AAuE7mCJSRIhqT_2_ytQS0JO_wJYHCTYOnFr6vITKA=s288-mo-c-c0xffffffff-rj-k-no",
        folder=True )
    plugintools.add_item(
        #action="", 
        title="TIEMPO DE JUEGO",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID3+"/",
        thumbnail="https://yt3.ggpht.com/a/AGF-l78sjGmqHDhPfwUpqO6SgojvMneumI7OpktGpQ=s288-c-k-c0xffffffff-no-rj-mo",
        folder=True )
    plugintools.add_item(
        #action="", 
        title="LA RESISTENCIA",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID4+"/",
        thumbnail="https://yt3.ggpht.com/a-/AAuE7mAmBsMJ1lUp0Vfdf-29F3guVYm9ZpHB2Zy_YQ=s288-mo-c-c0xffffffff-rj-k-no",
        folder=True )
    plugintools.add_item(
        #action="", 
        title="LATE MOTIV",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID5+"/",
        thumbnail="https://yt3.ggpht.com/a-/AAuE7mDXcId39AB_2o7U4-qkgKSqPO-lgbS-T94PCQ=s288-mo-c-c0xffffffff-rj-k-no",
        folder=True )
    plugintools.add_item(
        #action="", 
        title="PIROFAN PIROTECNIA",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID6+"/",
        thumbnail="https://yt3.ggpht.com/a-/AAuE7mBieI2R7spofUV7c9bemcGbSaCIdjr7cg4alA=s288-mo-c-c0xffffffff-rj-k-no",
        folder=True )		
    plugintools.add_item(
        #action="", 
        title="MUNDO DESCONOCIDO",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID7+"/",
        thumbnail="https://yt3.ggpht.com/a-/AAuE7mDgtDW5dCWXvG0Ly4qtA1ewaZi8LfNVZV5b3w=s176-c-k-c0x00ffffff-no-rj-mo",
        folder=True )		
    plugintools.add_item(
        #action="", 
        title="NADIE SABE NADA",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID8+"/",
        thumbnail="https://yt3.ggpht.com/a/AGF-l7_ASa4xVX555wr-yZqGU5abK2z6pdr9UFLJjA=s288-c-k-c0xffffffff-no-rj-mo",
        folder=True )
    plugintools.add_item(
        #action="", 
        title="SOY MOTOR",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID9+"/",
        thumbnail="https://yt3.ggpht.com/a/AGF-l79cYBEN5SXKECLcP6024xJvaL6RT55MWcBjrA=s288-c-k-c0xffffffff-no-rj-mo",
        folder=True )		
	
run()
