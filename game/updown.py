import random

def play():
    while True :
        print('''
UP!DOWN! 게임방법
==============
1. 컴퓨터가 1~50까지의 숫자 중 하나를 고릅니다.
2. user가 숫자를 골라 입력합니다.
3. 컴퓨터의 예상 숫자보다 낮으면 UP! 컴퓨터의 예상 숫자보다 높으면 DOWN!
4. 예상 숫자를 맞추면 게임은 종료됩니다.
        ''')
        computer = random.randint(0, 50)
        print()
        print("컴퓨터가 숫자를 골랐습니다. 게임을 시작하겠습니다.")

        while True:
            user_choice = int(input("숫자를 입력해주세요:"))

            def user_vs_computer():
                if user_choice < computer:
                    return "UP"
                elif user_choice > computer:
                    return "DOWN"
                elif user_choice == computer:
                    return "WINER"

            result = user_vs_computer()

            if result == "UP":
                print("UP")
            elif result == "DOWN":
                print("DOWN")
            elif result == "WINER":
                print("축하합니다. 정답입니다.")
                break

        if result == "WINER":
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