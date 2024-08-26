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
    discoButton.style.animation = 'disco 1s infinite';
}

// Function to stop the disco effect
function stopDiscoEffect() {
    const discoButton = document.getElementById('discoButton');
    discoButton.style.animation = 'none';
}
