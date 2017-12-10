def get_religion(data):
    religion=data.aggregate([{"$match":{"feature.amenity":"place_of_worship"}},
                        {"$group":{"_id":"$feature.religion","count":{"$sum":1}}},
                        {"$sort":{"count":-1}},
                        {"$limit":1}
                        ])
    for result in religion:
        print result