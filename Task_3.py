import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def get_wait_of_element_located(element):
    return WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, element)))

#Инициализация дайвера
driver = webdriver.Chrome(executable_path="C:\\Users\\kat1k\\Downloads\\chromedriver_win32\\chromedriver.exe")
url = "https://www.a1.by/ru/shop/c/phones"
driver.get(url) #(1.	Перейти по ссылке https://www.a1.by/ru/shop/c/phones)
driver.implicitly_wait(5)

#Ожидание отображаения списка с телефонами. Сбор всех телефонов на странице в список.
#Выбор случайным образом телефона на который кликнем.
#(На странице выбрать случайным образом блок со смартфоном и нажать на кнопку «Перейти к покупке»)
get_wait_of_element_located("//div[@class = 'product-listing']")
buttons_buy = driver.find_elements(By.XPATH, "//div[@class = 'product-listing-box ']")
buttons_buy[int(random.randint(0, len(buttons_buy) - 1))].click()

#Ожидание отображаения окна с выбором варианта оплаты. Клик на выпадающий список.
#(Справа из выпадающего списка выбрать вариант оплаты в рассрочку на 6 месяцев: «6 мес по ххх руб/мес»)
get_wait_of_element_located("//label[@class='form-label form-label--autosuggest ']")
button_payment_options = driver.find_element(By.XPATH, "//label[@class='form-label form-label--autosuggest ']")
button_payment_options.click()
#Ожидание отображаения в выпавшем окне варианта с 6-ю месяцами. Клик на вариант оплаты с 6 мес.
get_wait_of_element_located("//li[@class= 'select2-results__option'][2]")
button_six_months_credit = driver.find_element(By.XPATH, "//li[@class= 'select2-results__option'][2]")
button_six_months_credit.click()

#Сбор информации о заказе (выбранный телефон и выбранный вариант оплаты)
info_about_order = []
name_device = driver.find_element(By.XPATH, "//span[ @ itemprop = 'name'] / following::h1").text
payment_option = driver.find_element(By.XPATH, "//span[@class = 'select2-selection select2-selection--single']").text
info_about_order.append(name_device)
info_about_order.append(payment_option)

#Клик на кнопку Войти и купить
button_sign_and_buy = driver.find_element(By.XPATH, "//div[@class = 'live-filter-content-item active']/descendant::button")
button_sign_and_buy.click()
print(f'Выбран {info_about_order[0]}, вариант оплаты: {info_about_order[1]}.')

driver.quit()









