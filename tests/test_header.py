from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from helpers import AuthUser
from locators import HeadersLocators, ProfileLocators
from data import URLStorage, TestDataAuth


class TestHeader:
    def test_transition_to_profile_success(self, chrome_driver):
        """Проверка перехода по клику на Личный кабинет у авторизованного пользователя"""

        # Авторизация валидным пользователем
        chrome_driver.get(URLStorage().get_url('auth_page'))
        AuthUser().auth_user(chrome_driver, TestDataAuth.valid_email, TestDataAuth.valid_pass)

        # Переход на Личный кабинет по клику на Личный кабинет
        chrome_driver.find_element(*HeadersLocators.lk_btn).click()

        # Проверка
        check_profile_link_text = WebDriverWait(chrome_driver, 3).until(EC.visibility_of_element_located
                                                                        (ProfileLocators.profile_link)).text
        assert check_profile_link_text == 'Профиль'
