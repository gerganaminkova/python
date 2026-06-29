# Instagram Follower Bot 🤖 (Share-A-Naan Edition)

This Python script is an automated bot built using **Selenium WebDriver**. It automatically logs into the "Share-A-Naan" platform (an educational Instagram clone), navigates to a specific target profile, opens their followers list, and automatically follows users while scrolling through the popup.

## Features

* **Automated Login:** Safely logs into the platform and handles unexpected popup notifications/modals.
* **Targeted Navigation:** Automatically searches for and opens a target profile (e.g., `chefsteps`).
* **Smart Following:** Clicks the "Follow" buttons for users in the followers list while explicitly ignoring accounts you are already following.
* **Automated Scrolling:** Injects JavaScript to automatically scroll to the bottom of the followers popup, loading more users dynamically.
* **Error Handling:** Uses `WebDriverWait` and explicit waits to ensure the script doesn't crash due to slow loading times or animations.

## Prerequisites

To run this script, you will need the following installed on your machine:

* **Python 3.x**
* **Google Chrome** (browser)
* Python libraries: `selenium` and `python-dotenv`

## Installation and Setup

**1. Clone or download the project**
Save the project files to your preferred directory.

**2. Install dependencies**
Open your terminal and install the required libraries:
```bash
pip install selenium python-dotenv
```

**3. Set up environment variables**
In the root directory of the project, create a file named exactly `.env`. Add your login credentials inside (without quotes):
```env
EMAIL=your_email@example.com
PASSWORD=your_secret_password
```


