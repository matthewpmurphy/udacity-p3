import xml.etree.cElementTree as cET
import json
import codecs

#Convert the file to json and save
CREATED = [ "version", "changeset", "timestamp", "user", "uid" ]

def shape_element(element) :
    node = {}
    if (element.tag == "node") or (element.tag == "way") :
        node["created"]={}
        node["pos"]=[]
        node["id"]=element.attrib["id"]
        node["type"]=element.tag

        try:
            node["pos"].append(float(element.attrib["lat"]))
            node["pos"].append(float(element.attrib["lon"]))
        except:
            pass
        for a in CREATED:

            if a in element.attrib:
                node["created"][a]=element.attrib[a]

        if element.findall("./tag")!=[]:
            node["feature"]={}
            for tag in element.iter("tag"):
                node["feature"][tag.attrib["k"]]=tag.attrib["v"]
    return  node

def convert_file(file_in):

    file_out = "{0}.json".format(file_in)
    data = []
    with codecs.open(file_out, "w") as fo:
        for _, element in cET.iterparse(file_in):
            el = shape_element(element)
            if el:
                data.append(el)
                fo.write(json.dumps(el) + "\n")
    return data