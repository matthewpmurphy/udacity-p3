def get_cuisine(data):
    restaurants=data.aggregate([{"$match":{"feature.amenity":"restaurant"}},
                       {"$group":{"_id":"$feature.cuisine","count":{"$sum":1}}},
                       {"$sort":{"count":-1}},
                       {"$limit":10}
                      ])
    for result in restaurants:
        print(result)