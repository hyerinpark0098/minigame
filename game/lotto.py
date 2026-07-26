import random
from itertools import count

def play():
    while True:
        print('''
Lotto게임을 시작합니다.
===================
1. 1~40까지의 숫자 중 6개의 숫자를 한개씩 입력합니다.
2. 결과값이 나오고 게임이 종료됩니다.
    6자리 일치 = 1등
    5자리 일치 = 2등
    4자리 일치 = 3등
    3자리 일치 = 4등 
    그 외 낙첨
        ''')

        lotto = []

        while len(lotto) < 6:
            num = random.randint(1,40)
            if num not in lotto:
                lotto.append(num)

        user_lotto = []

        while len(user_lotto) < 6:
            user_choice = int(input("1부터 40까지의 숫자 중 선택해주세요. *중복불가* : "))
            if user_choice not in user_lotto:
                user_lotto.append(user_choice)

        mach = set(lotto) & set(user_lotto)
        count = len(mach)

        def lucky():
            if count == 0 or 1 or 2:
                return "낙첨"
            elif count == 3:
                return "4등"
            elif count == 4:
                return "3등"
            elif count == 5:
                return "2등"
            elif count == 6:
                return "1등"

        result = lucky()

        if result == "1등":
            print(lotto)
            print("축하합니다. 1등 당첨입니다.")
        elif result == "2등":
            print(lotto)
            print(f"2등, {count}개가 일치합니다.")
        elif result == "3등":
            print(lotto)
            print(f"3등, {count}개가 일치합니다.")
        elif result == "4등":
            print(lotto)
            print(f"4등, {count}개가 일치합니다.")
        elif result == "낙첨":
            print(lotto)
            print(f"낙첨입니다.")

        while True:
            user_again = input("게임을 다시 시작하겠습니까?[yes or no]")

            if user_again in ["yes", "y"]:
                play_aging = True
                break
            elif user_again == "no" or user_again == "n":
                play_aging = False
                break
            else:
                print("잘못된 입력값입니다.\"yes\",\"y\",\"no\",\"n\"중 입력해주십시오.")

        if play_aging:
            continue
        else:
            print("게임을 종료합니다. 이용해주셔서 감사합니다!")
            break