import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path='/Users/viktoria27vika27/PycharmProjects/python_selenium/chromedriver')
base_url = 'https://www.saucedemo.com'
driver.get(base_url)
driver.maximize_window()
login_standart_user = "standard_user"
password_all = "secret_sauce"
"""Авторизация на сайте"""
user_name = driver.find_element(By.XPATH, "//input[@id='user-name']")  # ID XPATH
user_name.send_keys(login_standart_user)
print("Input Login")

password = driver.find_element(By.XPATH, "//input[@id='password']")  # ID XPATH
password.send_keys(password_all)
print("Input Password")
button_login = driver.find_element(By.XPATH, "//input[@id='login-button']")
button_login.click()
print("Click Login Button")

"""Информация о product_1 и добавление в корзину """
product_1 = driver.find_element(By.XPATH, "//*[@id='item_0_title_link']/div")
value_product_1 = product_1.text
print("Название product_1 : " + value_product_1)
price_product_1 = driver.find_element(By.XPATH, "//*[@id='inventory_container']/div/div[2]/div[2]/div[2]/div")
value_price_product_1 = price_product_1.text
print("Цена product_1 : " + value_price_product_1)
button_add_to_cart_product_1 = driver.find_element(By.XPATH, "//*[@id='add-to-cart-sauce-labs-bike-light']")
button_add_to_cart_product_1.click()
print("Product_1 добавлен в корзину")

"""Информация о product_2 и добавление в корзину"""
product_2 = driver.find_element(By.XPATH, "//*[@id='item_5_title_link']/div")
value_product_2 = product_2.text
print("Название product_2 : " + value_product_2)
price_product_2 = driver.find_element(By.XPATH, "//*[@id='inventory_container']/div/div[4]/div[2]/div[2]/div")
value_price_product_2 = price_product_2.text
print("Цена product_2 : " + value_price_product_2)
button_add_to_cart_product_2 = driver.find_element(By.XPATH, "//*[@id='add-to-cart-sauce-labs-fleece-jacket']")
button_add_to_cart_product_2.click()
print("Product_2 добавлен в корзину")
"""Переход в корзину"""
cart = driver.find_element(By.XPATH, "//*[@id='shopping_cart_container']/a")
cart.click()
print("Вход в корзину")
time.sleep(2)

"""Информация о product_1 в корзине"""
cart_product_1 = driver.find_element(By.XPATH, "//*[@id='item_0_title_link']/div")
value_cart_product_1 = cart_product_1.text
print("Название product_1 в корзине: " + value_cart_product_1)
assert value_product_1 == value_cart_product_1
print("Название product_1 верное")
price_cart_product_1 = driver.find_element(By.XPATH, "//*[@id='cart_contents_container']/div/div[1]/div[3]/div[2]/div[2]/div")
value_price_cart_product_1 = price_cart_product_1.text
print("Цена product_1 в корзине: " + value_price_cart_product_1)
assert value_price_product_1 == value_price_cart_product_1
print("Цена product_1 верная")

"""Информация о product_2 в корзине"""
cart_product_2 = driver.find_element(By.XPATH, "//*[@id='item_5_title_link']/div")
value_cart_product_2 = cart_product_2.text
print("Название product_2 в корзине: " + value_cart_product_2)
assert value_product_2 == value_cart_product_2
print("Название product_2 верное")
price_cart_product_2 = driver.find_element(By.XPATH, "//*[@id='cart_contents_container']/div/div[1]/div[4]/div[2]/div[2]/div")
value_price_cart_product_2 = price_cart_product_2.text
print("Цена product_2 в корзине: " + value_price_cart_product_2)
assert value_price_product_2 == value_price_cart_product_2
print("Цена product_2 верная")
"""Переходим к заполнению информации о пользователе"""
button_checkout_1 = driver.find_element(By.XPATH, "//*[@id='checkout']")
button_checkout_1.click()
print("Click CHECKOUT")
first_name = driver.find_element(By.XPATH, "//*[@id='first-name']")
first_name.send_keys("Nick")
print("Input FirstName")
last_name = driver.find_element(By.XPATH, "//*[@id='last-name']")
last_name.send_keys("Kuzin")
print("Input LastName")
zip_postal_code = driver.find_element(By.XPATH, "//*[@id='postal-code']")
zip_postal_code.send_keys("426000")
print("Input Postal Code")
time.sleep(2)
"""Переходим в CHECKOUT: OVERVIEW"""
button_continue = driver.find_element(By.XPATH, "//*[@id='continue']")
button_continue.click()
print("Click CONTINUE")
"""Проверка информации о product_1 в заказе"""
finish_product_1 = driver.find_element(By.XPATH, "//*[@id='item_0_title_link']/div")
value_finish_product_1 = finish_product_1.text
print("Название product_1 в заказе : " + value_finish_product_1)
assert value_product_1 == value_finish_product_1
print("Название product_1 верное")
price_finish_product_1 = driver.find_element(By.XPATH, "//*[@id='checkout_summary_container']/div/div[1]/div[3]/div[2]/div[2]/div")
value_price_finish_product_1 = price_finish_product_1.text
print("Цена product_1 в заказе : " + value_price_finish_product_1)
assert value_price_product_1 == value_price_finish_product_1
print("Цена product_1 верная")
"""Проверка информации о product_2 в заказе"""
finish_product_2 = driver.find_element(By.XPATH, "//*[@id='item_5_title_link']/div")
value_finish_product_2 = finish_product_2.text
print("Название product_2 в заказе : " + value_finish_product_2)
assert value_product_2 == value_finish_product_2
print("Название product_2 верное")
price_finish_product_2 = driver.find_element(By.XPATH, "//*[@id='checkout_summary_container']/div/div[1]/div[4]/div[2]/div[2]/div")
value_price_finish_product_2 = price_finish_product_2.text
print("Цена product_2 в заказе : " + value_price_finish_product_2)
assert value_price_product_2 == value_price_finish_product_2
print("Цена product_2 верная")
"""Сверяем итоговую цену с суммой двух продуктов"""
summary_price = driver.find_element(By.XPATH, "//*[@id='checkout_summary_container']/div/div[2]/div[5]")
value_summary_price = summary_price.text
print(value_summary_price)
price_1 = value_price_product_1.translate({ord('$'): None})
price_2 = value_price_product_2.translate({ord('$'): None})
price_total = value_summary_price.translate({ord(i): None for i in 'Item total:$'})

assert (float(price_1) + float(price_2)) == float(price_total)
print("Итоговая цена без налога верная")
time.sleep(2)
"""Завершаем покупку"""
button_finish = driver.find_element(By.XPATH, "//*[@id='finish']")
button_finish.click()
print("Click FINISH")
"""Проверяем переход на страницу с большими благодарностями за покупку"""
text_complete = driver.find_element(By.XPATH, "//*[@id='checkout_complete_container']/h2")
value_text_complete = text_complete.text
print(value_text_complete)
assert value_text_complete == "THANK YOU FOR YOUR ORDER"
print("GOOD TEST")
time.sleep(2)
driver.close()