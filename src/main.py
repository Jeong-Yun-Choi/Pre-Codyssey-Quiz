# main.py

# QuizGame.py에서 QuizGame 클래스를 가져온다.
# main.py에서 QuizGame 객체를 생성하여 퀴즈 게임을 실행하기 위해 사용한다.
from QuizGame import QuizGame


# 프로그램의 전체 실행 과정을 담당하는 main 함수를 정의한다.
def main():

    # 프로그램 실행 중 예상하지 못한 키보드 인터럽트(Ctrl+C)가 발생할 수 있으므로
    # try 블록 안에서 게임을 실행한다.
    try:

        # QuizGame 클래스의 객체를 생성한다.
        # 이때 QuizGame의 __init__()이 실행되고
        # 퀴즈 목록과 최고 점수 등의 초기화 및 데이터 불러오기가 이루어진다.
        game = QuizGame()

        # 생성된 QuizGame 객체의 run() 메서드를 호출한다.
        # run()에서 메뉴를 보여주고 사용자의 선택에 따라
        # 퀴즈 풀기, 퀴즈 추가, 퀴즈 목록, 점수 확인 등의 기능을 실행한다.
        game.run()

    # 사용자가 프로그램 실행 중 Ctrl+C를 누르면 KeyboardInterrupt가 발생한다.
    # 이 예외를 처리하여 오류 메시지 대신 프로그램 종료 안내를 출력한다.
    except KeyboardInterrupt:

        # 줄을 바꾼 후 프로그램이 종료되었다는 메시지를 출력한다.
        print("\n프로그램 종료")


# 이 파일(main.py)을 직접 실행했을 때만 main() 함수를 호출한다.
# 다른 파일에서 main.py를 import하는 경우에는 main()이 자동으로 실행되지 않는다.
if __name__ == "__main__":

    # 위에서 정의한 main() 함수를 호출하여 프로그램을 시작한다.
    main()