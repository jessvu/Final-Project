import requests
import facebook  #pip install facebook-sdk
import json
from datetime import datetime
import calendar 


CACHE_FNAME = "facebook_posts.json"
try:
    cache_file = open(CACHE_FNAME,'r')
    cache_contents = cache_file.read()
    cache_file.close()
    CACHE_DICTION = json.loads(cache_contents)
except:
    CACHE_DICTION = {}

access_token = None
if access_token is None:
    access_token = input("\nCopy and paste token from https://developers.facebook.com/tools/explorer\n>  ")

graph = facebook.GraphAPI(access_token)
#all_files = ['message', 'created_time', 'likes']
#all_fields = ['message', 'created_time', 'description', 'caption', 'link', 'place', 'status_type']
#all_fields = ','.join(all_fields)

def getFB_likes(me):
	me = graph.get_connections('me', 'likes', fields= 'created_time, name, category, link', limit = 150) 
	if likes in CACHE_DICTION:
		print("Data in Cache")
		data = CACHE_DICTION[me]
		return data
	else:
		print("Making a request for new data...")
		uh = urllib.request.urlopen(url)
		data = uh.read().decode()
		try:
			CACHE_DICTION[me] =  json.loads(data)
			dumped_json_cache = json.dumps(CACHE_DICTION)
			fw = open(CACHE_FNAME,"w")
			fw.write(dumped_json_cache)
			fw.close() # Close the open file
			return CACHE_DICTION[me]
		except:
			print("Wasn't in cache and wasn't valid search either")
			return None

	#print(json.dumps(likes, indent = 4))

#while True:
#	try:
#		with open('facebook_posts.json','a') as f:
#			for like in likes['data']:
#				f.write(json.dumps(like)+"\n")
#			likes = requests.get(likes)['paging']['next'].json()
#	except KeyError:
		#ran out of posts
#		break




