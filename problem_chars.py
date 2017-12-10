import re
import xml.etree.cElementTree as cET

lower_case = re.compile(r'^([a-z]|_)*$')
colon = re.compile(r'^([a-z]|_)*:([a-z]|_)*$')
badchars = re.compile(r'[=\+/&<>;\'"\?%#$@\,\. \t\r\n]')

#search tags for three types of elements, ones that value values that are all lowercase and are valid, ones that are valid but have colons, and one that looks for bad or problem characters
def key_type(element, keys):
    if element.tag == "tag":
        for tag in element.iter('tag'):
            k = tag.get('k')
            if lower_case.search(k):
                keys['lower_case'] += 1
            elif colon.search(k):
                keys['colon'] += 1
            elif badchars.search(k):
                keys['badchars'] += 1
            else:
                keys['other'] += 1
    return keys

#execute search on osm file
def search_keys(osm):
    keys = {"lower_case": 0, "colon": 0, "badchars": 0, "other": 0}
    for _, element in cET.iterparse(osm):
        keys = key_type(element, keys)

    return keys