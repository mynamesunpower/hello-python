"""
1. 다음 코드의 실행 결과를 쓰시오.
try:
    for i in range(1, 7):
        result = 7 // i
        print(result)
except ZeroDivisionError:
    print("Not divided by 0")
finally:
    print("종료되었습니다.")
7
3
2
1
1
1
종료되었습니다

2. 다음 코드를 실행했을 때, 가장 마지막에 출력되는 값은? 5
sentence = list("Hello Gachon")
while (len(sentence) + 1):
    try:
        print(sentence.pop(0))
    except Exception as e:
        print(e)
        break

➀ o ➁ n ➂ h ➃ c ➄ pop from empty list

3. 다음 각각의 예외 처리에 적합한 내장 예외(built-in exception)를
순서대로 실행한 결과값이 바르게 짝지어진 것은? 4
(가)
alist = ["a", "1", "c"]
blist = ["b", "2", "d"]
for a, b in enumerate(zip(alist, blist)):
    print(b[a])

(나)
alist = ["a", "1", "c"]
blist = ["b", "2", "d"]
for a, b in enumerate(zip(alist, blist)):
    print(a/int(b[0]))
0, a,b // 1, 1,2 // 2, c,d
➀ NameError, ValueError ➁ IndexError, NameError
➂ ZeroDivisionError, ValueError ➃ IndexError, ValueError
➄ NameError, IndexError
4

4. 다음 중 예외(exception)의 이름과 내용이 잘못 짝지어진 것은? 4
① ZeroDivisionError: 0으로 숫자를 나눌 때
② ValueError: 변환할 수 없는 문자/숫자를 변환할 때
③ IndexError: 리스트의 인덱스 범위를 넘어 갈 때
④ SyntaxError: 조건문이나 변수에 오탈자가 존재할 때
⑤ NameError: 존재하지 않은 변수를 호출할 때


5. 파일의 종류에 대한 설명으로 틀린 것은? 4
① 바이너리 파일은 컴퓨터만 이해할 수 있는 형태인 이진법 형식으로 저장된 파일을 말한다.
② 텍스트 파일의 예로 HTML, 파이썬 코드 파일 등을 들 수 있다.
③ 바이너리 파일은 해당 확장자에 대한 파일을 열 수 있는 프로그램이 필요하다(엑셀, 워드 등).
④ 텍스트 파일의 경우 컴퓨터는 텍스트 파일 형태 그대로 처리가 가능하다.
⑤ 텍스트 파일은 사람도 이해할 수 있는 형태인 문자열 형식으로 저장된 파일을 말한다.


6. 다음 코드의 실행 결과를 쓰시오.

for i in range(3):
    try:
        print(i, 3// i)
    except ZeroDivisionError:
        print("Not divided by 0")
    
Not divided by 0
1 3
2 1

7. 다음 코드는 파이썬에서 ‘i_have_a_dream.txt’ 파일을 읽어오는 코드이다.
같은 기능을 하는 코드를 with 구문과 함께 사용하여 작성하시오.

f = open("i_have_a_dream.txt", "r")
contents = f.read()
print(contents)
f.close()

with open("i_have_a_dream.txt", "r") as f:
    contents = f.read()
    print(contents)

8. 바이너리 파일과 텍스트 파일에 대한 설명으로 틀린 것은? 3
① 텍스트 파일은 사람도 이해할 수 있는 형태로 저장된다.
② 메모장에 저장된 파일, HTML 파일, 파이썬 코드 파일 등은 모두 텍스트 파일이다.
③ 텍스트 파일은 컴퓨터만 이해할 수 있는 형태인 이진(법) 형식으로 저장된 파일이다.
④ 엑셀 파일, 워드 파일 등을 바이너리 파일이라고 부른다.
⑤ 모든 텍스트 파일도 실제는 바이너리 파일로 아스키/유니코드 문자열 집합으로 저장된다.

"""