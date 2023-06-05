import random
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def browser_init():
    driver = webdriver.Chrome(executable_path="C:\\Users\\kat1k\\Downloads\\chromedriver_win32\\chromedriver.exe")
    driver.implicitly_wait(5)
    yield driver
    driver.quit()


def test_browser(browser_init):
    url = "https://www.a1.by/ru/shop/c/phones"
    browser_init.get(url)
    assert url == browser_init.current_url

    WebDriverWait(browser_init, 5).until(EC.visibility_of_element_located((By.XPATH, "//div[@class = 'product-listing']")))
    buttons_buy = browser_init.find_elements(By.XPATH, "//div[@class = 'product-listing-box ']")
    device = buttons_buy[int(random.randint(0, len(buttons_buy) - 1))]
    device.click()
    assert buttons_buy != []

    WebDriverWait(browser_init, 5).until(EC.visibility_of_element_located((By.XPATH,
                                                                           "//label[@class='form-label form-label--autosuggest ']")))
    button_payment_options = browser_init.find_element(By.XPATH, "//label[@class='form-label form-label--autosuggest ']")
    button_payment_options.click()


    WebDriverWait(browser_init, 5).until(EC.visibility_of_element_located((By.XPATH,
                                                                           "//li[@class= 'select2-results__option'][2]")))
    button_six_months_credit = browser_init.find_element(By.XPATH, "//li[@class= 'select2-results__option'][2]")
    button_six_months_credit.click()
    payment_option = browser_init.find_element(By.XPATH,
                                               "//span[@class = 'select2-selection select2-selection--single']").text
    assert payment_option.__contains__('6 мес') == True
    assert payment_option.__contains__('24 мес') == False

    info_about_order = []
    name_device = browser_init.find_element(By.XPATH, "//span[ @ itemprop = 'name'] / following::h1").text
    info_about_order.append(name_device)
    info_about_order.append(payment_option)


    button_sign_and_buy = browser_init.find_element(By.XPATH, "//div[@class = 'live-filter-content-item active']/descendant::button")
    button_sign_and_buy.click()
    header_window_sign = browser_init.find_element(By.XPATH, "// h1[ @ class = 'h h--2']").text
    assert header_window_sign == "Вход в аккаунт"

    print(f'Выбран {info_about_order[0]}, вариант оплаты: {info_about_order[1]}.')