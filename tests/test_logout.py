from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from data import GenerateUserData
from locators import MainLocators, RegistrationLocators, ProfileLocators


class TestLogout:

    def test_logout(self, driver):
        driver.get("https://qa-desk.stand.praktikum-services.ru/")

        wait = WebDriverWait(driver, 10)

        wait.until(EC.element_to_be_clickable(MainLocators.LOGIN_REGISTER_BUTTON)).click()

        wait.until(EC.element_to_be_clickable(RegistrationLocators.NO_ACCOUNT_BUTTON)).click()

        email = GenerateUserData.generate_user_email()
        password = GenerateUserData.generate_password()

        wait.until(EC.visibility_of_element_located(RegistrationLocators.EMAIL_INPUT)).send_keys(email)

        driver.find_element(*RegistrationLocators.PASSWORD_INPUT).send_keys(password)
        driver.find_element(*RegistrationLocators.CONFIRM_PASSWORD_INPUT).send_keys(password)
        driver.find_element(*RegistrationLocators.CREATE_ACCOUNT_BUTTON).click()

        wait.until(EC.visibility_of_element_located(ProfileLocators.USER_AVATAR))

        wait.until(EC.element_to_be_clickable(ProfileLocators.LOGOUT_BUTTON)).click()

        wait.until(EC.visibility_of_element_located(MainLocators.LOGIN_REGISTER_BUTTON))

        assert driver.find_element(*MainLocators.LOGIN_REGISTER_BUTTON).is_displayed()
