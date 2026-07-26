from game.rps  import play as play_rps
from game.updown import play as play_updown
from game.lotto import play as play_lotto
from game.pupa_game import play as play_pupa
from game.riddles import play as play_riddles

while True:
    print('''
오락실에 오신것을 환영합니다
=====================
1. 실행할 게임을 선택하세요.
    1) 가위, 바위, 보 게임
    2) UP!DOWN 게임
    3) lotto 게임
    4) 넌센스 퀴즈 게임
    5) 번데기 게임
    0) 종료
2. 한 게임이 끝나면 게임진행 여부가 나옵니다.
3. 종료를 원할 시 0을 누르시면 됩니다.
    ''')

    choice = input("실행할 게임 번호를 선택하세요: ").strip()

    if choice == "1":
        play_rps()
    elif choice == "2":
        play_updown()
    elif choice == "3":
        play_lotto()
    elif choice == "4":
        play_riddles()
    elif choice == "5":
        play_pupa()
    elif choice == "0":
        print("게임센터를 종료합니다!")
        break
    else :
        print("잘못입력하셨습니다. 다시 입력하시길 바랍니다.")
        continue
    print()

    while True:
        again_game = input("다른 게임을 선택하시겠습니까?\"yes/no\": ")
        if again_game == "yes":
            print("게임을 다시 시작합니다.")
            break

        elif again_game == "no":
            print("이용해주셔서 감사합니다. 오락실을 종료합니다!")
            break

        else :
            print("잘못입력하셨습니다. 다시 입력하시길 바랍니다.")

    if again_game == "no":
        break
