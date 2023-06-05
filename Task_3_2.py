import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#Второй вариант для Задачи №3
class PageObject:
    driver = webdriver.Chrome(executable_path="C:\\Users\\kat1k\\Downloads\\chromedriver_win32\\chromedriver.exe")
    url = "https://www.a1.by/ru/shop/c/phones"
    driver.get(url)
    driver.implicitly_wait(5)

    def get_wait_of_element_located(self, element):
        return WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, element)))


class HeaderPage(PageObject):
    pass


class FilterPage(PageObject):
    pass


class MainPage(PageObject):

    list_device = "//div[@class = 'product-listing']"
    button_buy = "//div[@class = 'product-listing-box ']"
    buttons_buy = PageObject.driver.find_elements(By.XPATH, button_buy)

    def click_button(self, button):
        button.click()

    def click_button_2(self, button):
        button_1 = self.driver.find_element(By.XPATH, button)
        button_1.click()

    def wait_element(self, x):
        self.get_wait_of_element_located(x)


def get_info_about_order():
    info_about_order = []
    name_device = MainPage.driver.find_element(By.XPATH, "//span[ @ itemprop = 'name'] / following::h1").text
    payment_option = MainPage.driver.find_element(By.XPATH, "//span[@class = 'select2-selection select2-selection--single']").text
    info_about_order.append(name_device)
    info_about_order.append(payment_option)
    return info_about_order


class MainPageDevice(MainPage):
    button_payment_options = "//label[@class='form-label form-label--autosuggest ']"
    credit_six_month = "//li[@class= 'select2-results__option'][2]"
    button_sign_and_buy = "//div[@class = 'live-filter-content-item active']/descendant::button"


def main():

    first_action = MainPage()
    first_action.wait_element(MainPage.list_device)
    first_action.click_button(MainPage.buttons_buy[int(random.randint(0, len(MainPage.buttons_buy) - 1))])

    second_action = MainPageDevice()
    second_action.wait_element(MainPageDevice.button_payment_options)
    second_action.click_button_2(MainPageDevice.button_payment_options)
    second_action.wait_element(MainPageDevice.credit_six_month)
    second_action.click_button_2(MainPageDevice.credit_six_month)

    print(f'Выбран {get_info_about_order()[0]}, вариант оплаты: {get_info_about_order()[1]}.')

    third_action = MainPageDevice()
    third_action.click_button_2(MainPageDevice.button_sign_and_buy)

    MainPage.driver.quit()


if __name__ == '__main__':

    main()

