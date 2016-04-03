# Importing libraries to handle API requests, SQL commands, and JSON object handling

import json
import pymysql
import requests

# API information

endpoint = "http://www.fantasyfootballnerd.com/service/players/json/XXXXX/"    # plus KEY

# Accessing SQL DB and looking into desired table

conn = pymysql.connect(host='localhost', port=XXXXX, user='root', passwd='XXXXX', db='XXXXX')
cur = conn.cursor()

# Accessing JSON object, getting total count of entires in the object

get_obj = requests.get(endpoint)
obj_content = get_obj.content
data = json.loads(obj_content)
total_objs = range(1, len(data['Players']))

# Iterate through each entry in the JSON object to get only the RBs, and then post them back on our DB

for x, y in zip(data['Players'], total_objs):
	try:
		if data['Players'][y]['position'] == "RB":
			playerId = int(data['Players'][y]['playerId'])
			active = int(data['Players'][y]['active'])
			fname = data['Players'][y]['fname']
			lname = data['Players'][y]['lname']
			team = data['Players'][y]['team']
			height = data['Players'][y]['height']
			weight = data['Players'][y]['weight']
			dob = data['Players'][y]['dob']
			college = data['Players'][y]['college']

			cur.execute("""INSERT INTO allBacks (id, active, fname, lname, team, height, weight, dob, college)
					VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s');""" % (playerId, active, fname, lname, team, height, weight, dob, college))
			conn.commit()

			print playerId, fname, lname, "SUCCESSFULLY ADDED"
	except:
		print "FAILURE FOR:", playerId

cur.close()
conn.close()

