# Musical Time Machine: Billboard Hot 100 to Spotify

## Features
* **Web Scraping:** Uses `BeautifulSoup` and `requests` to scrape the top 100 songs from the Billboard Hot 100 archive.
* **Spotify API Integration:** Connects to the Spotify API using the `spotipy` library.
* **OAuth2 Authentication:** Securely authenticates the user and requests the necessary permissions (`playlist-modify-private`) to create playlists.
* **Automated Playlist Creation:** Searches for each scraped song on Spotify, retrieves their unique URIs, and adds them to a newly created private playlist.
* **Error Handling & Stability:** Implements custom delays (`time.sleep`) and API timeout retries to prevent connection drops when sending bulk requests.

## Technologies Used
* Python 3
* [BeautifulSoup4](https://pypi.org/project/beautifulsoup4/) (Web Scraping)
* Requests (HTTP requests)
* [Spotipy](https://spotipy.readthedocs.io/) (Spotify Web API wrapper)
* Python-dotenv (Environment variable management)

## Setup and Installation

### 1. Spotify Developer Account Setup
1. Go to the [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/).
2. Log in and create a new App.
3. Add `http://example.com` (or your preferred URL) to the **Redirect URIs** in your app settings.
4. Go to **User Management** in the dashboard and add the exact email address associated with your Spotify account.
5. Note down your **Client ID** and **Client Secret**.

### 2. Local Environment Setup
1. Clone this repository.
2. Install the required Python packages:
   ```bash
   pip install bs4 requests spotipy python-dotenv