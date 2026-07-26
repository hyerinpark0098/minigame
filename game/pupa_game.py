import random
import time

def play():
    while True:
        print('''
번데기 게임 게임방법
===============
1. 컴퓨터가 "번"을 외친 갯수만큼 "데기"를 입력하세요.
2. 제한시간은 20초 입니다! (ex: "번 번 번"-> "데기데기데기")
3. 제한시간동안 입력을 못할 시 시간초과로 게임오버!
   글자 오타가 날 시에도 게임오버가 됩니다.
            ''')

        limit_time = 20.0

        count_bun = random.randint(1,10)
        print(f"컴퓨터: {'번' * count_bun}")

        answer = "데기" * count_bun

        start_time = time.time()

        usper_answer = input("정답: ").strip()
        clean_usper_answer = usper_answer.replace(" ", "")

        end_time = time.time()
        time_taken = end_time - start_time

        if time_taken > limit_time:
            print("시간이 초과되었습니다.")

        if answer == clean_usper_answer:
            print("축하합니다! 성공입니다.")
        else :
            print("틀렸습니다 ㅠㅠ 게임오버!")

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