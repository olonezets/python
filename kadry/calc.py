from datetime import date
import pandas as pd

date1 = date(
    int(input('enter_a_first_year:')),
    int(input('enter_a_first_month:')),
    int(input('enter_a_first_day:'))
    )

date2 = date(
    int(input('enter_a_last_year:')),
    int(input('enter_a_last_month:')),
    int(input('enter_a_last_day:'))
    )

dt1 = pd.date_range(date1, date2)
dt2 = dt1[(dt1.day != 29) | (dt1.month != 2)]

print (len(dt1), 'oll_days_betwen_date')
print (len(dt1) - len(dt2), 'leap_days_betwen_date')
print(len(dt2), 'days_betwen_date_without_daysleap')

x0 = len(dt2) * 0.082191781
x1 = round(x0)

print(x1, 'days_otpusk_for_date_without_daysleap')
