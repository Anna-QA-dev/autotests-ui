import pytest
from playwright.sync_api import sync_playwright, Page


@pytest.fixture()
def chromium_page() -> Page:
    """Фикстура для создания новой страницы (без состояния авторизации)"""
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        yield page
        # Закрываем в обратном порядке
        context.close()
        browser.close()


@pytest.fixture(scope="session")
def initialize_browser_state():
    """Инициализация состояния браузера (регистрация пользователя)"""
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        # Регистрация пользователя
        page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")

        email_input = page.get_by_test_id('registration-form-email-input').locator('input')
        email_input.fill('user.name@gmail.com')

        username_input = page.get_by_test_id('registration-form-username-input').locator('input')
        username_input.fill('username')

        password_input = page.get_by_test_id('registration-form-password-input').locator('input')
        password_input.fill('password')

        registration_button = page.get_by_test_id('registration-page-registration-button')
        registration_button.click()

        page.wait_for_timeout(3000)

        # Сохраняем состояние
        context.storage_state(path="browser-state.json")

        # Закрываем
        context.close()
        browser.close()


@pytest.fixture()
def chromium_page_with_state(initialize_browser_state) -> Page:
    """Фикстура для создания страницы с сохраненным состоянием авторизации"""
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context(storage_state="browser-state.json")
        page = context.new_page()
        yield page
        # Закрываем в обратном порядке
        context.close()
        browser.close()