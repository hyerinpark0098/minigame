import random

rps = ["가위", "바위", "보"]
choice = ["yes", "y", "no", "n"]

def play ():
    while True:

        print('''
가위, 바위, 보 게임을 시작합니다.
=========================
1.가위, 바위, 보 중에서 선택해서 입력합니다.
  입략방법 : ex) 가위, 바위, 보
2.비기면 \"다시시작\", 승패가 나면 \"종료\"가 됩니다.
3.게임 종료시, 다시 시작여부에 \"yes or y\" 가 입력되면 다시 시작
  종료 시 \"no or n\"를 입력하면 게임이 종료됩니다.
    ''')

        while True:
            user = input("가위, 바위, 보 중에서 어떤걸 선택하시겠습니까?")

            if user not in rps:
                print("잘못된 입력값입니다.\"가위\", \"바위\", \"보\" 중에서 정확히 입력하세요.")

            else:
                break

        computer = random.choice(rps)

        def determine_winer():
            if user == computer:
                return "무승부"

            winer_case = {
                "가위": "보",
                "바위": "가위",
                "보": "바위"
            }

            if winer_case[user] == computer:
                return "승리"
            else:
                return "패배"

        result = determine_winer()

        print(f"user: {user}, computer: {computer}")
        if result == "승리" :
            print("축하합니다! 이겼습니다.")
        elif result == "패배" :
            print("아쉽네요. 컴퓨터가 이겼습니다 ㅠㅠ")
        else :
            print("비겼습니다. 게임을 다시 시작합니다")
            continue

        if result == "승리" or "패배":
             while True:
                user_again = input("게임을 다시 시작하겠습니까?[yes or no]")

                if user_again in ["yes", "y"]:
                    play_aging = True
                    break
                elif user_again == "no" or user_again == "n":
                    play_aging = False
                    break
                else :
                    print("잘못된 입력값입니다.\"yes\",\"y\",\"no\",\"n\"중 입력해주십시오.")

        if play_aging:
            continue
        else:
            print("게임을 종료합니다. 이용해주셔서 감사합니다!")
            break