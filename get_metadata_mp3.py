
import eyeD3

def get_meta(path):
    tag = eyeD3.Tag()
    tag.link(path)
    print "Artist: %s" % tag.getArtist()
    print "Album: %s" % tag.getAlbum()
    print "Track: %s" % tag.getTitle()
    TrackNum, TrackTotal = tag.getTrackNum()
    print "Track #: %d" % TrackNum
    print "Track TOtal: %d" % TrackTotal
    print "Release Year: %s" % tag.getYear()

def update_meta(path):
    tag = eyeD3.Tag()
    tag.link(path)
    tag.setArtist("ARTIST")
    tag.setTitle("TITLE")
    tag.setDate("2012")
    tag.setGenre("GENRE")
    tag.setAlbum("ALBUM")
    tag.setTrackNum((12, 12))
    tag.update()

path = 'D:/1.mp3' 
get_meta(path)
update_meta(path)
get_meta(path)
