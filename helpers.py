import random
import string
from locators import AuthLocators


class UserGenerator:
    """Генерация логина и пароля"""

    @staticmethod
    def generate_login(first_name, last_name, cohort_number):
        random_digits = str(random.randint(000, 999))
        domain = 'yandex.ru'
        return f"{first_name.lower()}{last_name.lower()}{str(cohort_number)}{random_digits}@{domain}"

    @staticmethod
    def generate_password(length_pass):
        return ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=length_pass))


class AuthUser:
    @staticmethod
    def auth_user(chrome_driver, email, password):
        """Прохождение авторизации валидным пользователем"""

        chrome_driver.find_element(*AuthLocators.email_input).send_keys(email)
        chrome_driver.find_element(*AuthLocators.pass_input).send_keys(password)
        chrome_driver.find_element(*AuthLocators.auth_btn).click()
