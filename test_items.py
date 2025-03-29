import time
from selenium.webdriver.common.by import By


def test_check_adding_product_to_basket(browser, language):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)

    time.sleep(30)

    add_to_basket_button = browser.find_elements(By.CSS_SELECTOR, "button[class='btn btn-lg btn-primary btn-add-to-basket']")
    assert add_to_basket_button, "Не найдена кнопка ДОБАВИТЬ В КОРЗИНУ"
    add_to_basket_button[0].click()
