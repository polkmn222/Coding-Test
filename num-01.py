"""
아래 링크의 Json 파일에 정의되어 있는 Bread 객체를 디자인 패턴 (팩토리 메소드)을
이용하여 생성하고, 이 객체들을 리스트에 삽입합니다. 리스트 내 Bread 객체를 순환하며 각
Bread 속성을 출력 하십시오.
- Input Json 링크
https://drive.google.com/open?id=1CPt0YMDN6mOZR9NlwDZ-NdgCOZSGNiiM
- Output
https://drive.google.com/open?id=13fe3eJQ4YdJ2wg0Nxyq_Uar7imCF5Pnd
"""

# cream = {"flour" : 100, "water" : 100, "cream" : 200}
cream = []
cream.append("flour: 100")
cream.append("water: 100")
cream.append("cream: 100")

sugar = []
sugar.append("flour: 100") 
sugar.append("water: 50")
sugar.append("sugar: 200")

butter = []
butter.append("flour: 100")
butter.append("water: 100")
butter.append("butter: 50")

# while True:
a = input()
if a == "cream":
    print("breadType: cream")
    print("recepe")
    for i in cream:
        print(i)
elif a == "sugar":
    print("breadType: sugar")
    print("recepe")
    for i in sugar:
        print(i)
elif a == "butter":
    print("breadType: butter")
    print("recepe")
    for i in butter:
        print(i)

