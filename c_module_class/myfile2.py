import mypackage.mymodule
today = mypackage.mymodule.get_weather()
print('오늘의 날씨:', today)
print('오늘은', mypackage.mymodule.get_date() + '요일입니다')

from mypackage.mymodule import get_weather, get_date
print('오늘의 날씨:', get_weather())
print('오늘은', get_date() + '요일입니다')
