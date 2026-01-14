class LoginSystem:
    MAX_ATTEMPTS = 5

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.attempts = 0
        self.locked = False

    def login(self, input_pw):
        if self.locked:
            return "계정이 잠겼습니다."
        if input_pw == self.password:
            self.attempts = 0
            return f"{self.username}님! 로그인 성공~"
        else:  # 비번이 틀렸다면
            self.attempts += 1
            if self.attempts >= LoginSystem.MAX_ATTEMPTS:
                self.locked = True
                return f"비밀번호 {LoginSystem.MAX_ATTEMPTS}회 오류! 계정 잠김."
            else:
                remain = LoginSystem.MAX_ATTEMPTS - self.attempts
                return f"비밀번호 오류! 남은 기회 : {remain}회 입니다."
stu1201 = LoginSystem("Kwak", "1111")
print(stu1201.login("Kwak"))