import sys
import os
import xbmc
import xbmcgui
import urllib2
import dicsmeremote

#import threading

_ = sys.modules[ "__main__" ].__language__
__scriptname__ = sys.modules[ "__main__" ].__scriptname__
__version__ = sys.modules[ "__main__" ].__version__
__settings__ = sys.modules[ "__main__" ].__settings__

STATUS=105
UID=100
ID=101
ADD=102
ID2=103
DEL=104
BUT=120
LIST=120
BASEURL="http://127.0.0.1:4567"

class GUI( xbmcgui.WindowXML ):
    
    def __init__( self, *args, **kwargs ):
	  
	  pass
    
    def onInit( self ):
	  self.setup_all()

    def setup_all( self ):
		try:
			self.getControl( STATUS ).setLabel( "C'est parti...")
			
			# Let's instanciate our Discme link object
			dr = dicsmeremote.DicsmeRemote( BASEURL )
			
			# Let's get our albums
			enum = dr.getAlbumList()
			
			for i, album in enumerate( enum ):

				listitem = xbmcgui.ListItem( label2=album['UUID'], label=album['identifier'])

				self.getControl( LIST ).addItem( listitem )

				self.setFocus( self.getControl( LIST ) )
		except:
			error = "Erreur"
			self.getControl( STATUS ).setLabel( error )

    def message(self, message):
		dialog = xbmcgui.Dialog()
		dialog.ok(" My message title", message)    
    
    def onClick( self, controlId ):
		print "click"+str(controlId)
		
		# Detect the source of the click
		if ( controlId == BUT ):
			self.message(self,"are you sure?")
			print self.getControl( controlId ).getSelectedItem().getLabel()
		elif ( controlId == ADD):
			self.getList()

    def onFocus( self, controlId ):
		self.controlId = controlId
		print "focus"+str(controlId)
		if ( controlId == UID ):
			keyboard = xbmc.Keyboard('mytext')
			keyboard.doModal()
			if (keyboard.isConfirmed()):
				self.getControl( UID ).setLabel(keyboard.getText())
			else:
				self.getControl( UID ).setLabel('user canceled')


		
#list
# toto = eval(urllib2.urlopen('http://127.0.0.1:4567/list').read())
# if ( len(toto) > 0 ) :
# 	print toto
# else:
# 	print "vide"


# # track details
# toto2 = eval(urllib2.urlopen("http://127.0.0.1:4567/track/super%20tramp").read())
# if ( len(toto2) > 0 ) :
# 	print toto2
# else:
# 	print "vide"
# 		
# #ADD
# req = urllib2.Request(url='http://127.0.0.1:4567/add', data='uid=grostest&id=grostoto')
# print urllib2.urlopen(req).read()
# 
# # #DEL
# req = urllib2.Request(url="http://127.0.0.1:4567/super%20tramp", data='_method=delete')
# print urllib2.urlopen(req).read()

def onAction( self, action ):
	if ( action.getButtonCode() in CANCEL_DIALOG ):
		print "Closing"
		self.close()


		#    	global t
		#
		#    	interval = __settings__.getSetting( "interval" )
		#
		#    	if interval == "0": timer = 60
		#    	if interval == "1": timer = 300
		#    	if interval == "2": timer = 600
		#
		#    	t = threading.Timer(float(timer), self.setup_all)
		#    	t.start()
