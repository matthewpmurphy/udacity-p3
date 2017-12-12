import re
import xml.etree.cElementTree as cET
from collections import defaultdict

def audit_zipcode(invalid_zipcodes, zipcode):
    twoDigits = zipcode[0:2]

    if not twoDigits.isdigit():
        invalid_zipcodes[twoDigits].add(zipcode)

    elif twoDigits != 95:
        invalid_zipcodes[twoDigits].add(zipcode)

def is_zipcode(elem):
    return (elem.attrib['k'] == "addr:postcode")

def audit(osmfile):
    osm_file = open(osmfile, "r")
    invalid_zipcodes = defaultdict(set)
    for event, elem in cET.iterparse(osm_file, events=("start",)):

        if elem.tag == "node" or elem.tag == "way":
            for tag in elem.iter("tag"):
                if is_zipcode(tag):
                    audit_zipcode(invalid_zipcodes,tag.attrib['v'])

    return invalid_zipcodes

def update_zips(zipcode):
    testNum = re.findall('[a-zA-Z]*', zipcode)
    if testNum:
        testNum = testNum[0]
    testNum.strip()
    if testNum == "LA":
        convertedZipcode = (re.findall(r'\d+', zipcode))
        if convertedZipcode:
            if convertedZipcode.__len__() == 2:
                return (re.findall(r'\d+', zipcode))[0] + "-" +(re.findall(r'\d+', zipcode))[1]
            else:
                return (re.findall(r'\d+', zipcode))[0]
    return zipcode


def audit_zips(osmFile):
    zipcodes = audit(osmFile)

    for street_type, ways in zipcodes.iteritems():
        for zipcode in ways:
            updated_zipcode = update_zips(zipcode)
            if zipcode != updated_zipcode :
                print zipcode, "=>", updated_zipcode