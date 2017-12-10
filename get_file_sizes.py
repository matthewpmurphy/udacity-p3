import os

def getFileSizes(osmFile):
    print 'The original OSM file is {} MB'.format(os.path.getsize(osmFile)/1.0e6) # convert from bytes to megabytes
    print 'The JSON file is {} MB'.format(os.path.getsize(osmFile + ".json")/1.0e6) # convert from bytes to megabytes