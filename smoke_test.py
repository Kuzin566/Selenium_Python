import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path='/Users/viktoria27vika27/PycharmProjects/python_selenium/chromedriver')
base_url = 'https://www.saucedemo.com'
driver.get(base_url)
driver.maximize_window()
login_standart_user = "standard_user"
password_all = "secret_sauce"
"""Авторизация на сайте"""
driver.find_element(By.XPATH, "//input[@id='user-name']").send_keys(login_standart_user)
print("Input Login")
driver.find_element(By.XPATH, "//input[@id='password']").send_keys(password_all)
print("Input Password")
driver.find_element(By.XPATH, "//input[@id='login-button']").click()
print("Click Login Button")
"""Информация о product_1 и добавление в корзину """
product_1 = driver.find_element(By.XPATH, "//*[@id='item_0_title_link']/div").text
print("Название product_1 : " + product_1)
price_product_1 = driver.find_element(By.XPATH, "//*[@id='inventory_container']/div/div[2]/div[2]/div[2]/div").text
print("Цена product_1 : " + price_product_1)
driver.find_element(By.XPATH, "//*[@id='add-to-cart-sauce-labs-bike-light']").click()
print("Product_1 добавлен в корзину")
"""Информация о product_2 и добавление в корзину"""
product_2 = driver.find_element(By.XPATH, "//*[@id='item_5_title_link']/div").text
print("Название product_2 : " + product_2)
price_product_2 = driver.find_element(By.XPATH, "//*[@id='inventory_container']/div/div[4]/div[2]/div[2]/div").text
print("Цена product_2 : " + price_product_2)
driver.find_element(By.XPATH, "//*[@id='add-to-cart-sauce-labs-fleece-jacket']").click()
print("Product_2 добавлен в корзину")
"""Переход в корзину"""
driver.find_element(By.XPATH, "//*[@id='shopping_cart_container']/a").click()
print("Вход в корзину")
time.sleep(2)
"""Информация о product_1 в корзине"""
cart_product_1 = driver.find_element(By.XPATH, "//*[@id='item_0_title_link']/div").text
print("Название product_1 в корзине: " + cart_product_1)
assert product_1 == cart_product_1
print("Название product_1 верное")
price_cart_product_1 = driver.find_element(By.XPATH, "//*[@id='cart_contents_container']/div/div[1]/div[3]/div[2]/div[2]/div").text
print("Цена product_1 в корзине: " + price_cart_product_1)
assert price_product_1 == price_cart_product_1
print("Цена product_1 верная")
"""Информация о product_2 в корзине"""
cart_product_2 = driver.find_element(By.XPATH, "//*[@id='item_5_title_link']/div").text
print("Название product_2 в корзине: " + cart_product_2)
assert product_2 == cart_product_2
print("Название product_2 верное")
price_cart_product_2 = driver.find_element(By.XPATH, "//*[@id='cart_contents_container']/div/div[1]/div[4]/div[2]/div[2]/div").text
print("Цена product_2 в корзине: " + price_cart_product_2)
assert price_product_2 == price_cart_product_2
print("Цена product_2 верная")
"""Переходим к заполнению информации о пользователе"""
driver.find_element(By.XPATH, "//*[@id='checkout']").click()
print("Click CHECKOUT")
driver.find_element(By.XPATH, "//*[@id='first-name']").send_keys("Nick")
print("Input FirstName")
driver.find_element(By.XPATH, "//*[@id='last-name']").send_keys("Kuzin")
print("Input LastName")
driver.find_element(By.XPATH, "//*[@id='postal-code']").send_keys("426000")
print("Input Postal Code")
time.sleep(2)
"""Переходим в CHECKOUT: OVERVIEW"""
driver.find_element(By.XPATH, "//*[@id='continue']").click()
print("Click CONTINUE")
"""Проверка информации о product_1 в заказе"""
finish_product_1 = driver.find_element(By.XPATH, "//*[@id='item_0_title_link']/div").text
print("Название product_1 в заказе : " + finish_product_1)
assert product_1 == finish_product_1
print("Название product_1 верное")
price_finish_product_1 = driver.find_element(By.XPATH, "//*[@id='checkout_summary_container']/div/div[1]/div[3]/div[2]/div[2]/div").text
print("Цена product_1 в заказе : " + price_finish_product_1)
assert price_product_1 == price_finish_product_1
print("Цена product_1 верная")
"""Проверка информации о product_2 в заказе"""
finish_product_2 = driver.find_element(By.XPATH, "//*[@id='item_5_title_link']/div").text
print("Название product_2 в заказе : " + finish_product_2)
assert product_2 == finish_product_2
print("Название product_2 верное")
price_finish_product_2 = driver.find_element(By.XPATH, "//*[@id='checkout_summary_container']/div/div[1]/div[4]/div[2]/div[2]/div").text
print("Цена product_2 в заказе : " + price_finish_product_2)
assert price_product_2 == price_finish_product_2
print("Цена product_2 верная")
"""Сверяем итоговую цену с суммой двух продуктов"""
summary_price = driver.find_element(By.XPATH, "//*[@id='checkout_summary_container']/div/div[2]/div[5]").text
print(summary_price)
price_1 = price_product_1.translate({ord('$'): None})
price_2 = price_product_2.translate({ord('$'): None})
price_total = summary_price.translate({ord(i): None for i in 'Item total:$'})
assert (float(price_1) + float(price_2)) == float(price_total)
print("Итоговая цена без налога верная")
time.sleep(2)
"""Завершаем покупку"""
driver.find_element(By.XPATH, "//*[@id='finish']").click()
print("Click FINISH")
"""Проверяем переход на страницу с большими благодарностями за покупку"""
text_complete = driver.find_element(By.XPATH, "//*[@id='checkout_complete_container']/h2").text
print(text_complete)
assert text_complete == "THANK YOU FOR YOUR ORDER"
print("GOOD TEST")
time.sleep(2)
driver.close()