def make_set(data):
    
    my_list = []

    for item in data:
        if item not in my_list:
            my_list.append(item)
    
    return my_list


def is_set(data):

    my_list = []

    for item in data:
        if item in my_list:
            return False
        elif item not in my_list:
            my_list.append(item)
    
    return True


def union(setA, setB):

    union_list = []

    emptylist = []

    if not is_set(setA) or not is_set(setB):
        return emptylist
    
    else:
        for item in setA:
            union_list.append(item)
        for item in setB:
            if item not in union_list:
                union_list.append(item)
    
    return union_list


def intersection(setA, setB):
    
    union_list = []
    intersection_list = []

    emptylist = []

    if not is_set(setA) or not is_set(setB):
        return emptylist
    
    else:
        for item in setA:
            union_list.append(item)
        for item in setB:
            if item in union_list:
                intersection_list.append(item)
    
    return intersection_list
