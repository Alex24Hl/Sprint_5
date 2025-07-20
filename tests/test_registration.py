from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from data import GenerateUserData
from locators import MainLocators, RegistrationLocators, ProfileLocators


class TestRegistration:

    def test_successful_registration(self, driver):
        driver.get("https://qa-desk.stand.praktikum-services.ru/")

        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(MainLocators.LOGIN_REGISTER_BUTTON)).click()  

        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(RegistrationLocators.NO_ACCOUNT_BUTTON)).click()            

        email = GenerateUserData.generate_user_email()
        password = GenerateUserData.generate_password()

        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(RegistrationLocators.EMAIL_INPUT)).send_keys(email)        
        
        driver.find_element(*RegistrationLocators.PASSWORD_INPUT).send_keys(password)
        driver.find_element(*RegistrationLocators.CONFIRM_PASSWORD_INPUT).send_keys(password)
        driver.find_element(*RegistrationLocators.CREATE_ACCOUNT_BUTTON).click()

        WebDriverWait(driver, 10).until(EC.presence_of_element_located(MainLocators.PLACE_AD_BUTTON))                    
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(MainLocators.USER_AVATAR))

        assert driver.find_element(*MainLocators.USER_NAME).is_displayed()
    
    def test_invalid_email_registration(self, driver):
        driver.get("https://qa-desk.stand.praktikum-services.ru/")

        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(MainLocators.LOGIN_REGISTER_BUTTON)).click()   

        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(RegistrationLocators.NO_ACCOUNT_BUTTON)).click()

        invalid_email = GenerateUserData.generate_invalid_email()
        password = GenerateUserData.generate_password()

        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(RegistrationLocators.EMAIL_INPUT)).send_keys(invalid_email)

        driver.find_element(*RegistrationLocators.PASSWORD_INPUT).send_keys(password)
        driver.find_element(*RegistrationLocators.CONFIRM_PASSWORD_INPUT).send_keys(password)
        driver.find_element(*RegistrationLocators.CREATE_ACCOUNT_BUTTON).click()

        email_error = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(RegistrationLocators.EMAIL_ERROR_MESSAGE))
        assert "Ошибка" in email_error.text

        error_email_container = driver.find_element(*RegistrationLocators.INPUT_ERROR_CONTAINER_EMAIL)
        assert "input_inputerror" in error_email_container.get_attribute("class").lower()

        error_password_container = driver.find_element(*RegistrationLocators.INPUT_ERROR_CONTAINER_PASSWORD)
        assert "input_inputerror" in error_password_container.get_attribute("class").lower()

        error_confirm_container = driver.find_element(*RegistrationLocators.INPUT_ERROR_CONTAINER_SUBMIT_PASSWORD)
        assert "input_inputerror" in error_confirm_container.get_attribute("class").lower()

    def test_registration_with_existing_user(self, driver):
        driver.get("https://qa-desk.stand.praktikum-services.ru/")

        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(MainLocators.LOGIN_REGISTER_BUTTON)).click()      

        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(RegistrationLocators.NO_ACCOUNT_BUTTON)).click()
            
        email = GenerateUserData.generate_invalid_email()
        password = GenerateUserData.generate_password()

        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(RegistrationLocators.EMAIL_INPUT)).send_keys(email)

        driver.find_element(*RegistrationLocators.PASSWORD_INPUT).send_keys(password)
        driver.find_element(*RegistrationLocators.CONFIRM_PASSWORD_INPUT).send_keys(password)
        driver.find_element(*RegistrationLocators.CREATE_ACCOUNT_BUTTON).click()

        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(ProfileLocators.LOGOUT_BUTTON)).click()
            
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(MainLocators.LOGIN_REGISTER_BUTTON))
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(MainLocators.LOGIN_REGISTER_BUTTON)).click()

        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(RegistrationLocators.NO_ACCOUNT_BUTTON)).click()

        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(RegistrationLocators.EMAIL_INPUT)).send_keys(email)

        driver.find_element(*RegistrationLocators.PASSWORD_INPUT).send_keys(password)
        driver.find_element(*RegistrationLocators.CONFIRM_PASSWORD_INPUT).send_keys(password)
        driver.find_element(*RegistrationLocators.CREATE_ACCOUNT_BUTTON).click()

        error_message = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(RegistrationLocators.EMAIL_ERROR_MESSAGE))
        assert "Ошибка" in error_message.text

        email_container = driver.find_element(*RegistrationLocators.INPUT_ERROR_CONTAINER_EMAIL)
        assert "input_inputerror" in email_container.get_attribute("class").lower()
