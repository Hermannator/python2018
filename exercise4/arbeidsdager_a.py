ukedager = ["mandag","tirsdag","onsdag","torsdag","fredag","lørdag","søndag"]

def is_leap_year(year):
    if year%400==0:
        return True
    elif year%100==0:
        return False
    elif year%4==0:
        return True
    return False

def increment(x):
    if x>=0:
        return 1
    else:
        return -1

def weekday_newyear(year):
    for x in range(0,year,increment(year)):
        if is_leap_year(x):
            year+=increment(year)
    return year%7-2

for x in range(1900,1920):
    print(x,' ',ukedager[weekday_newyear(x)])
