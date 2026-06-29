# 🐶 Tindog Auto-Swiper Bot

A Python automation script built with **Selenium WebDriver** that automates the process of logging in and swiping right on [Tindog](https://app.100daysofpython.dev/services/tindog/). 

## Features

* **Automated Facebark Login:** Seamlessly handles multi-window navigation to log into Tindog via the Facebark authentication popup.
* **Popup Handling:** Automatically dismisses intrusive location, notification, and cookie consent popups.
* **Auto-Liking:** Automatically swipes right (likes) on 20 profiles.
* **Match Handling:** Gracefully handles `ElementClickInterceptedException` errors by detecting "It's a Match!" popups and closing them to resume swiping.
* **Secure Credentials:** Uses `python-dotenv` to keep your login email and password hidden and secure.

## Prerequisites

* Python 3.x
* Google Chrome browser
* Required Python packages: `selenium`, `python-dotenv`

## Installation and Setup

1. **Clone the repository:**
   ```bash
   git clone <your-repository-url>
   cd <your-repository-folder>