# Yes, I know I'm building a RB app. And yes, I know, this is Tom Brady. But the API I plan on using doesn't have statisical
# data samples available for any position by QB, so, beggars can't be choosers. This code is simply to get a feel for the
# JSON objects I'll be working with, accessing them as quickly and as efficiently as possible, and then working to include
# SQL commands to post this back to a database for easier reference/calling/etc. to build my models from.

import json
import requests

# Source of JSON object to access
source = 'http://www.fantasyfootballnerd.com/service/player/json/test/13/'

# Retrival of that JSON object
get_obj = requests.get(source)

# Accessing the content of the JSON object
obj_content = get_obj.content

# Final formating of the JSON object data to access
data = json.loads(obj_content)

# Root of JSON object to use when iterating through the object
statskey = data['Stats']

# Defining a function that will iterate through the past 10 years of stats data
def getYear():
	for x in range(2005, 2016):
		yield str(x)

# Defining a function that will iterate through each of the 17 weeks of an NFL regular season
def getWeek():
	for x in range(1, 18):
		yield str(x)

# Storing the yearly and weekly functions in variables to make them iterable.
# NOTE: I can't get BOTH to work in a single function, so my yearlyAccess has been hacked to take manual input of the year
# with iterations through each week of the year.
years = getYear()
weeks = getWeek()

# Defining a function that will take user input for the year, and then iterate through each of the 17 weeks to access 
# each key value for each week of each year
def yearlyAccess(year):
	# Below is an example of how I'd execute this code *outside* of Sublime, which doesn't seem to play well with raw_input
	# year = raw_input("Please insert the year, between 2005 and 2015, that'd you like to access.")
	try:
		for x in weeks:
			root = statskey[str(year)][x]
			
			pass_att = int(root['passAttempts'])
			pass_yds = int(root['passYards'])
			pass_td = int(root['passTD'])
			rush_att = int(root['rushAttempts'])
			rush_yards = int(root['rushYards'])
			rush_td = int(root['rushTD'])
			completions = int(root['completions'])

			# Example of possible of output, which should be able to be modified/added to with PyMySQL to post to a database table.
			# Basically, I'd have a 2001 season table, and a column for each value. Once I've entered a year, the function would
			# run and then populate each column as directed by the SQL command issued through PyMySQL (not present in this example)
			print "Season: " + str(year) + ", " + "Week: " + str(x) + ", " + "Pass Attempts: " + str(pass_att) + " by Tom Brady"

	except:
		pass

yearlyAccess(2001)
