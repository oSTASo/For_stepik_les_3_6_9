import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


def test_button_add_to_basket(browser):
    url = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    browser.get(url)
    time.sleep(5)
    assert WebDriverWait(browser, 5).until(ec.presence_of_element_located((By.CSS_SELECTOR, '.btn-add-to-basket')))
