import datetime
from datetime import date,time

from gcsa.recurrence import SUNDAY,MONDAY,TUESDAY,WEDNESDAY,THURSDAY,FRIDAY,SATURDAY

class Assignments:

    def __init__(self,assignment_name,deadlinedate,deadlinetime,duedayslist,difficultylevel,timetaken):
        self.assignment_name = assignment_name
        self.deadlinedate = deadlinedate
        self.deadlinetime = deadlinetime
        self.duedayslist = duedayslist
        self.difficultylevel = difficultylevel
        self.timetaken = timetaken

    def get_assignment_name(self):
        return self.assignment_name

    def get_datetime_deadline(self):
        datelist = self.deadlinedate.split("-")
        month = int(datelist[0])
        date = int(datelist[1])
        year = int(datelist[2])
        timelist = self.deadlinetime.split(":")
        hours = timelist[0]
        minutes = timelist[2]
        return datetime.datetime(year,month,date,hours,minutes)

    def getduedayslist(self):
        duedayslist = []
        for i in self.duedayslist:
            if i == "Sun":
                duedayslist.append(SUNDAY)
            elif i == "Mon":
                duedayslist.append(MONDAY)
            elif i == "Tue":
                duedayslist.append(TUESDAY)
            elif i == "Wed":
                duedayslist.append(WEDNESDAY)
            elif i == "Thu":
                duedayslist.append(THURSDAY)
            elif i == "Fri":
                duedayslist.append(FRIDAY)
            else:
                duedayslist.append(SATURDAY)
        return duedayslist

    def getdifficulty(self):
        return self.difficultylevel

    def timetaken(self):
        return int(self.timetaken)