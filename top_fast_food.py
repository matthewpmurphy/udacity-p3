def get_fast_food(data):
    fast_food=data.aggregate([{"$match":{"feature.amenity":"fast_food"}},
                       {"$group":{"_id":"$feature.cuisine","count":{"$sum":1}}},
                       {"$sort":{"count":-1}},
                       {"$limit":10}
                      ])
    for result in fast_food:
        print(result)