from Quiz import Quiz

class QuizGame:
    # json 파일명을 상수 선언(클래스 변수) == 공유자원, 변하지 않는 파일이라고 명시
    FILE_NAME = "state.json"

    # 각자의 독립된 상태를 저장하기 위해 객체로 구현
    # init은 초기 상태를 표현함.
    def __init__(self):
        # 퀴즈 목록
        self.quizzes = []
        # 최고 점수
        self.best_score = 0

        # json 파일 불러오기
        self.load_data()
        
    # ==========================
    # [기능 요구사항] 2. 메뉴 기능
    # ==========================
    def show_menu(self):

        print("\n" + "=" * 40)
        print("🎯 나만의 퀴즈 게임")
        print("-" * 40)
        print("1. 퀴즈 풀기")
        print("2. 퀴즈 추가")
        print("3. 퀴즈 목록")
        print("4. 최고 점수")
        print("5. 종료")
        print("=" * 40)

    # ==========================
    # [기능 요구사항] 3. 숫자 입력(예외처리)
    # ==========================
    def get_number_input(self, message, min_num, max_num):

        # True일 동안 반복
        while True:

            try:
                # 케이스 1) strip 함수로 입력 앞뒤 공백제거 처리
                user_input = input(message).strip()

                # 케이스 2) 빈 입력(Enter)인 경우
                if user_input == "":
                    # 안내 메시지 출력
                    print("입력이 비어있습니다.")
                    # 재입력 유도
                    continue

                # 케이스 3) 허용범위 밖 숫자(0, 9)인 경우
                # 사용자의 입력값을 정수형으로 형변환
                value = int(user_input)

                # 최솟값 이상 최댓값 이하의 value 값이면 사용자 입력값을 반환
                if min_num <= value <= max_num:
                    return value

                # 안내 메시지 출력
                print(
                    f"{min_num} ~ {max_num} 사이의 숫자를 입력해주세요."
                )

            # 케이스 4) 숫자 변환 처리 실패한 경우(문자열 abc)
            except ValueError:
                # 안내 메시지 출력
                print("숫자를 입력하세요.")

            # 프로그램 실행 중 Ctrl+C(KeyboardInterrupt) 입력 or 
            # 입력스트림 종료(EOFError) 발생해도 비정상종료하지 않도록 처리
            except (KeyboardInterrupt, EOFError):
                # 안내 메시지 출력
                print("\n프로그램을 종료합니다.")
                # 가능한 범위에서 저장
                self.save_data()
                # 프로그램 종료
                exit()

    # ==========================
    # [기능 요구사항] 5. 기본 퀴즈 데이터
    # ==========================
    def create_default_quizzes(self):
        return [
            Quiz(
                "객체지향 설계 원칙 중 서브타입(상속받은 하위 클래스)은\n어디에서나 자신의 기반타입(상위 클래스)으로\n교체할 수 있어야 함을 의미하는 원칙은?\n",
                ["ISP(Interface Segregation Principle)", "DIP(Dependency Inversion Principle)", "LSP(Liskov Substitution Principle)", "SRP(Single Responsibiliy Principle)"],
                3
            ),
            Quiz(
                "객체지향 소프트웨어 공학에서 하나의 이상의\n유사한 객체들을 묶어서 하나의 공통된 특성을 표현한 것은?\n",
                ["트랜잭션", "클래스", "시퀀스", "서브루틴"],
                2
            ),
            Quiz(
                "UI 설계 원칙 중 누구나 쉽게 이해하고 사용할 수 있어야 한다는 원칙은?\n",
                ["희소성", "유연성", "직관성", "멀티운용성"],
                3
            ),
            Quiz(
                "대표적으로 DOS 및 UNIX 등의 운영체제에서 조작을 위해 사용하던 것으로,\n 정해진 명령 문자열을 입력하여 시스템을 조작하는 사용자 인터페이스(User Interface)는?\n",
                ["GUI", "CLI", "CUI", "MUI"],
                2
            ),
            Quiz(
                "자료 사전에서 자료의 생략을 의미하는 기호는?\n", 
                ["{}", "**", "=", "( )"],
                4
            ),
        ]

    # ==========================
    # [기능 요구사항] 6. 퀴즈 풀기
    # ==========================
    def play_quiz(self):

        # 퀴즈가 없는 경우 처리
        if len(self.quizzes) == 0:
            print("퀴즈가 없습니다!")
            return

        # 점수 초기 상태 0으로 초기화
        score = 0

        # 총 문제 개수 출력
        print(f"\n총 {len(self.quizzes)}문제입니다!")

        # 현재 문제 번호(index), 해당되는 문제(quiz)를 순회하면서 문제번호와 문제를 함께 출력
        for index, quiz in enumerate(self.quizzes, start=1):
            # 문제 번호 출력
            print(f"\n문제 {index}")
            # 한 문제를 출력해주는 메서드로 해당되는 문제 출력
            quiz.display()
            # 선택지 1 ~ 4까지 입력받는 메서드 호출 
            answer = self.get_number_input(
                "\n정답: ",
                1,
                4
            )

            # 사용자가 입력한 답이 맞는지 정답 확인 메서드로 확인
            if quiz.check_answer(answer):
                # 정답이면 다음 명령어 출력
                print("\n정답입니다!")
                # 점수를 1 증가시킴(누적)
                score += 1
            # 아니라면 다음 명령어 출력
            else:
                print(
                    f"오답입니다! (정답: {quiz.answer})"
                )
        # 모든 문제를 풀면 결과 표시
        print("\n[결과]")
        print(
            # 총 점수를 퀴즈목록으로 나눠서 출력
            f"{score}/{len(self.quizzes)}"
        )

        # 총 점수가 최고 점수보다 클 경우
        if score > self.best_score:
            # 현재 총 점수를 최고 점수에 저장(갱신)
            self.best_score = score
            print("축하합니다! 최고 점수를 갱신했습니다!")
            # 게임이 끝나면 해당 내용을 저장-파일 저장하는 메서드 호출
            self.save_data()

    # ==========================
    # [기능 요구사항] 7. 퀴즈 추가
    # ==========================
    def add_quiz(self):

        print("\n퀴즈 추가\n")

        question = input("문제: ").strip()

        choices = []

        for i in range(4):
            choice = input(
                f"선택지 {i+1}: "
            ).strip()

            choices.append(choice)

        answer = self.get_number_input(
            "정답 번호: ",
            1,
            4
        )

        quiz = Quiz(
            question,
            choices,
            answer
        )

        self.quizzes.append(quiz)

        self.save_data()

        print("새로운 추가 완료")