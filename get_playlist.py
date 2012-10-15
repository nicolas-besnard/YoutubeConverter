from urllib import urlopen
import json
import os

def getPlaylist(playlistID):
	"""
	Return an dict with the "title" & the "video ID"
	"""
	max_results = 50
	flag = True
	i = 1
	count = 1
	playlist_value = dict()
	while flag == True:
		playlist_url = "http://gdata.youtube.com/feeds/api/playlists/{playlist_id}?v=2&alt=json&max-results={max_results_nb}&start-index={index_id}"
		playlist = urlopen(playlist_url.format(playlist_id = playlistID, max_results_nb = str(max_results), index_id = str(i)))
		content = playlist.read();
		my_json = json.loads(content)
		try: total_videos
		except NameError:
			total_videos = my_json[u'feed'][u'openSearch$totalResults'][u'$t']
		# Try to access to entry
		# Sometimes when a video is deleted but still in a playlist, they continue to bo in the playlist
		try: videos = my_json[u'feed'][u'entry']
		except KeyError:
			return (playlist_value)
		for video in videos:
			playlist_value[count] = dict()
			playlist_value[count]['author'] = repr(video[u'title'][u'$t'].partition(' - ')[0])
			playlist_value[count]['title'] =  repr(video[u'title'][u'$t'].partition(' - ')[2])
			playlist_value[count]['id'] = video[u'content'][u'src'].split("/v/")[1][0:11]
			count = count + 1
			if count == total_videos:
				flag = False
		i = i + max_results
	return (playlist_value)

def showPlaylist():
	big = "PL0212F192E077825A"
	small = "PLibkuuutrFxEAiJ-cp6GJm9WIIE9E6KLG"
	for video in getPlaylist(big).values():
		print video['author']
		print video['title']
		print video['id']
