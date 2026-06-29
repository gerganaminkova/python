# Internet Speed Twitter Bot 🚀

This Python script uses **Selenium WebDriver** to automate the process of testing your internet connection speed via [Speedtest.net](https://www.speedtest.net/) and automatically posts a message (tweet) with the results on an educational platform (a Twitter/X clone) if the speeds don't match what you pay for.

##  How it works

1. **Opens Chrome** and navigates to Speedtest.net.
2. **Accepts cookies** automatically.
3. **Starts the test** and waits patiently for it to finish (up to 2 minutes).
4. **Extracts the data** for Download and Upload speeds.
5. **Logs into your account** on the `app.100daysofpython.dev/services/y/login` platform by automatically filling in your email and password.
6. **Posts a complaint**, containing your actual results compared to what you are paying for.


## Installation and Setup

**1. Clone or download the project** to a convenient folder on your machine.

**2. Install the required dependencies** via the terminal:
```bash
pip install selenium python-dotenv