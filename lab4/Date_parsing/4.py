import datetime
def dif_in_sec(d1, d2):
    diff = d1 - d2
    res = 0;
    res += round(diff.total_seconds())
    print(res)
    
dif_in_sec(datetime.datetime.now() , datetime.datetime(2024, 2, 13, 12, 4))
