from playwright.sync_api import sync_playwright, expect


with sync_playwright() as playwright:
    browser =  playwright.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto(" https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login")

    email_input = page.locator('//div[@data-testid="login-form-email-input"]')
    expect(email_input).to_be_visible()

    password_input = page.locator('//div[@data-testid="login-form-password-input"]')
    expect(password_input).to_be_visible()

    login_button = page.locator('//button[@data-testid="login-page-login-button"]')
    expect(login_button).to_be_visible()

    registration_button = page.locator('//a[@data-testid="login-page-registration-link"]')
    expect(registration_button).to_be_visible()
    with page.expect_navigation():
        registration_button.click()
        expect(page).to_have_url('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')

        email_input_registration = page.locator('//div[@data-testid="registration-form-email-input"]')
        expect(email_input_registration).to_be_visible()

        password_input_registration = page.locator('//div[@data-testid="registration-form-password-input"]')
        expect(password_input_registration).to_be_visible()

        registration_button_registration = page.locator('//button[@data-testid="registration-page-registration-button"]')
        expect(registration_button_registration).to_be_visible()


    page.wait_for_timeout(5000)