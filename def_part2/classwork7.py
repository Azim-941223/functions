
dic = {'cola': 'water', 1234: 'numb'}

def take_tuples(dic):

    keys = set(dic.keys())

    values = set(dic.values())

    return keys, values

print(take_tuples(dic))