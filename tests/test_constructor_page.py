from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from helpers import AuthUser
from locators import ConstructorLocators


class TestConstructor:
    base_url = "https://stellarburgers.nomoreparties.site/"

    # Список табов для проверки переходов
    locators = [
        ConstructorLocators.buns_tab,
        ConstructorLocators.sauces_tab,
        ConstructorLocators.fillings_tab
    ]

    def test_transition_between_tabs_signin_success(self, chrome_driver):
        """Проверка перехода между табами в Конструкторе у авторизованного пользователя"""

        # Авторизация валидным пользователем
        chrome_driver.get(self.base_url + 'login')
        AuthUser().auth_user(chrome_driver, AuthUser.valid_email, AuthUser.valid_pass)

        # Проверка
        for locator in self.locators:
            element = WebDriverWait(chrome_driver, 3).until(EC.visibility_of_element_located(locator))
            chrome_driver.execute_script("arguments[0].click();", element)
            current_class = element.get_attribute('class')
            assert "tab_tab_type_current" in current_class

    def test_transition_between_tabs_logout_success(self, chrome_driver):
        """Проверка перехода между табами в Конструкторе у неавторизованного пользователя"""

        # Переход на Главную страницу
        chrome_driver.get(self.base_url)

        # Проверка
        for locator in self.locators:
            element = WebDriverWait(chrome_driver, 3).until(EC.visibility_of_element_located(locator))
            chrome_driver.execute_script("arguments[0].click();", element)
            current_class = element.get_attribute('class')
            assert "tab_tab_type_current" in current_class
