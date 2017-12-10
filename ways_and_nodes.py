def get_ways_and_nodes(data):
    print "Number of nodes:",data.find({'type':'node'}).count()
    print "Number of ways:",data.find({'type':'way'}).count()