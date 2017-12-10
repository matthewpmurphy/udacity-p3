def get_amenities(data):
    amenities=data.aggregate([{"$match":{"feature.amenity":{"$exists":1}}},
                       {"$group":{"_id":"$feature.amenity","count":{"$sum":1}}},
                       {"$sort":{"count":-1}},
                       {"$limit":10}
                      ])

    for result in amenities:
        print(result)