# Importing libraries to handle API requests, SQL commands, and JSON object handling

import json
import pymysql
import requests

# API information

endpoint = "http://www.fantasyfootballnerd.com/service/player/json/"    # plus KEY, plus PLAYERID
key = 'XXXXX'

# Accessing SQL DB and looking into desired table

conn = pymysql.connect(host='localhost', port=XXXXX, user='XXXXX', passwd='XXXXX', db='XXXXX')
cur = conn.cursor()
cur.execute("""SELECT player_id FROM rblist;""")
rows = cur.fetchall()

# Creating a holder for all running back IDs, then filling it with said IDs

rb_ids = []

for row in rows:
	for col in row:
		rb_ids.append(str(col))

# Creating a holder for running back API endpoints, then filling with with said completed endpoints

rb_endpoints = []

for x in rb_ids:
	rb_endpoints.append(str(endpoint + key + x + "/"))

# Defining functions to get the past 10 years worth of data for each of the 17 weeks of the NFL regular season

def getYear():
	for x in range(2005, 2016):
		yield str(x)

def getWeek():
	for x in range(1, 18):
		yield str(x)

years = getYear()
weeks = getWeek()

# Iterating through each API endpoint, hitting it, and getting the necessary data back.

for x in rb_endpoints:
	get_obj = requests.get(x)
	obj_content = get_obj.content
	data = json.loads(obj_content)
	statskey = data['Stats']

	try:
		rush_att = int(statskey['2015']['1']['rushAttempts'])
		rush_yards = int(statskey['2015']['1']['rushYards'])
		rush_td = int(statskey['2015']['1']['rushTD'])
		receptions = int(statskey['2015']['1']['receptions'])
		rec_yards = int(statskey['2015']['1']['recYards'])
		rec_td = int(statskey['2015']['1']['recTD'])
		fum_lost = int(statskey['2015']['1']['fumbleLost'])

		cur.execute("""INSERT INTO season_2015 (carries, rushyds, runtd, rec, recyds, rectd, fum)
				VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s');""" % (rush_att, rush_yards, rush_td, receptions, rec_yards, rec_td, fum_lost))
		conn.commit()

	except:
		pass

cur.close()
conn.close()
