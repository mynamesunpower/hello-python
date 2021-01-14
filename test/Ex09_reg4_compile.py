'''
    # compile
     - 동일한 정규표현식을 매번 다시 쓰기 번거로움을 해결
     - compile로 해당표현식을 re.RegexObject 객체로 저장하여 사용가능
'''

import re


#----------------------------------------
webs = ['http://www.test.co.kr',
        'https://www.test1.com',
        'http://www.test.com',
        'ftp://www.test.com',
        'http:://www.test.com',
       'htp://www.test.com',
       'http://www.google.com',
       'https://www.homepage.com.']

pattern = re.compile(r'[\w-]+@[\w.]+')  # 문자와 -이 섞여서 올 수 있고 여러개도 올수있다
result = pattern.search('test@gmail.com hahahaha  good')
if result:
    print(result.group())

url_pattern = re.compile(r'https?://[\w.]+\w$')  # d? d가 0개이거나 1개이거나
result = list(map(lambda w: url_pattern.search(w), webs))
for url in result:
    if url:
        print(url.group())


def email_check(email):
    pattern = re.compile(r'[^\W-]+@[\w]+\.[\w]+$')
    if pattern.search(email):
        print('성공')

email_check('kim@encore.com')       # 올바른 이메일
email_check('kim@encore')           # 잘못된 이메일 ( . 하나 없어서 )
email_check('k!m@encore.com')      # 잘못된 이메일 ( 특수문자 ! 안됨 )
email_check('!km@encore.com')      # 잘못된 이메일 ( 특수문자 ! 안됨 )