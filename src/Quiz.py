# ==========================
# [기능 요구사항] 4. Quiz 클래스
# ==========================
class Quiz:
    # 퀴즈 클래스의 속성들을 초기화, 객체의 
    def __init__(self, question, choices, answer):
        # 속성: 문제
        self.question = question
        # 속성: 선택지
        self.choices = choices
        # 속성: 정답
        self.answer = answer

    # 퀴즈 풀기 기능(play_quiz) 선택 시
    # 한 퀴즈 문제에 대한 화면을 출력해주는 메서드 정의
    def display(self):
        print("\n" + "-" * 40)
        # 한 문제 출력
        print(self.question)  

        # 자료를 순회하면서 각 요소에 번호(인덱스)를 넣어줌
        for i, choice in enumerate(self.choices, start=1):
            # 서식지정자로 선택 번호와 선택지 함께 출력
            print(f"{i}. {choice}")

    # 정답을 확인하는 메서드 정의
    def check_answer(self, user_answer):
        # 문제의 정답과 사용자의 입력값을 대조한 뒤 반환값 전달
        return user_answer == self.answer

    # 퀴즈 객체의 데이터를 딕셔너리 타입으로 변환해주는 메서드 정의
    # 객체 -> 딕셔너리
    def to_dict(self):
        # 키와 쌍으로 이루어진 딕셔너리 타입으로 변환
        # 키: "문제", "선택지", "정답", 값: 실제 데이터값
        return {
            "question": self.question,
            "choices": self.choices,
            "answer": self.answer
        }

    # Quiz 클래스에게 이 딕셔너리로 Quiz 객체 하나 만들어달라고 요청
    @classmethod # 클래스가 사용하는 메서드
    # 딕셔너리 -> 객체
    def from_dict(cls, data):
        # Quiz 클래스 자체
        return cls(
            data["question"],
            data["choices"],
            data["answer"]
        )