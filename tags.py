# load libraries
import xml.etree.cElementTree as cET

#count the number of unique elements in our file to get a picture of the data structure
def count_tags(osm):
    tags = {}
    for event, elem in cET.iterparse(osm):
        if elem.tag in tags:
            tags[elem.tag] += 1
        else:
            tags[elem.tag] = 1
    return tags

