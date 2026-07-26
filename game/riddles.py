import random

quiz_data = [
    ("미소의 반댓말은?","당기소"),
    ("논리적인 사람이 총을 쏘면?","타당타당"),
    ("누룽지를 영어로 하면?","바비브라운"),
    ("소녀시대는 소원을 몇개 들어줄까요?","4개"),
    ("왕이 넘어지면?","킹콩"),
    ("가장 뜨거운 과일은?","천도복숭아"),
    ("바나나가 웃으면?","바나나킥"),
    ("엄마가 동생편만 드는 세상은?","형편없는세상"),
    ("아몬드가 죽으면?","다이아몬드"),
    ("전주비빔밥보다 신선한 비빔밥은?","이번주비빔밥"),
    ("부처님이 잘생겼다를 4글자로 하면?","부처핸썸"),
    ("개가 사람을 가르치면?","개인지도")
]

def play():
    while True:

        print('''
넌센스 퀴즈 게임방법
================
1. 질문이 나오면 답을 입력합니다.
2. 정답에 띄어쓰기는 없습니다.
3. 정답을 맞추면 종료! 정답을 못 맞출 시 다시 정답을 입력하게 됩니다.
4. "no" 입력할 시 정답을 알려주며 게임이 종료됩니다.
        ''')

        print("넌센스퀴즈를 시작합니다.")

        data = random.choice(quiz_data)

        question = data[0]
        answer = data[1]

        print(question)

        while True:
            user = input("정답:")

            def determin_winner():
                if user == answer:
                    return "정답"
                else :
                    return "오답"

            if determin_winner() == "정답" :
                print("정답입니다.")
                break
            else :
                print("오답입니다.")
                user_want_answer = input("정답을 알려드릴까요?(yes/no):")
                if user_want_answer == "yes":
                    print(answer)
                    break
                elif user_want_answer == "no" :
                    continue
                else :
                    print("잘못된 입력값입니다.\"yes\",\"no\"중 입력해주십시오.")

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