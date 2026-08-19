class QuizGame:
    # ==========================
    # [기능 요구사항] 2. 메뉴 기능
    # ==========================
    def show_menu(self):

        print("\n" + "-" * 40)
        print("🎯 나만의 퀴즈 게임")
        print("-" * 40)
        print("1. 퀴즈 풀기")
        print("2. 퀴즈 추가")
        print("3. 퀴즈 목록")
        print("4. 최고 점수")
        print("5. 종료")
        print("-" * 40)

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
                # 안전하게 종료
                exit()