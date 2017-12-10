from pymongo import MongoClient
import subprocess
import os

def connectToMongo() :
    pro = subprocess.Popen('mongod', preexec_fn = os.setsid)
    db_name = 'udacity_p3'
    mongo = MongoClient('localhost:27017')
    return mongo[db_name]
