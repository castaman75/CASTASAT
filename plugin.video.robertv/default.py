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
YOUTUBE_CHANNEL_ID9 = "UCica1XyzfrHl8AC5N-qKYvA"
YOUTUBE_CHANNEL_ID10 = "HobbynewsTV"
YOUTUBE_CHANNEL_ID11 = "UCWcp1Mwm7_bJ-mVoZb8TdkQ"
YOUTUBE_CHANNEL_ID12 = "Mretaprime"
YOUTUBE_CHANNEL_ID13 = "UC5hBvytNbuALxppbRJBluyg"
YOUTUBE_CHANNEL_ID14 = "albertochicotetv"
YOUTUBE_CHANNEL_ID15 = "CanalComedyCentral"
YOUTUBE_CHANNEL_ID16 = "UCFKcIYyLxfQBAD4r0Bq1RfA"
YOUTUBE_CHANNEL_ID17 = "ElTerrat"
YOUTUBE_CHANNEL_ID18 = "UCnkjyVyvCg4RItUvSGDZ7_g"


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
        title="VODAFONE YU",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID9+"/",
        thumbnail="https://yt3.ggpht.com/a/AGF-l7-OXKZwZtoiOufxQxhHsQY4Ht6TwaDhkd1FrA=s288-c-k-c0xffffffff-no-rj-mo",
        folder=True )
    plugintools.add_item(
        #action="", 
        title="HOBBY CONSOLAS",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID10+"/",
        thumbnail="https://yt3.ggpht.com/a/AGF-l78gFd8V1jhUJcFu2pwe26blJi2n7c91X7I8HA=s288-c-k-c0xffffffff-no-rj-mo",
        folder=True )
    plugintools.add_item(
        #action="", 
        title="TUBER VIEJUNER",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID11+"/",
        thumbnail="https://yt3.ggpht.com/a/AGF-l7_49QcJR8rRbUDIXdG_Lqi_8QF0Kxna03l6=s288-c-k-c0xffffffff-no-rj-mo",
        folder=True )
    plugintools.add_item(
        #action="", 
        title="ETA PRIME",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID12+"/",
        thumbnail="https://yt3.ggpht.com/a/AGF-l7_3zrCe1yW7QwCIIUMoqf2KcbJpAL5LbaDWvA=s288-c-k-c0xffffffff-no-rj-mo",
        folder=True )	
    plugintools.add_item(
        #action="", 
        title="LA LENGUA MODERNA",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID13+"/",
        thumbnail="https://yt3.ggpht.com/a/AGF-l7-I05nAXjD8UfiglDVWqiivrJ6k1wNKw3TWlQ=s288-c-k-c0xffffffff-no-rj-mo",
        folder=True )
    plugintools.add_item(
        #action="", 
        title="CHICOTE TUBE",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID14+"/",
        thumbnail="https://yt3.ggpht.com/a/AGF-l79eGpi1dHFBEQdK7L-Tswv-BoeTU9EM98uAsw=s288-c-k-c0xffffffff-no-rj-mo",
        folder=True )
    plugintools.add_item(
        #action="", 
        title="COMEDY CENTRAL",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID15+"/",
        thumbnail="https://yt3.ggpht.com/a/AGF-l79ySmszdv7SaDBvwdbGyjaPekkfNP2ysahxXw=s288-c-k-c0xffffffff-no-rj-mo",
        folder=True )	
    plugintools.add_item(
        #action="", 
        title="PHI BETA LAMBDA",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID16+"/",
        thumbnail="https://yt3.ggpht.com/a/AGF-l79G11X7KAKflc4QSHemd4NddDGKeoocidle=s288-c-k-c0xffffffff-no-rj-mo",
        folder=True )
    plugintools.add_item(
        #action="", 
        title="EL TERRAT",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID17+"/",
        thumbnail="https://yt3.ggpht.com/a/AGF-l7_zRSNNQLzLG46Foqzw41zjfaZrMZ1VNAB9-w=s288-c-k-c0xffffffff-no-rj-mo",
        folder=True )	
    plugintools.add_item(
        #action="", 
        title="EL RINCÓN DE CHINA",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID18+"/",
        thumbnail="https://dl.dropbox.com/s/rh05a1rrkync3u5/china.jpg",
        folder=True )		
	
run()
