import re
import xml.etree.cElementTree as cET
from collections import defaultdict
#Clean up street names so they all use the same abbreviation, print out the ones we updated.
street_type_re = re.compile(r'\b\S+\.?$', re.IGNORECASE)
expected = ["Avenue", "Boulevard", "Commons", "Court", "Drive", "Lane", "Parkway",
                         "Place", "Road", "Square", "Street", "Trail"]
mapping = {'Ave'  : 'Avenue',
           'Blvd' : 'Boulevard',
           'Dr'   : 'Drive',
           'Ln'   : 'Lane',
           'Pkwy' : 'Parkway',
           'Rd'   : 'Road',
           'Rd.'   : 'Road',
           'St'   : 'Street',
           'street' :"Street",
           'Ct'   : "Court",
           'Cir'  : "Circle",
           'Cr'   : "Court",
           'ave'  : 'Avenue',
           'Hwg'  : 'Highway',
           'Hwy'  : 'Highway',
           'Sq'   : "Square"}

def audit_street_type(street_types, street_name):
    m = street_type_re.search(street_name)
    if m:
        street_type = m.group()
        if street_type not in expected:
            street_types[street_type].add(street_name)

def is_street_name(elem):
    return (elem.attrib['k'] == "addr:street")

def audit(osmfile):
    osm_file = open(osmfile, "r")
    street_types = defaultdict(set)
    for event, elem in cET.iterparse(osm_file, events=("start",)):

        if elem.tag == "node" or elem.tag == "way":
            for tag in elem.iter("tag"):
                if is_street_name(tag):
                    audit_street_type(street_types, tag.attrib['v'])

    return street_types

def update_street_name(name, mapping, regex):
    m = regex.search(name)
    if m:
        street_type = m.group()
        if street_type in mapping:
            name = re.sub(regex, mapping[street_type], name)

    return name

def audit_streets(osmfile):
    #take inventory of street names
    streets = audit(osmfile)
    #loops through and show the ones that were updated
    street_type_re = re.compile(r'\b\S+\.?$', re.IGNORECASE)
    for street_type, ways in streets.iteritems():
        for name in ways:
            updated_name = update_street_name(name, mapping, street_type_re)
            if updated_name != name :
                print name, "=>", updated_name