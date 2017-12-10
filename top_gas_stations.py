def get_gas_stations(data):
    gas_stations=data.aggregate([{"$match":{"feature.amenity":"fuel"}},
                       {"$group":{"_id":"$feature.name","count":{"$sum":1}}},
                       {"$sort":{"count":-1}},
                       {"$limit":10}
                      ])
    for result in gas_stations:
        print(result)