# Ex03_xml.py

import xml.etree.ElementTree as et

# [ 참고 ] 위치 인자와 키워드 인자를 구별해야 합니다.
# 키워드=인자 로 지정하려면 키워드 인자임. 위치 인자가 아닙니다.
tree = et.ElementTree(file='./data/temp.xml')
root = tree.getroot()

# 단군, 시조
print('root:', root)
print('root tag:', root.tag)

# 자식 뽑으러 가자
for child in root:
    # print(child.tag)
    print([grandchild.text for grandchild in child])