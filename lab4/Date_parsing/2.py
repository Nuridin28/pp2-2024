import datetime

x = datetime.datetime.now()
print("Yesterday", x.day - 1)
print("Today", x.day )
print("Tomorrow", x.day + 1)