from selenium.webdriver.common.by import By


class WelcomeLocators:
    """Локаторы на Главной странице"""

    auth_btn = (By.XPATH, "//button[contains(@class, '33qZ0') and contains(text(), 'Войти')]")  # Кнопка "Войти"
    order_btn = (By.XPATH, "//button[contains(@class, '33qZ0') and text()='Оформить заказ']")  # Кнопка "Оформить заказ"


class HeadersLocators:
    """Локаторы в шапке сервиса"""

    lk_btn = (By.XPATH, "//p[contains(@class, 'AppHeader') and text()='Личный Кабинет']")  # Кнопка Личный кабинет
    constructor_btn = (By.XPATH, "//a/p[text()='Конструктор']")  # Кнопка Конструктор
    logo_btn = (By.CLASS_NAME, "AppHeader_header__logo__2D0X2")


class RegLocators:
    """Локаторы на странице Регистрации"""

    name_input = (By.XPATH, "//fieldset[1]//input[@type='text' and @name='name']")  # Инпут Имя
    email_input = (By.XPATH, "//fieldset[2]//input[@type='text' and @name='name']")  # Инпут Email
    pass_input = (By.NAME, "Пароль")  # Инпут Пароль
    reg_btn = (By.XPATH, "//button[text()='Зарегистрироваться']")  # Кнопка Зарегистрироваться
    incorrect_pass_error = (By.XPATH, "//p[text()='Некорректный пароль']")  # Ошибка "Некорректный пароль"
    auth_link = (By.CLASS_NAME, "Auth_link__1fOlj")  # Гиперссылка Войти


class AuthLocators:
    """Локаторы на странице Авторизации"""

    email_input = (By.XPATH, "//fieldset[1]//input[@type='text' and @name='name']")  # Инпут Email
    pass_input = (By.NAME, "Пароль")  # Инпут Пароль
    auth_btn = (By.XPATH, "//button[contains(@class, '33qZ0') and contains(text(), 'Войти')]")  # Кнопка Войти


class RecoveryPassLocators:
    """Локаторы на странице Восстановление пароля"""

    auth_link = (By.CLASS_NAME, "Auth_link__1fOlj")  # Гиперссылка Войти


class ProfileLocators:
    """Локаторы на странице Личный кабинет"""

    profile_link = (By.LINK_TEXT, "Профиль")  # Гиперссылка Профиль
    logout_btn = (By.XPATH, "//nav[@class='Account_nav__Lgali']//button[text()='Выход']")  # кнопка Выход


class ConstructorLocators:
    """Локаторы в разделе Конструктор"""

    title = (By.XPATH, "//h1[text()='Соберите бургер']")  # Заголовок "Соберите бургер"
    buns_tab = (By.XPATH, "//div[contains(@class, 'tab_tab__1SPyG') and contains(*, 'Булки')]")  # Таб Булки
    sauces_tab = (By.XPATH, "//div[contains(@class, 'tab_tab__1SPyG') and contains(*, 'Соусы')]")  # Таб Соусы
    fillings_tab = (By.XPATH, "//div[contains(@class, 'tab_tab__1SPyG') and contains(*, 'Начинки')]")  # Таб Начинки
