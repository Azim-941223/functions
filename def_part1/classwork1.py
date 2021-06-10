
list_1 = ['name', 'age', '1', '19']
print(list_1)


def my_list():

    new_list = []
    a = list_1[:2] 
    b = list_1[2:]
    a.reverse()
    b.reverse()
    new_list.extend(a)
    new_list.extend(b)
    print(new_list)

my_list()