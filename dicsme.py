import os
import sys
import xbmcaddon
import urllib2


__scriptname__ = "dicsme"
__author__ = "Clodeindustrie"
__url__ = ""
__svn_url__ = ""
__credits__ = ""
__version__ = "0.1"
__XBMC_Revision__ = "22240"


BASE_RESOURCE_PATH = xbmc.translatePath( os.path.join( os.getcwd(), 'resources', 'lib' ) )

sys.path.append (BASE_RESOURCE_PATH)

__settings__ = xbmcaddon.Addon(id='script.dicsme')

__language__ = __settings__.getLocalizedString

if __name__ == "__main__":
    import gui
    ui = gui.GUI( "script-GmailChecker-main.xml" , os.getcwd(), "Default")
    ui.doModal()
    del ui
    sys.modules.clear()