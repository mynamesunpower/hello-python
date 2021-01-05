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
print('한 달 전', today - timedelta(days=30))


