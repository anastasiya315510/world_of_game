import sys

import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

from MainGame import launch_flask_server


def check_server_alive(url):
    """Check if the score server is reachable."""
    try:
        response = requests.get(url, timeout=2)
        return response.status_code == 200
    except requests.exceptions.RequestException:
        return False


def test_scores_service(url: str)->bool:
    """
        Test a web service by checking the score element on the given URL.

        Steps:
        1. Open the given URL in a headless browser.
        2. Locate the score element in the page.
        3. Validate that its value is a number between 1 and 1000.
        4. Return True if valid, False otherwise.
        """

    options = Options()
    options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)


    try:
        driver.get(url)

        score_element = driver.find_element(By.ID, "score")
        score_text = score_element.text.strip()
        print(score_text)

        if not score_text.isdigit():
            return False

        score_value = int(score_text)
        return 1<= score_value<=1000


    except Exception as e:
        print(e)
        return False


    finally:
        driver.quit()

def main_function():
    """Main entry point — runs tests and exits with OS exit code."""
    score_server_url="http://127.0.0.1:5000/"

    launch_flask_server()

    if not check_server_alive(score_server_url):
        print("❌ Score server not reachable. Tests skipped.")
        sys.exit(-1)

    success = test_scores_service(score_server_url)
    sys.exit(0 if success else -1)



if __name__ == "__main__":
    main_function()