class URLStorage:
    def __init__(self):
        self.base_url = "https://stellarburgers.nomoreparties.site/"
        self.urls = {
            'base_url': self.base_url,
            'registration_page': f"{self.base_url}register",
            'auth_page': f"{self.base_url}login",
            'forgot_password': f"{self.base_url}forgot-password"
        }

    def get_url(self, name):
        return self.urls.get(name, None)


class TestDataRegistration:
    """Тестовые данные для регистрации"""
    first_name = 'Анастасия'
    last_name = 'Заборских'
    cohort_number = 17


class TestDataAuth:
    """Тестовые данные для авторизации"""

    # Валидные тестовые данные
    valid_email = 'анастасиязаборских17001@yandex.ru'
    valid_pass = 'test01'

    # Невалидные тестовые данные
    invalid_email = 'неверный_email@yandex.ru'
    invalid_pass = 'неверный пароль'
