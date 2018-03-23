def assist_levels(data):
    m = {"None": [0], "Pass": [1,2,3,4]}
    m2 = {v: k for k,vv in m.items() for v in vv}
    data["assist_method"] = data.assist_method.map(m2).astype("category", categories=set(m2.values()))
    ct = data["assist_method"].value_counts()
    dimension = ct.size
    return dimension