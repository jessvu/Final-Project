import requests
import facebook  #pip install facebook-sdk
import json
import sqlite3
import datetime
import calendar 

CACHE_FNAME = 'facebook_posts.json'


access_token = None
if access_token is None:
    access_token = input("\nCopy and paste token from https://developers.facebook.com/tools/explorer\n>  ")


graph = facebook.GraphAPI(access_token)
likes = graph.get_connections('me', 'likes', fields= 'created_time, name, category, link', limit =100) 
#print(json.dumps(likes, indent = 4))


l = json.loads(json.dumps(likes))
x = (l['data'])
print(x)

#print(x)

# for date in x:
# 	print(date)
def GetDate(fb):
	daysofweek = [0,0,0,0,0,0,0]
	days = ['Monday', 'Tuesday', 'Wednesday', 'Thurday', 'Friday', 'Saturday', 'Sunday']

	L = []
	for d in fb:

		# L2 = []
		# L3 = []
		dates = (d['created_time'])
		dt = (dates.split('T')[0])
		#print(dt)
		year, month, day = (int(x) for x in dt.split('-'))
		fbday = datetime.date(year, month, day).weekday()
		if fbday==0:
			daysofweek[0]+=1
			fbday = 'Monday'
		elif fbday==1:
			daysofweek[1]+=1
			fbday = 'Tuesday'
		elif fbday==2:
			daysofweek[2]+=1
			fbday = 'Wednesday'
		elif fbday==3:
			daysofweek[3]+=1
			fbday = 'Thursday'
		elif fbday==4:
			daysofweek[4]+=1
			fbday = 'Friday'
		elif fbday==5:
			daysofweek[5]+=1
			fbday = 'Saturday'
		elif fbday==6:
			daysofweek[6]+=1
			fbday ='Sunday'
		L.append(fbday)
	return L

date = GetDate(x)
print(date)
# print(newdict)
#print(newlist)

# for weekday in L:
# 	print(weekday)
	#print(L.append(fbday))
	# day_liked = (fbday,dt)
	#print(dict(zip(fbday,dt)))

	# L.append(dt)
	# L2.append(dates)
	# L3.append(names)
	# day_liked = (dict(zip(L2, L)))
	# print(day_liked)
	#print(L3.append(day_liked))
	#print(date_liked)
	#print({names:date_liked})
	#print(L3.append(day_liked))

	#print (dict(zip(days, daysofweek)))

while True:
	try:
		with open(CACHE_FNAME,'a') as f:
			for like in likes['data']:
				f.write(json.dumps(like)+"\n")
			likes = requests.get(likes['paging']['next']).json()

	except KeyError:
		#ran out of posts
		break


print('creating database')
conn = sqlite3.connect('FB_APIAndDB.sqlite')
cur = conn.cursor()
print('finished creating database')

cur.execute('DROP TABLE IF EXISTS Pages')
cur.execute('CREATE TABLE Pages (name TEXT, date_liked DATETIME, day TEXT)')


for info in x:
	weekday = date[x.index(info)] 
	tup = info['name'], info['created_time'], weekday
	cur.execute('INSERT INTO Pages (name, date_liked, day) VALUES(?,?,?)', tup)
# for weekday in L:
# 	tup2 = weekday['day'],
# 	cur.execute('INSERT INTO Pages (day) VALUES(?)', tup2)

conn.commit()



