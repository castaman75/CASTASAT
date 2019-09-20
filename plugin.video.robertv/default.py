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
YOUTUBE_CHANNEL_ID7 = "PirofanWeb1"
YOUTUBE_CHANNEL_ID8 = "UCj0Mcpfdh98SAlyCKJ2DbVw"
YOUTUBE_CHANNEL_ID9 = "UCqD2Z37jXR7cpasLdH8Tj7g"
YOUTUBE_CHANNEL_ID10 = "UCvosUrZ7hXpzAyobhfztg4w"
YOUTUBE_CHANNEL_ID11 = "UC2MXy4PrVCDt9nduHrdPtuQ"
YOUTUBE_CHANNEL_ID12 = "GrupoZeroInves"
YOUTUBE_CHANNEL_ID13 = "UCkDF5-NG0jlPwt0PTzgBM2A"
YOUTUBE_CHANNEL_ID14 = "UCA0AXvVu2kZ4nauMgXs_Naw"
YOUTUBE_CHANNEL_ID15 = "VocesAnonimas3"
YOUTUBE_CHANNEL_ID16 = "valentiestaloco"
YOUTUBE_CHANNEL_ID17 = "UCuz0AziVwPgwcuXXsVp14ng"


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
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID3+"/videos/",
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
    plugintools.add_item(
        #action="", 
        title="PIROFAN PIROTECNIA",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID7+"/",
        thumbnail="https://yt3.ggpht.com/a-/AAuE7mBieI2R7spofUV7c9bemcGbSaCIdjr7cg4alA=s288-mo-c-c0xffffffff-rj-k-no",
        folder=True )
    plugintools.add_item(
        #action="", 
        title="BENDITOS BASTARDOS",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID8+"/",
        thumbnail="https://yt3.ggpht.com/a-/AAuE7mAlQyeJSm3JZpZ9I_2ddigsK773k70vJZjktQ=s288-mo-c-c0xffffffff-rj-k-no",
        folder=True )
    plugintools.add_item(
        #action="", 
        title="EL DESVÁN DE NACHO FERRÓ",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID9+"/",
        thumbnail="https://yt3.ggpht.com/a-/AAuE7mDZDqMdg3xfEpyJQ8iCIRf-YLKQoVYyL5CJNA=s288-mo-c-c0xffffffff-rj-k-no",
        folder=True )
    plugintools.add_item(
        #action="", 
        title="LA RESISTENCIA",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID10+"/",
        thumbnail="https://yt3.ggpht.com/a-/AAuE7mAmBsMJ1lUp0Vfdf-29F3guVYm9ZpHB2Zy_YQ=s288-mo-c-c0xffffffff-rj-k-no",
        folder=True )
    plugintools.add_item(
        #action="", 
        title="LATE MOTIV",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID11+"/",
        thumbnail="https://yt3.ggpht.com/a-/AAuE7mDXcId39AB_2o7U4-qkgKSqPO-lgbS-T94PCQ=s288-mo-c-c0xffffffff-rj-k-no",
        folder=True )
    plugintools.add_item(
        #action="", 
        title="GRUPO ZERO INVESTIGACIÓN",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID12+"/",
        thumbnail="https://yt3.ggpht.com/a-/AAuE7mAY9ozxcuun_YfSpj_VW4tfT0eNvxelyBrUug=s288-mo-c-c0xffffffff-rj-k-no",
        folder=True )
    plugintools.add_item(
        #action="", 
        title="CREEPYPASTAS EVERYWHERE",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID13+"/",
        thumbnail="https://yt3.ggpht.com/a-/AAuE7mDgPVd7GIEqrf5PEN7HwuM0oxCLNLdT01mjfA=s288-mo-c-c0xffffffff-rj-k-no",
        folder=True )
    plugintools.add_item(
        #action="", 
        title="EL DOQMENTALISTA",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID14+"/",
        thumbnail="https://yt3.ggpht.com/a-/AAuE7mDqacDhbm_i0hJFRHsN-IF_EliKcgeE__mSTQ=s288-mo-c-c0xffffffff-rj-k-no",
        folder=True )
    plugintools.add_item(
        #action="", 
        title="VOCES ANÓNIMAS",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID15+"/",
        thumbnail="https://yt3.ggpht.com/a-/AAuE7mBCsHWmFPYkaTLqN-OcoCLbHhMPtHMMa3UMSA=s288-mo-c-c0xffffffff-rj-k-no",
        folder=True )
    plugintools.add_item(
        #action="", 
        title="VALENTI ESTÁ LOCO",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID16+"/",
        thumbnail="https://yt3.ggpht.com/a-/AAuE7mDmZJ6tVgzvj9F28LBJw8mSQPidgM5bEbo-kg=s288-mo-c-c0xffffffff-rj-k-no",
        folder=True )
    plugintools.add_item(
        #action="", 
        title="BRICOMANIA",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID17+"/",
        thumbnail="https://yt3.ggpht.com/a-/AAuE7mBRWXrcv0g8dypEQBB3vyjSwECzsSK4uOnA3A=s288-mo-c-c0xffffffff-rj-k-no",
        folder=True )		
	
	
	
run()
