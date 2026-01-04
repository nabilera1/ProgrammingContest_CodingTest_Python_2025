// 퀴즈 데이터 정의
const questions = [
    {
        q: "PyCharm 공식 홈페이지에서 다운로드할 때 올바른 행동은?",
        options: ["반드시 스크롤을 내려서 숨겨진 파일을 찾는다.", "화면에 보이는 통합 [Download] 버튼을 누른다.", "반드시 결제를 먼저 해야 한다.", "이메일 주소를 입력해야만 다운로드된다."],
        a: 1,
        desc: "최신 버전은 통합되어 있으므로 보이는 버튼을 바로 누르면 됩니다."
    },
    {
        q: "설치 후 '30일 체험판(Trial)'이라는 문구가 떴을 때 올바른 대처법은?",
        options: ["즉시 프로그램을 삭제한다.", "부모님께 결제해달라고 조른다.", "당황하지 않고 그냥 쓴다. (30일 뒤 무료 전환)", "해킹된 것이니 신고한다."],
        a: 2,
        desc: "30일 후 자동으로 무료 버전(Community) 기능으로 전환되므로 걱정 없이 사용하면 됩니다."
    },
    {
        q: "파이참(PyCharm)을 설치하기 전에 '반드시' 먼저 설치해야 하는 것은?",
        options: ["Chrome 브라우저", "카카오톡", "Python 인터프리터 (파이썬 엔진)", "MS 워드"],
        a: 2,
        desc: "자동차에 엔진이 필요하듯, 파이참을 돌리려면 파이썬이 먼저 설치되어 있어야 합니다."
    },
    {
        q: "파이썬 설치 첫 화면에서 꼭 체크해야 하는 옵션은?",
        options: ["Add Python.exe to PATH", "Install Now", "Uninstall", "Documentation"],
        a: 0,
        desc: "PATH에 추가해야 컴퓨터가 파이썬 명령어를 어디서든 인식할 수 있습니다."
    },
    {
        q: "다음 중 사실이 *아닌* 것은?",
        options: ["파이참은 파이썬 전용 도구다.", "파이썬 파일을 저장할 때 확장자는 .py다.", "파이참 설치 시 반드시 신용카드를 등록해야 한다.", "파이참은 코드 자동 완성 기능이 있다."],
        a: 2,
        desc: "파이참 무료 사용(또는 체험판)에는 신용카드 정보가 전혀 필요하지 않습니다."
    }
];

// 화면 로드 후 실행
document.addEventListener('DOMContentLoaded', () => {
    const quizArea = document.getElementById('quiz-area');

    // 퀴즈 문제 생성 및 화면 출력
    questions.forEach((item, idx) => {
        const div = document.createElement('div');
        div.className = 'quiz-item';

        let btns = '';
        item.options.forEach((opt, optIdx) => {
            // HTML 문자열 내에서 함수 호출 시 따옴표 처리에 주의해야 합니다.
            btns += `<button onclick="checkAnswer(${idx}, ${optIdx}, this)">${optIdx+1}. ${opt}</button>`;
        });

        div.innerHTML = `
            <div class="quiz-q">Q${idx+1}. ${item.q}</div>
            <div class="quiz-options">${btns}</div>
            <div class="feedback" id="feed-${idx}"></div>
        `;
        quizArea.appendChild(div);
    });
});

// 정답 확인 함수 (전역 스코프에서 접근 가능해야 하므로 window 객체에 할당하거나 그대로 둡니다)
function checkAnswer(qIdx, userChoice, btnElement) {
    const feedback = document.getElementById(`feed-${qIdx}`);
    const q = questions[qIdx];
    const allBtns = btnElement.parentElement.querySelectorAll('button');

    // 모든 버튼 비활성화
    allBtns.forEach(b => b.disabled = true);

    if (userChoice === q.a) {
        feedback.innerHTML = `⭕ 정답입니다! <br> ${q.desc}`;
        feedback.className = "feedback correct";
        feedback.style.display = "block";
        btnElement.style.background = "#d1e7dd";
        btnElement.style.borderColor = "#0f5132";
    } else {
        feedback.innerHTML = `❌ 틀렸습니다. 정답은 ${q.a+1}번입니다. <br> ${q.desc}`;
        feedback.className = "feedback incorrect";
        feedback.style.display = "block";
        btnElement.style.background = "#f8d7da";
        btnElement.style.borderColor = "#842029";
        // 정답 버튼 강조
        allBtns[q.a].style.background = "#d1e7dd";
        allBtns[q.a].style.borderColor = "#0f5132";
    }
}