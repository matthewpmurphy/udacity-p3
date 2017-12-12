# load libraries
import re
import os
import pprint
from tags import count_tags
from users import get_users
from problem_chars import search_keys
from audit_street_names import audit_streets
from audit_zipcodes import audit_zips
from convert_to_json import convert_file
from connect_to_db import connectToMongo
from import_file import importFile
from get_file_sizes import getFileSizes
from ways_and_nodes import get_ways_and_nodes
from top_contributors import get_contribs
from top_amenities import get_amenities
from top_religion import get_religion
from top_cuisine import get_cuisine
from top_fast_food import get_fast_food
from top_gas_stations import get_gas_stations

#Load OSM file and path, in this case we are looking at New Orleans, LA, USA
filename = "new-orleans_louisiana.osm"
#sample file
#filename = "sample.osm"
path = "./map"
osmFile = os.path.join(path, filename)

#execute count_tags on our osm file
tags = count_tags(osmFile)
#print the results
pprint.pprint(tags)
#get a count of users
users = get_users(osmFile)
print len(users)
#search for valid values and potential problems
keys = search_keys(osmFile)
pprint.pprint(keys)
#audit street names
audit_streets(osmFile)
#audit zip codes
audit_zips(osmFile)
#Create a json file for import into mongo
convert_file(osmFile)
#connect to mongo db
db = connectToMongo()
#Import our file into mongodb
db_name = 'udacity_p3'
collection = 'data'
json_file = osmFile + '.json'
importFile(db, db_name, json_file, collection)
#load db collection into  object for reuse
new_orleans_la_data = db[collection]
#Get size of the OSM file and the JSON file
getFileSizes(osmFile)
#Number of documents
new_orleans_la_data.find().count()
#Number of unique users
len(new_orleans_la_data.distinct('created.user'))
#Number of nodes and ways
get_ways_and_nodes(new_orleans_la_data)
#get the top contributers
get_contribs(new_orleans_la_data)
#get the top religion
get_religion(new_orleans_la_data)
#get the top cuisines
get_cuisine(new_orleans_la_data)
#get the top fast food types
get_fast_food(new_orleans_la_data)
#get the top gas stations
get_gas_stations(new_orleans_la_data)