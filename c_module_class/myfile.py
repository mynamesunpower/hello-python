# 1 모듈 전체를 참고할 때
from c_module_class.mypackage import mymodule, mymodule as mm

print('오늘의 날씨는', mymodule.get_weather(), '입니다.')
print('오늘은 ', mymodule.get_date(), '요일입니다.')


# 2 별칭 부여도 가능하다
print('오늘의 날씨는', mm.get_weather(), '입니다.')
print('오늘은 ', mm.get_date(), '요일입니다.')


# 3 필요한 부분만 임포트
from c_module_class.mypackage.mymodule import get_weather, get_date
print('오늘의 날씨는', get_weather(), '입니다.')
print('오늘은 ', get_date(), '요일입니다.')


# 4 필요한 부분만 별칭 부여 가능
from c_module_class.mypackage.mymodule import get_weather as g, get_date as f
print('오늘의 날씨는', g(), '입니다.')
print('오늘은 ', f(), '요일입니다.')

from c_module_class.mypackage.exam.exmodule import sum, sum2
print(sum(4, 5))
print(sum('a', 5))

print(sum2(4, 9))