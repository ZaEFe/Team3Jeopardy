function revealQuestion(questionId) {
    fetch(`/set_current_question/${questionId}/`)
    .then(response => response.json())
    .then(data => {
        document.getElementById("question-display").innerText = data.question;
    });
}