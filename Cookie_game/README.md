# 🍪 Cookie Clicker Bot

A fully automated Python bot for the classic web game [Cookie Clicker](https://ozh.github.io/cookieclicker/), built using **Selenium WebDriver**.

## Features

* **Auto-Clicker:** Rapidly and continuously clicks the "Big Cookie" to generate cookies.
* **Smart Auto-Buyer:** Checks the store every 5 seconds and automatically purchases the most expensive upgrade available, maximizing the cookies-per-second rate.
* **Popup Handling:** Automatically dismisses the initial language selection and cookie consent screens.
* **Time-Limited Execution:** Runs for exactly 5 minutes, prints the final score to the console, and gracefully shuts down.

## Prerequisites
* Python 3.x installed
* Google Chrome browser installed
* Selenium package installed

1. **Clone the repository:**
   ```bash
   git clone <your-repository-url>
   cd <your-repository-folder>