from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from helpers import AuthUser
from locators import AuthLocators, HeadersLocators, ProfileLocators, ConstructorLocators
from data import URLStorage, TestDataAuth


class TestProfile:
    def test_transition_to_constructor_via_btn_success(self, chrome_driver):
        """Проверка перехода в Конструктор по кнопке у авторизованного пользователя"""

        # Авторизация валидным пользователем
        chrome_driver.get(URLStorage().get_url('auth_page'))
        AuthUser().auth_user(chrome_driver, TestDataAuth.valid_email, TestDataAuth.valid_pass)

        # Переход в Личный кабинет
        chrome_driver.find_element(*HeadersLocators.lk_btn).click()

        # Переход на Конструктор по кнопке
        chrome_driver.find_element(*HeadersLocators.constructor_btn).click()

        # Проверка
        check_title_text = WebDriverWait(chrome_driver, 3).until(EC.visibility_of_element_located
                                                                 (ConstructorLocators.title)).text
        assert check_title_text == 'Соберите бургер'

    def test_transition_to_constructor_via_logo_success(self, chrome_driver):
        """Проверка перехода в Конструктор по лого у авторизованного пользователя"""

        # Авторизация валидным пользователем
        chrome_driver.get(URLStorage().get_url('auth_page'))
        AuthUser().auth_user(chrome_driver, TestDataAuth.valid_email, TestDataAuth.valid_pass)

        # Переход в Личный кабинет
        chrome_driver.find_element(*HeadersLocators.lk_btn).click()

        # Переход на Конструктор по Лого
        chrome_driver.find_element(*HeadersLocators.logo_btn).click()

        # Проверка
        check_title_text = WebDriverWait(chrome_driver, 3).until(EC.visibility_of_element_located
                                                                 (ConstructorLocators.title)).text
        assert check_title_text == 'Соберите бургер'

    def test_logout_by_btn_success(self, chrome_driver):
        """Проверка выхода из аккаунта по кнопке Выход"""

        # Авторизация валидным пользователем
        chrome_driver.get(URLStorage().get_url('auth_page'))
        AuthUser().auth_user(chrome_driver, TestDataAuth.valid_email, TestDataAuth.valid_pass)

        # Переход в Личный кабинет
        chrome_driver.find_element(*HeadersLocators.lk_btn).click()

        # Выход из аккаунта по кнопке Выход
        WebDriverWait(chrome_driver, 3).until(EC.visibility_of_element_located
                                              (ProfileLocators.logout_btn)).click()

        # Проверка
        check_logout_text = WebDriverWait(chrome_driver, 3).until(EC.visibility_of_element_located
                                                                  (AuthLocators.auth_btn)).text
        assert check_logout_text == 'Войти'
