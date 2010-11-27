import sys
import os
import urllib2
import dicsmeremote

BASE_RESOURCE_PATH = os.getcwd()

sys.path.append (BASE_RESOURCE_PATH)

BASEURL="http://192.168.0.17:4567"

# Let's instanciate our Discme link object
dr = dicsmeremote.DicsmeRemote(BASEURL)

print dr.addAlbum( "toto" , "tata" )

# Let's get our albums
enum = dr.getAlbumList()

for i, album in enumerate( enum ):

	print album
