# load libraries
import xml.etree.cElementTree as cET

#get the users that have contributed to this OSM file
def get_users(osm):
    users = set()
    for _, element in cET.iterparse(osm):
        for e in element:
            if 'uid' in e.attrib:
                users.add(e.attrib['uid'])
    return users