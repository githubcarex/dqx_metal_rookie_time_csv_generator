#! /usr/bin/env python

import datetime

subject = "Metal-Rookie"

type = ["C","D","E","A","B"]

schedule = {}

schedule["A"] = [0,5,10,15,20]
schedule["B"] = [1,6,11,16,21]
schedule["C"] = [2,7,12,17,22]
schedule["D"] = [3,8,13,18,23]
schedule["E"] = [4,9,14,19]

result = []

print("//// Start Generate Metal-Rookie Spown Time ////")
print("")
print("Subject,Start Date,Start Time,End Date,End Time,Description,Location,Guests,Event ID")
result.append("Subject,Start Date,Start Time,End Date,End Time,Description,Location,Guests,Event ID")

ofname = "Google_Calender_Metal_Rookie_Time.csv"

jan_1 = datetime.date(2020,1,1)

for i in range(366):

  one_day = jan_1 + datetime.timedelta(days=i)

  amari = (one_day - jan_1).days % 5

  one_day_str = one_day.strftime("%Y/%m/%d")

  #print(one_day.strftime("%Y/%m/%d"), type[amari])

  for sch in schedule[type[amari]]:
    #print sch
    #print '%s,%s,%d:00,%s,%d:30,,,,,' % (subject, one_day_str, sch, one_day_str, sch)
    result.append('%s,%s,%d:00,%s,%d:30,,,,,' % (subject, one_day_str, sch, one_day_str, sch))

print("//// Output ////")
with open(ofname, mode='w') as f:

  f.write('\n'.join(result))

print("")
print("Finish")

