import time

from webdriver_wrapper import WebDriverWrapper
from selenium.webdriver.common.keys import Keys


def lambda_handler(*args, **kwargs):
    driver = WebDriverWrapper()
    example_text = ''
    sekinAl="https://seekingalpha.com/market-news/all" 
# driver.get("http://www.python.org")
    driver.get_url(sekinAl)
# assert "Python" in driver.title
# driver
    elem = driver.find_elements_by_class_name("title")
    for i in elem:
        print(i.text)

    driver.close()

    return example_text
