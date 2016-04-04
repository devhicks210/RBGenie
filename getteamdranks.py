import pymysql

# Access .txt file with team D ranks...BeautifulSoup wasn't working as easily as I needed it to (or, I'm just not good with # it, so I just copy/pasted each year's ranks from here: http://espn.go.com/nfl/statistics/team/_/stat/rushing/position# /defense/year/2011. I just flipped through the years, updated the DB table I was pointing at, and boom.
# NOTE: I left the code in where I built the dictionary. I could have probably done that easier, but, whatever. It's done
# and I can re-use easily now.

dranks = open('2015rushdranks.txt')

# Accessing SQL DB and looking into desired table

conn = pymysql.connect(host='localhost', port=XXXXX, user='XXXXX', passwd='XXXXX', db='XXXXX')
cur = conn.cursor()

# Creating blank dictionary to update an add team names and abbreviations
# NOTE: It WAS a blank dict, but once I built it and ran the code, I just copied/pasted the print result and then boom,
# I have my "teams" dictionary. But the code is still there for when I built the dictionary. If you want to build to from
# scratch like I initially did, just make sure "teams" is a blank dictionary, then run the commented out code below.

teams = {'Green Bay': 'GB', 'San Diego': 'SD', 'NY Jets': 'NYJ', 'Chicago': 'CHI', 'Seattle': 'SEA', 'Kansas City': 'KC', 'Denver': 'DEN', 'Minnesota': 'MN', 'Indianapolis': 'IND', 'Detroit': 'DET', 'San Francisco': 'SF', 'NY Giants': 'NYG', 'New Orleans': 'NO', 'Buffalo': 'BUF', 'Baltimore': 'BAL', 'Carolina': 'CAR', 'Houston': 'HOU', 'Arizona': 'ARI', 'Cincinnati': 'CIN', 'Tampa Bay': 'TB', 'Pittsburgh': 'PIT', 'New England': 'NE', 'Dallas': 'DAL', 'Washington': 'WAS', 'Philadelphia': 'PHI', 'Miami': 'MIA', 'Tennessee': 'TEN', 'Los Angeles': 'STL', 'Cleveland': 'CLE', 'Atlanta': 'ATL', 'Oakland': 'OAK', 'Jacksonville': 'JAC'}

for x in dranks:
	holder = x.strip().split()

	if not holder[2].isdigit():
		rank = holder[0]
		team = holder[1] + " " + holder[2]
		ypa = holder[5]
		ypg = holder[8]

		team = teams[team]

		cur.execute("""INSERT INTO dRanks_2011 (rank, team, ypa, ypg)
					VALUES ('%s', '%s', '%s', '%s');""" % (rank, team, ypa, ypg))
		conn.commit()

		print rank, team, ypa, ypg, "SUCCESS!"

		# if team == "Green Bay":
		# 	teams.update({team:'GB'})

		# elif team == "San Diego":
		# 	teams.update({team:'SD'})

		# elif team == "NY Jets":
		# 	teams.update({team:'NYJ'})

		# elif team == "Kansas City":
		# 	teams.update({team:'KC'})

		# elif team == "San Francisco":
		# 	teams.update({team:'SF'})

		# elif team == "New Orleans":
		# 	teams.update({team:'NO'})

		# elif team == "Tampa Bay":
		# 	teams.update({team:'TB'})

		# elif team == "New England":
		# 	teams.update({team:'NE'})

		# elif team == "Los Angeles":
		# 	teams.update({team:'STL'})

		# elif team == "NY Giants":
		# 	teams.update({team:'NYG'})

		# else:
		# 	pass

	else:
		rank = holder[0]
		team = holder[1]
		ypa = holder[4]
		ypg = holder[7]

		team = teams[team]

		cur.execute("""INSERT INTO dRanks_2011 (rank, team, ypa, ypg)
					VALUES ('%s', '%s', '%s', '%s');""" % (rank, team, ypa, ypg))
		conn.commit()

		print rank, team, ypa, ypg, "SUCCESS!"

		# if team == "Chicago":
		# 	teams.update({team:'CHI'})

		# elif team == "Seattle":
		# 	teams.update({team:'SEA'})

		# elif team == "Denver":
		# 	teams.update({team:'DEN'})

		# elif team == "Minnesota":
		# 	teams.update({team:'MN'})

		# elif team == "Indianapolis":
		# 	teams.update({team:'IND'})

		# elif team == "Detroit":
		# 	teams.update({team:'DET'})

		# elif team == "Seattle":
		# 	teams.update({team:'SEA'})

		# elif team == "Buffalo":
		# 	teams.update({team:'BUF'})

		# elif team == "Baltimore":
		# 	teams.update({team:'BAL'})

		# elif team == "Carolina":
		# 	teams.update({team:'CAR'})

		# elif team == "Houston":
		# 	teams.update({team:'HOU'})

		# elif team == "Arizona":
		# 	teams.update({team:'ARI'})

		# elif team == "Cincinnati":
		# 	teams.update({team:'CIN'})

		# elif team == "Pittsburgh":
		# 	teams.update({team:'PIT'})

		# elif team == "Dallas":
		# 	teams.update({team:'DAL'})

		# elif team == "Washington":
		# 	teams.update({team:'WAS'})

		# elif team == "Philadelphia":
		# 	teams.update({team:'PHI'})

		# elif team == "Miami":
		# 	teams.update({team:'MIA'})

		# elif team == "Tennessee":
		# 	teams.update({team:'TEN'})

		# elif team == "Cleveland":
		# 	teams.update({team:'CLE'})

		# elif team == "Atlanta":
		# 	teams.update({team:'ATL'})

		# elif team == "Oakland":
		# 	teams.update({team:'OAK'})

		# elif team == "Jacksonville":
		# 	teams.update({team:'JAC'})

		# else:
		# 	pass

cur.close()
conn.close()
