import streamlit as st
from pathlib import Path

# Function to read file content
def read_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()

# Set page configuration
st.set_page_config(page_title="Simple Calculator", layout="wide")

# Load HTML, CSS, and JS content
html_content = read_file('cal.html')
css_content = read_file('cal.css')
js_content = read_file('cal.js')

# Inject CSS and JavaScript into HTML
html_with_css_js = f"""
<!DOCTYPE html>
<html lang="en" dir="ltr">
<head>
  <meta charset="utf-8">
  <title>Simple Calculator with Background Video Changer</title>
  <style>{css_content}</style>
</head>
<body>

<!-- Video Background -->
<video id="backgroundVideo" autoplay muted loop>
  <source src="https://cdn.pixabay.com/video/2021/04/12/70796-538877060_large.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>

<!-- Disco RGB Button -->
<button id="discoButton" onclick="changeBackground()">Click Me!</button>

<!-- Calculator Table -->
{html_content}

<script type="text/javascript">
{js_content}
</script>

</body>
</html>
"""

# Streamlit app
def main():
    st.title("Simple Calculator with Background Video Changer")
    st.markdown(html_with_css_js, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
