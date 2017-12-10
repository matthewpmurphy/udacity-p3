import subprocess

def importFile(db, db_name, json_file, collection):
    mongoimport_cmd = 'mongoimport -h 127.0.0.1:27017 ' + \
                  '--db ' + db_name + \
                  ' --collection ' + collection + \
                  ' --file ' + json_file
    # Before importing, drop collection if it is already running
    if collection in db.collection_names():
        print 'Dropping collection: ' + collection
        db[collection].drop()
    # Execute the command
    print 'Executing: ' + mongoimport_cmd
    subprocess.call(mongoimport_cmd.split())
