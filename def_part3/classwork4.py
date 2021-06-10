s1 = {1,2,3,4,5,6,20,50,60,8,9,12,13,15}
def set2(sets_del):
    if len(sets_del) > 0:
        sets_del.pop()
        set2(sets_del)
    else:
        print("OK")
        return

set2(s1)




