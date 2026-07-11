let chart;

function analyze() {
    let text = document.getElementById("text").value;

    fetch("/predict", {
        method: "POST",
        headers: {"Content-Type": "application/x-www-form-urlencoded"},
        body: "text=" + text
    })
    .then(res => res.json())
    .then(data => {
        document.getElementById("result").innerText =
            "Emotion: " + data.emotion.toUpperCase();

        document.getElementById("message").innerText = data.message;

        changeBackground(data.emotion);
        showChart(data.scores);
    });
}

function changeBackground(emotion) {
    const colors = {
        happy: "#f6e58d",
        sad: "#74b9ff",
        angry: "#ff7675",
        calm: "#55efc4",
        stress: "#a29bfe"
    };

    document.getElementById("page").style.background =
        colors[emotion] || "#dfe6e9";
}

function showChart(scores) {
    const ctx = document.getElementById("emotionChart").getContext("2d");

    if (chart) chart.destroy();

    chart = new Chart(ctx, {
        type: "bar",
        data: {
            labels: Object.keys(scores),
            datasets: [{
                label: "Emotion Confidence",
                data: Object.values(scores),
            }]
        }
    });
}
function loadHistory() {
    fetch("/history")
        .then(res => res.json())
        .then(data => {
            const times = data.map(item => item.time);
            const emotions = data.map(item => emotionToNumber(item.emotion));

            const ctx = document.getElementById("historyChart").getContext("2d");

            if (window.historyChart) window.historyChart.destroy();

            window.historyChart = new Chart(ctx, {
                type: "line",
                data: {
                    labels: times,
                    datasets: [{
                        label: "Mood Over Time",
                        data: emotions,
                        fill: false,
                        tension: 0.3
                    }]
                }
            });
        });
}
function emotionToNumber(emotion) {
    const map = {
        happy: 5,
        calm: 4,
        stress: 3,
        sad: 2,
        angry: 1
    };
    return map[emotion] || 0;
}
function clearHistory() {
    fetch("/clear_history", { method: "POST" })
        .then(res => res.json())
        .then(() => {
            document.getElementById("quote").innerText = "💬 " + data.quote;

            alert("Mood history cleared!");
            if (window.historyChart) window.historyChart.destroy();
        });
}
function toggleMode() {
    document.body.classList.toggle("dark");
}
