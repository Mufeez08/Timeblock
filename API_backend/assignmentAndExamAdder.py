import datetime

from gcsa.event import Event
from gcsa.google_calendar import GoogleCalendar
from gcsa.calendar import Calendar
from datetime import date,time

from gcsa.recurrence import Recurrence

# days of the week
from gcsa.recurrence import SUNDAY,MONDAY,TUESDAY,WEDNESDAY,THURSDAY,FRIDAY,SATURDAY

# possible repetition frequencies
from gcsa.recurrence import SECONDLY, MINUTELY, HOURLY, \
                            DAILY, WEEKLY, MONTHLY, YEARLY



from beautiful_date import *

gc = GoogleCalendar()

def add_recurring_event(Assignment_name, assignment_start_date_list,semester_end_date_list,due_days_list,time_taken):


    start =  datetime.datetime(assignment_start_date_list[0], assignment_start_date_list[1], assignment_start_date_list[2],assignment_start_date_list[3],assignment_start_date_list[4])
    end = start + time_taken * hours


    start_date = start.date()
    # date(2003,5,15) year,month,date
    end_date = date(semester_end_date_list[0],semester_end_date_list[1],semester_end_date_list[2])
    weeks = ((abs(start_date-end_date)).days)//7

    event = Event( Assignment_name,start = start,end = end,recurrence= Recurrence.rule(freq=WEEKLY, by_week_day=due_days_list,
   count = weeks*len(due_days_list)), minutes_before_email_reminder=60)
    gc.add_event(event)




assignment = "webwork"
# class datetime.datetime(year, month, day, hour=0, minute=0, second=0, microsecond=0, tzinfo=None, *, fold=0)
start_date_list = [2023,1,29,17,00]
semester_enddate = [2023,2,18,17,00]
time = 2
duedays_list = [SUNDAY,MONDAY]

add_recurring_event(assignment,start_date_list,semester_enddate,duedays_list,time)




