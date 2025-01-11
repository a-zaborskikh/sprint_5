from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from helpers import AuthUser
from locators import WelcomeLocators, HeadersLocators, RegLocators, RecoveryPassLocators


class TestAuth:
    base_url = "https://stellarburgers.nomoreparties.site/"

    def test_auth_valid_user_from_main_success(self, chrome_driver):
        """Проверка авторизации валидного пользователя с Главной страницы"""

        # Переход на Главную страницу
        chrome_driver.get(self.base_url)

        # Переход на форму авторизации с Главной страницы
        chrome_driver.find_element(*WelcomeLocators.auth_btn).click()

        # Авторизация валидным пользователем
        AuthUser().auth_user(chrome_driver, AuthUser.valid_email, AuthUser.valid_pass)

        # Проверка
        check_order_btn_text = WebDriverWait(chrome_driver, 3).until(EC.visibility_of_element_located
                                                                     (WelcomeLocators.order_btn)).text

        assert check_order_btn_text == 'Оформить заказ'

    def test_auth_valid_user_from_profile_success(self, chrome_driver):
        """Проверка авторизации валидного пользователя по кнопке Личного кабинета"""

        # Переход на Главную страницу
        chrome_driver.get(self.base_url)

        # Переход на форму авторизации по кнопке Личный кабинет
        chrome_driver.find_element(*HeadersLocators.lk_btn).click()

        # Авторизация валидным пользователем
        AuthUser().auth_user(chrome_driver, AuthUser.valid_email, AuthUser.valid_pass)

        # Проверка
        check_order_btn_text = WebDriverWait(chrome_driver, 3).until(EC.visibility_of_element_located
                                                                     (WelcomeLocators.order_btn)).text
        assert check_order_btn_text == 'Оформить заказ'

    def test_auth_valid_user_from_reg_success(self, chrome_driver):
        """Проверка авторизации валидного пользователя со страницы Регистрации"""

        # Переход на страницу регистрации
        chrome_driver.get(self.base_url + "register")

        # Переход на форму авторизации по кнопке Войти
        chrome_driver.find_element(*RegLocators.auth_link).click()

        # Авторизация валидным пользователем
        AuthUser().auth_user(chrome_driver, AuthUser.valid_email, AuthUser.valid_pass)

        # Проверка
        check_order_btn_text = WebDriverWait(chrome_driver, 3).until(EC.visibility_of_element_located
                                                                     (WelcomeLocators.order_btn)).text
        assert check_order_btn_text == 'Оформить заказ'

    def test_auth_valid_user_from_recovery_pass_success(self, chrome_driver):
        """Проверка авторизации валидного пользователя со страницы Восстановления пароля"""

        # Переход на страницу регистрации
        chrome_driver.get(self.base_url + "forgot-password")

        # Переход на форму авторизации по кнопке Войти
        chrome_driver.find_element(*RecoveryPassLocators.auth_link).click()

        # Авторизация валидным пользователем
        AuthUser().auth_user(chrome_driver, AuthUser.valid_email, AuthUser.valid_pass)

        # Проверка
        check_order_btn_text = WebDriverWait(chrome_driver, 3).until(EC.visibility_of_element_located
                                                                     (WelcomeLocators.order_btn)).text
        assert check_order_btn_text == 'Оформить заказ'
