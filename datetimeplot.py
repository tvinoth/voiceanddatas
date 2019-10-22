import matplotlib.pyplot as plt
from matplotlib.dates import (YEARLY, DateFormatter,
                              rrulewrapper, RRuleLocator, drange)
import numpy as np
import datetime
import calendar

# Fixing random state for reproducibility
np.random.seed(19680801)


# tick every 5th easter
rule = rrulewrapper(YEARLY, byeaster=1, interval=5)
loc = RRuleLocator(rule)
formatter = DateFormatter('%m/%d/%y')
now 	=	datetime.datetime.now()
num_days = calendar.monthrange(now.year, now.month)[1]
# date1 = datetime.date(now.year, now.month, now.day)
# date1 = datetime.date(1994, 4, 12)
# date2 = datetime.date(2004, 4, 12)
delta = datetime.timedelta(days=num_days)
nowdays	=	[]
for day in range(1, num_days+1):
	datefor	=	datetime.date(now.year, now.month, day)
	nowdays.append(datefor.strftime("%m,%d,%y"))
	# nowdays.append(datefor.strftime("%d:%b:%Y"))
	# nowdays.append(datetime.date(now.year, now.month, day))
	# print(datetime.date(now.year, now.month, day))

print(nowdays)

# dates = drange(date1, date2, delta)
# s = np.random.rand(len(dates))  # make up some random y values
s = np.random.rand(len(nowdays))  # make up some random y values


fig, ax = plt.subplots()
# plt.plot_date(dates, s)
plt.plot_date(nowdays, s)
ax.xaxis.set_major_locator(loc)
ax.xaxis.set_major_formatter(formatter)
ax.xaxis.set_tick_params(rotation=90, labelsize=60)

plt.show()