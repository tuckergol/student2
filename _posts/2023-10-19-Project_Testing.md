---
toc: true
comments: false
layout: default
title: Project Testing
type: hacks
courses: { compsci: {week: 9} }
---

<html>

<head>
    <title>Geoestimator</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            height: 100vh;
            margin: 0;
        }

        h1 {
            color: #FFFFFF;
        }

        #word-box {
            display: flex;
            justify-content: center;
            align-items: center;
            height: 200px;
            width: 400px;
            border: 2px solid #FFFFFF;
            border-radius: 10px;
            margin-top: 20px;
            font-size: 40px;
            font-weight: bold;
        }

        #input-box {
            margin-top: 20px;
        }

        #result {
            margin-top: 20px;
            font-weight: bold;
        }

        button {
            margin-top: 20px;
            padding: 10px 20px;
            background-color: #4CAF50;
            color: white;
            border: none;
            border-radius: 4px;
            cursor: pointer;
        }

        button:hover {
            background-color: #45a049;
        }

        #timer {
            position: absolute;
            top: 0;
            right: 4px;
            font-size: 20px;
        }
    </style>
</head>

<body>
    <h1>Geoestimator</h1>
    <div id="timer">00:00:00.000</div>
    <div id="word-box"></div>
    <div id="compass"></div>
    <div id="input-box">
        <input type="text" id="user-input" placeholder="Enter your guess" />
        <button onclick="checkGuess()">Check</button>
        <button onclick="startRound()">New Round</button>
    </div>
    <div id="result"></div>

    <script>
        const countries = [
            "United States",
            "United Kingdom",
            "Canada",
            "Australia",
            "France",
            "Germany",
            "Italy",
            "Japan",
            "China",
            "India",
            "Russia",
            "Brazil",
            "Mexico",
            "Spain",
            "South Africa",
            "Argentina",
            "Egypt",
            "Turkey",
            "Greece",
            "Netherlands",
            "Switzerland",
            "South Korea",
            "Sweden",
            "Norway",
            "Denmark",
            "Ireland",
            "New Zealand",
            "Singapore",
            "Malaysia",
            "Thailand",
            "Vietnam",
            "Indonesia",
            "Philippines",
            "Saudi Arabia",
            "Qatar",
            "Israel",
            "Jordan",
            "Lebanon"
        ];

        let currentCountry, currentLat, currentLng, attempts, lastDistance, lastDirection;
        let startTime, timerInterval;
        let seconds = 0;
        let minutes = 0;
        let hours = 0;
        let milliseconds = 0;

        function startRound() {
            currentCountry = countries[Math.floor(Math.random() * countries.length)];
            document.getElementById('word-box').innerText = currentCountry;
            attempts = 0;
            lastDistance = 0;
            lastDirection = "";
            document.getElementById('result').innerText = ""; // Clear the result text
            document.getElementById('user-input').value = ""; // Clear the input box

            resetTimer();
        }

        function checkGuess() {
            const userInput = document.getElementById('user-input').value.trim();
            if (userInput.toLowerCase() === currentCountry.toLowerCase()) {
                document.getElementById('result').innerText = `Congratulations! You guessed it right in ${attempts + 1} attempts.`;
                stopTimer();
            } else {
                attempts++;
                const lengthDifference = currentCountry.length - userInput.length;
                if (lengthDifference > 0) {
                    document.getElementById('result').innerText = `Try again. You are ${lengthDifference} letters too short.`;
                } else {
                    document.getElementById('result').innerText = `Try again. You are ${Math.abs(lengthDifference)} letters too long.`;
                }
            }
        }

        function resetTimer() {
            startTime = new Date().getTime();
            clearInterval(timerInterval);
            timerInterval = setInterval(updateTimer, 10); // Update every 10 milliseconds
        }

        function stopTimer() {
            clearInterval(timerInterval);
        }

        function updateTimer() {
            const currentTime = new Date().getTime();
            let elapsedTime = currentTime - startTime;

            hours = Math.floor(elapsedTime / 3600000);
            elapsedTime -= hours * 3600000;

            minutes = Math.floor(elapsedTime / 60000);
            elapsedTime -= minutes * 60000;

            seconds = Math.floor(elapsedTime / 1000);
            milliseconds = elapsedTime - (seconds * 1000);

            updateTimerDisplay();
        }

        function updateTimerDisplay() {
            const timerElement = document.getElementById('timer');
            timerElement.textContent = `${pad(hours)}:${pad(minutes)}:${pad(seconds)}.${padMilliseconds(milliseconds)}`;
        }

        function pad(num) {
            return num.toString().padStart(2, '0');
        }

        function padMilliseconds(num) {
            return num.toString().padStart(3, '0');
        }

        startRound();
    </script>
</body>

</html>