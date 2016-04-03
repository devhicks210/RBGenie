# Importing libraries to handle API requests, SQL commands, and JSON object handling

import json
import pymysql
import requests
import re

# API information

endpoint = "http://www.fantasyfootballnerd.com/service/player/json/"    # plus KEY plus PLAYERID
key = 'XXXXX'

# Accessing SQL DB and looking into desired table

conn = pymysql.connect(host='localhost', port=XXXXX, user='XXXXX', passwd='XXXXX', db='XXXXX')
cur = conn.cursor()
cur.execute("""SELECT id FROM allBacks;""")
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

# Iterating through each API endpoint, hitting it, and getting the necessary data back.

for x in rb_endpoints:
	get_obj = requests.get(x)
	obj_content = get_obj.content
	data = json.loads(obj_content)
	statskey = data['Stats']

	try:
		if "'" in data['Player']['fname']:
			fname = re.sub("'", "", data['Player']['fname'])
			lname = data['Player']['lname']
			playerId = data['Player']['playerId']
			team = data['Player']['team']

			# This below info is for calculating age...unfortunately, the API's birthday data is not accurate.
			# dob1 = data['Player']['dob']
			# dob3 = ''
			# dob2 = dob1.split('-')
			# d0 = date(int(dob2[0]), int(dob2[1]), int(dob2[2]))
			# d1 = date(2016, 4, 2)
			# delta = d1 - d0

			# for x in dob2:
			# 	dob3 = dob3 + x + ":"

			rush_att = int(statskey['2014']['8']['rushAttempts'])
			rush_yards = int(statskey['2014']['8']['rushYards'])
			rush_td = int(statskey['2014']['8']['rushTD'])
			receptions = int(statskey['2014']['8']['receptions'])
			rec_yards = int(statskey['2014']['8']['recYards'])
			rec_td = int(statskey['2014']['8']['recTD'])
			fum_lost = int(statskey['2014']['8']['fumbleLost'])
			week = int(statskey['2014']['8']['week'])
			opp = statskey['2014']['8']['opponent']
			# dob4 = dob3[:-1]

			cur.execute("""INSERT INTO season_2014 (opp, week, team, fname, lname, rb_id, carries, rushyds, runtd, rec, recyds, rectd, fum)
					VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s');""" % (opp, week, team, fname, lname, playerId, rush_att, rush_yards, rush_td, receptions, rec_yards, rec_td, fum_lost))
			conn.commit()

			print playerId, fname, lname, "SUCCESS!"
		
		elif "'" in data['Player']['lname']:
			fname = data['Player']['fname']
			lname = re.sub("'", "", data['Player']['lname'])
			playerId = data['Player']['playerId']
			team = data['Player']['team']

			rush_att = int(statskey['2014']['8']['rushAttempts'])
			rush_yards = int(statskey['2014']['8']['rushYards'])
			rush_td = int(statskey['2014']['8']['rushTD'])
			receptions = int(statskey['2014']['8']['receptions'])
			rec_yards = int(statskey['2014']['8']['recYards'])
			rec_td = int(statskey['2014']['8']['recTD'])
			fum_lost = int(statskey['2014']['8']['fumbleLost'])
			week = int(statskey['2014']['8']['week'])
			opp = statskey['2014']['8']['opponent']

			cur.execute("""INSERT INTO season_2014 (opp, week, team, fname, lname, rb_id, carries, rushyds, runtd, rec, recyds, rectd, fum)
					VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s');""" % (opp, week, team, fname, lname, playerId, rush_att, rush_yards, rush_td, receptions, rec_yards, rec_td, fum_lost))
			conn.commit()

			print playerId, fname, lname, "SUCCESS!"

		else:
			fname = data['Player']['fname']
			lname = data['Player']['lname']
			playerId = data['Player']['playerId']
			team = data['Player']['team']

			rush_att = int(statskey['2014']['8']['rushAttempts'])
			rush_yards = int(statskey['2014']['8']['rushYards'])
			rush_td = int(statskey['2014']['8']['rushTD'])
			receptions = int(statskey['2014']['8']['receptions'])
			rec_yards = int(statskey['2014']['8']['recYards'])
			rec_td = int(statskey['2014']['8']['recTD'])
			fum_lost = int(statskey['2014']['8']['fumbleLost'])
			week = int(statskey['2014']['8']['week'])
			opp = statskey['2014']['8']['opponent']

			cur.execute("""INSERT INTO season_2014 (opp, week, team, fname, lname, rb_id, carries, rushyds, runtd, rec, recyds, rectd, fum)
					VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s');""" % (opp, week, team, fname, lname, playerId, rush_att, rush_yards, rush_td, receptions, rec_yards, rec_td, fum_lost))
			conn.commit()

			print playerId, fname, lname, "SUCCESS!"

	except:
		print "NO STATS"

cur.close()
conn.close()
