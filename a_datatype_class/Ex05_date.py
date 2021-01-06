#
# import datetime
# today = datetime.date.today();
# print('today is ', today)


from datetime import date, timedelta
today = date.today()
print('today is ', today)
print('년도 ', today.year)
print('월: ', today.month)
print('일: ', today.day)

# 날짜 계산 -> timedelta
# from datetime import timedelta
print('어제', today + timedelta(days=-1))
print('어제', today - timedelta(days=1))

# 일주일 후
print('일주일 후', today + timedelta(weeks=1))

# 10일 전
print('10일 전', today - timedelta(days=10))

# 한 달 전
from dateutil.relativedelta import relativedelta
aftermonth = today - relativedelta(months=1)
print('한 달 전', aftermonth)


# 날짜 형식 출력 (strftime())
from datetime import datetime
today = datetime.today()
print(today)
print(today.strftime("%Y-%m-%d >> %H:%M:%S"))

# 문자열을 날짜형으로 변환 ( *** strptime() )
day = '2021-01-08 12:50'
mydate = datetime.strptime(day, '%Y-%m-%d %H:%M')
print(mydate)
print(type(mydate))