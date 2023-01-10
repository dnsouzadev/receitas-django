from pathlib import Path
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

ROOT_PATH = Path(__file__).parent.parent
CHROMEDRIVER_NAME = 'chromedriver.exe'
CHROMEDRIVER_PATH = ROOT_PATH / 'bin' / CHROMEDRIVER_NAME


def make_chrome_browser(*options):
    chrome_options = webdriver.ChromeOptions()

    if options is not None:
        for option in options:
            chrome_options.add_argument(option)

    chrome_service = Service(executable_path=CHROMEDRIVER_PATH)  # type: ignore
    browser = webdriver.Chrome(service=chrome_service, options=chrome_options)
    return browser


if __name__ == "__main__":
    browser = make_chrome_browser()
    browser.get('http://127.0.0.1:8000')
    sleep(2)
    browser.quit()
