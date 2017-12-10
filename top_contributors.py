def get_contribs(data):
    result = data.aggregate( [
                                { "$group" : {"_id" : "$created.user",
                                  "count" : { "$sum" : 1} } },
                                { "$sort" : {"count" : -1} },
                                { "$limit" : 10 } ] )
    print(list(result))