import urllib2

class DicsmeRemote(object):
    """docstring for DicsmeRemote"""
    def __init__(self, baseurl):
		self.BASEURL = baseurl	

    def getAlbum( self, id ):
		f = eval(urllib2.urlopen(self.BASEURL+'/track/'+str(id)).read())
		return f

    def getAlbumList( self ):
		retour = eval(urllib2.urlopen(self.BASEURL+'/list').read())
		return retour
		
    def addAlbum( self , uuid, id ):
		"""docstring for deleteAlbum"""
		req = urllib2.Request(url=self.BASEURL+'/add', data='uid=' + uuid + '&id=' + id)
		return eval(urllib2.urlopen(req).read())

    def deleteAlbum( self, id):
		"""docstring for deleteAlbum"""
		req = urllib2.Request(url=self.BASEURL+"/"+id, data='_method=delete')
		return eval(urllib2.urlopen(req).read())
