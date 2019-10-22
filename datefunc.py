import datetime  
import pytz
import calendar
from dateutil.relativedelta import *

t = datetime.time(1, 10, 20, 13)  
print(t)
today = datetime.date.today()
print(today)
print(today.ctime())

print('Year:', today.year)  
print('Month:', today.month)  
print('Day :', today.day)  
print('Time :', datetime.time())


x = datetime.datetime(2018, 9, 15)

print(x.strftime("%b %d %Y %H:%M:%S %Z")) 
print(today.strftime("%j")) 

x = datetime.datetime.now()
print(x)
print(x.strftime("%z"))

naive = datetime.datetime.now()
zone = pytz.timezone('Asia/Kolkata')

d_aware = zone.localize(naive)
print(naive.tzinfo)
print(d_aware)

	
my_birthday = datetime.datetime(1985, 10, 20, 17, 55)
brothers_birthday = datetime.datetime(1992, 6, 25, 18, 30)


my_birthday = zone.localize(my_birthday)
brothers_birthday = zone.localize(brothers_birthday)

diff = brothers_birthday - my_birthday
print(diff)


today = datetime.datetime.now()
ninety_days = datetime.timedelta(days=1)

target_date = today + ninety_days

print(target_date.strftime("%A"))

now = datetime.datetime.now()
print(calendar.monthrange(now.year, now.month)[1])
print(calendar.monthrange(now.year, now.month-3)[1])


num_days = calendar.monthrange(now.year, now.month)[1]
days = [datetime.date(now.year, now.month, day) for day in range(1, num_days+1)]
print(days)
nowdays	=	[]
for day in range(1, num_days+1):
	datefor	=	datetime.date(now.year, now.month, day)
	nowdays.append(datefor.strftime("%d:%b:%Y"))
	# nowdays.append(datetime.date(now.year, now.month, day))
	# print(datetime.date(now.year, now.month, day))

print(nowdays)

# nexmonth = datetime.datetime.today()
# nexmonth = nexmonth+relativedelta(months=1)
# print(nexmonth)
# num_days = calendar.monthrange(nexmonth.year, nexmonth.month)[1]
# for day in range(1, num_days+1):
# 	print(datetime.date(nexmonth.year, nexmonth.month, day))

# date = datetime.datetime.today()
# last_day = date + relativedelta(day=1, months=+1, days=-1)
# first_day = date + relativedelta(day=1)
# print(last_day)
# print(first_day)

