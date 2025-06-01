from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from data import GenerateUserData
from locators import MainLocators, RegistrationLocators, ProfileLocators


class TestLogin:

    def test_successful_login(self, driver):
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

        driver.find_element(*ProfileLocators.PROFILE_BUTTON).click()

        wait.until(EC.element_to_be_clickable(ProfileLocators.LOGOUT_BUTTON)).click()
        wait.until(EC.presence_of_element_located(MainLocators.LOGIN_REGISTER_BUTTON))

        login_button = driver.find_element(*MainLocators.LOGIN_REGISTER_BUTTON)
        wait.until(EC.element_to_be_clickable(MainLocators.LOGIN_REGISTER_BUTTON))
        login_button.click()

        wait.until(EC.visibility_of_element_located(RegistrationLocators.EMAIL_INPUT)).send_keys(email)
        driver.find_element(*RegistrationLocators.PASSWORD_INPUT).send_keys(password)

        login_button = driver.find_element(*MainLocators.LOGIN_BUTTON)
        wait.until(EC.element_to_be_clickable(MainLocators.LOGIN_BUTTON))
        login_button.click()

        user_avatar = WebDriverWait(driver, 10).until(EC.presence_of_element_located(MainLocators.USER_AVATAR))
        assert user_avatar.is_displayed()
