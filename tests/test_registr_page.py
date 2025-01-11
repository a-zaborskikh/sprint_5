from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators import RegLocators, AuthLocators
from helpers import UserGenerator


class TestRegistration:
    base_url = "https://stellarburgers.nomoreparties.site/"
    first_name = 'Анастасия'
    last_name = 'Заборских'
    cohort_number = 17

    def test_new_user_valid_all_data_success(self, chrome_driver):
        # Генерация рандомных данных
        email = UserGenerator.generate_login(self.first_name, self.last_name, self.cohort_number)
        password = UserGenerator.generate_password(6)

        # Переход на страницу регистрации
        chrome_driver.get(self.base_url + "register")

        # Регистрация
        chrome_driver.find_element(*RegLocators.name_input).send_keys(self.first_name)
        chrome_driver.find_element(*RegLocators.email_input).send_keys(email)
        chrome_driver.find_element(*RegLocators.pass_input).send_keys(password)
        chrome_driver.find_element(*RegLocators.reg_btn).click()

        # Ожидание загрузки страницы
        WebDriverWait(chrome_driver, 3).until(EC.visibility_of_element_located(AuthLocators.auth_btn))

        # проверка, что после регистрации произошел переход на страницу авторизации
        assert chrome_driver.current_url == self.base_url + "login"

    def test_new_user_with_pass_6_symbol_error(self, chrome_driver):
        # Генерация рандомных данных
        email = UserGenerator.generate_login(self.first_name, self.last_name, self.cohort_number)
        password = UserGenerator.generate_password(5)

        # Переход на страницу регистрации
        chrome_driver.get(self.base_url + "register")

        # Регистрация
        chrome_driver.find_element(*RegLocators.name_input).send_keys(self.first_name)
        chrome_driver.find_element(*RegLocators.email_input).send_keys(email)
        chrome_driver.find_element(*RegLocators.pass_input).send_keys(password)
        chrome_driver.find_element(*RegLocators.reg_btn).click()

        # проверка, что появилась ошибка об некорректном пароле
        check_error_reg_incorrect_pass_text = chrome_driver.find_element(*RegLocators.incorrect_pass_error).text
        assert check_error_reg_incorrect_pass_text == 'Некорректный пароль'
