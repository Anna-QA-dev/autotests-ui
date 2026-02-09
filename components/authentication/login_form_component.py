from playwright.sync_api import Page
from components.base_component import BaseComponent
from elements.input import Input
from elements.button import Button

class LoginFormComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.email_input = Input(page, 'login-form-email-input', 'Email')
        self.password_input = Input(page, 'login-form-password-input', 'Password')
        self.login_button = Button(page, 'login-page-login-button', 'Login button')

    def fill(self, email: str, password: str):
        self.email_input.fill(email)
        self.email_input.check_have_value(email)

        self.password_input.fill(password)
        self.password_input.check_have_value(password)

    def check_visible(self, email: str = "", password: str = ""):
        self.email_input.check_visible()
        self.password_input.check_visible()
        self.login_button.check_visible()

        if email:
            self.email_input.check_have_value(email)
        if password:
            self.password_input.check_have_value(password)