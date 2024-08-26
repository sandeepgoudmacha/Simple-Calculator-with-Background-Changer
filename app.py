import streamlit as st

# Define the HTML and CSS for the calculator
html_content = """
<!DOCTYPE html>
<html lang="en" dir="ltr">
<head>
  <meta charset="utf-8">
  <title>Simple Calculator with Background Changer</title>
  <style>
    body {
        font-family: 'Arial', sans-serif;
        display: flex;
        justify-content: center;
        align-items: center;
        height: 100vh;
        margin: 0;
        background-image: url('https://images.hdqwalls.com/wallpapers/peyto-lake-canada-mountains-4k-tj.jpg'); /* Default background image */
        background-size: cover;
        background-position: center;
        color: #333;
        transition: background-color 0.3s ease, color 0.3s ease;
    }

    .calculator {
        border: 1px solid #ccc;
        padding: 20px;
        background-color: #fff;
        border-radius: 10px;
        box-shadow: 0px 5px 10px rgba(0, 0, 0, 0.1);
        transition: background-color 0.3s ease, border-color 0.3s ease;
    }

    .display-box {
        width: 100%;
        height: 50px;
        background-color: #eaeaea;
        border: none;
        border-radius: 5px;
        text-align: left;
        padding: 10px;
        font-size: 24px;
        color: #333;
        transition: background-color 0.3s ease, color 0.3s ease;
    }

    input[type="button"] {
        width: 60px;
        height: 60px;
        margin: 5px;
        font-size: 22px;
        background-color: #f1f1f1;
        border: 1px solid #ccc;
        border-radius: 5px;
        color: #333;
        cursor: pointer;
        transition: background-color 0.2s ease, border-color 0.2s ease;
    }

    input[type="button"]:hover {
        background-color: #ddd;
    }

    #btn {
        background-color: #f76c6c;
        color: white;
    }

    #btn:hover {
        background-color: #e55a5a;
    }

    #discoButton {
        position: absolute;
        top: 20px;
        right: 20px;
        padding: 10px 20px;
        font-size: 16px;
        background: linear-gradient(45deg,#ff0000, #ff7f00, #00ff00, #0000ff);
        color: white;
        border: none;
        border-radius: 50%;
        cursor: pointer;
        transition: background-color 0.3s ease;
    }

    #discoButton:hover {
        opacity: 0.8;
    }

    body.dark-mode {
        background-color: #333;
        color: #fff;
    }

    .calculator.dark-mode {
        background-color: #444;
        border-color: #666;
    }

    .display-box.dark-mode {
        background-color: #555;
        color: #fff;
    }

    input[type="button"].dark-mode {
        background-color: #666;
        border-color: #888;
        color: #fff;
    }

    input[type="button"].dark-mode:hover {
        background-color: #777;
    }

    #btn.dark-mode {
        background-color: #d9534f;
    }

    #btn.dark-mode:hover {
        background-color: #c9302c;
    }

    @keyframes disco {
        0% { background: red; }
        16% { background: orange; }
        33% { background: yellow; }
        50% { background: green; }
        66% { background: blue; }
        83% { background: indigo; }
        100% { background: violet; }
    }
  </style>
</head>
<body>
  <!-- Disco RGB Button -->
  <button id="discoButton" onclick="changeBackground()">Click Me!</button>

  <table class="calculator">
    <tr>
      <td colspan="3"> <input class="display-box" type="text" id="result" disabled /> </td>
      <td> <input type="button" value="C" onclick="clearScreen()" id="btn" /> </td>
    </tr>
    <tr>
      <td> <input type="button" value="1" onclick="display('1')" /> </td>
      <td> <input type="button" value="2" onclick="display('2')" /> </td>
      <td> <input type="button" value="3" onclick="display('3')" /> </td>
      <td> <input type="button" value="/" onclick="display('/')" /> </td>
    </tr>
    <tr>
      <td> <input type="button" value="4" onclick="display('4')" /> </td>
      <td> <input type="button" value="5" onclick="display('5')" /> </td>
      <td> <input type="button" value="6" onclick="display('6')" /> </td>
      <td> <input type="button" value="-" onclick="display('-')" /> </td>
    </tr>
    <tr>
      <td> <input type="button" value="7" onclick="display('7')" /> </td>
      <td> <input type="button" value="8" onclick="display('8')" /> </td>
      <td> <input type="button" value="9" onclick="display('9')" /> </td>
      <td> <input type="button" value="+" onclick="display('+')" /> </td>
    </tr>
    <tr>
      <td> <input type="button" value="." onclick="display('.')" /> </td>
      <td> <input type="button" value="0" onclick="display('0')" /> </td>
      <td> <input type="button" value="=" onclick="calculate()" id="btn" /> </td>
      <td> <input type="button" value="*" onclick="display('*')" /> </td>
    </tr>
  </table>

  <script type="text/javascript">
    // Array of background images
    const backgrounds = [
        'https://cdn.wallpapersafari.com/15/2/qSOWl9.jpg',
        'https://wallpaperwaifu.com/wp-content/uploads/2019/09/mountain-with-stars-nature-thumb.jpg',
        'https://cdn.wallpapersafari.com/85/83/wZncxe.jpg',
        'https://images.hdqwalls.com/wallpapers/peyto-lake-canada-mountains-4k-tj.jpg'
    ];

    let currentBackgroundIndex = 0;

    // Function to change background image
    function changeBackground() {
        // Toggle dark mode
        toggleDarkMode();

        // Change background image
        currentBackgroundIndex = (currentBackgroundIndex + 1) % backgrounds.length;
        document.body.style.backgroundImage = `url(${backgrounds[currentBackgroundIndex]})`;

        // Optionally start or stop disco effect
        if (document.body.classList.contains('dark-mode')) {
            startDiscoEffect();
        } else {
            stopDiscoEffect();
        }
    }

    // Function to clear the display
    function clearScreen() {
        document.getElementById("result").value = "";
    }

    // Function to display values
    function display(value) {
        document.getElementById("result").value += value;
    }

    // Function to evaluate the expression and display the result
    function calculate() {
        try {
            const expression = document.getElementById("result").value;
            const result = eval(expression);
            document.getElementById("result").value = result;
        } catch (error) {
            alert("Invalid Expression");
            clearScreen();
        }
    }

    // Event listener to trigger calculation when Enter key is pressed
    document.getElementById("result").addEventListener("keyup", function(event) {
        if (event.key === "Enter") {
            calculate();
        }
    });

    // Function to toggle between dark mode and light mode
    function toggleDarkMode() {
        const body = document.body;
        const calculator = document.querySelector('.calculator');
        const displayBox = document.querySelector('.display-box');
        const buttons = document.querySelectorAll('input[type="button"]');
        const discoButton = document.getElementById('discoButton');

        body.classList.toggle('dark-mode');
        calculator.classList.toggle('dark-mode');
        displayBox.classList.toggle('dark-mode');
        buttons.forEach(button => button.classList.toggle('dark-mode'));

        // Start or stop the disco effect
        if (body.classList.contains('dark-mode')) {
            startDiscoEffect();
        } else {
            stopDiscoEffect();
        }
    }

    // Function to start the disco effect
    function startDiscoEffect() {
        const discoButton = document.getElementById('discoButton');
        discoButton.style.animation = 'disco 
