import requests
import time
from datetime import datetime

def ping_website(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}]  Success! {url} is reachable.")
        else:
            print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}]  Warning! {url} returned status code {response.status_code}.")
    except requests.ConnectionError:
        print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}]  Error! Unable to connect to {url}.")

if __name__ == "__main__":
    website_urls = [
        "https://para-i1ne.onrender.com/ud",  # Replace with your website URLs
        "https://fantasyflex.onrender.com/ud",
        
    ]

    while True:
        for url in website_urls:
            ping_website(url)
        time.sleep(300)  # Sleep for 5 minutes (300 seconds)
what is a github description for this script