from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common import StaleElementReferenceException

from data import GenerateUserData
from locators import *


class TestCreateAd:

    def test_create_ad_authorized_user(self, driver):
        driver.get("https://qa-desk.stand.praktikum-services.ru/")

        wait = WebDriverWait(driver, 10)

        wait.until(EC.element_to_be_clickable(MainLocators.LOGIN_REGISTER_BUTTON)).click()

        wait.until(EC.element_to_be_clickable(RegistrationLocators.NO_ACCOUNT_BUTTON)).click()

        email = GenerateUserData.generate_user_email()
        password = GenerateUserData.generate_password()

        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(RegistrationLocators.EMAIL_INPUT)).send_keys(email)        

        driver.find_element(*RegistrationLocators.PASSWORD_INPUT).send_keys(password)
        driver.find_element(*RegistrationLocators.CONFIRM_PASSWORD_INPUT).send_keys(password)
        driver.find_element(*RegistrationLocators.CREATE_ACCOUNT_BUTTON).click()

        wait.until(EC.element_to_be_clickable(MainLocators.PLACE_AD_BUTTON)).click()  
        wait.until(EC.visibility_of_element_located(AdLocators.NAME_OF_GOOD_INPUT)).send_keys("Смартфон")

        desc_input = driver.find_element(*AdLocators.DESCRIPTION)
        driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", desc_input)
        wait.until(EC.visibility_of(desc_input)).send_keys("Продаётся iPhone 13 Pro, 128 GB, Green")

        category_dropdown = wait.until(EC.element_to_be_clickable(AdLocators.DROPDOWN_CATEGORY))
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", category_dropdown)
        category_dropdown.click()

        technology_button = wait.until(EC.element_to_be_clickable(AdLocators.TECHNOLOGY_CATEGORY))
        technology_button.click()

        price_input = driver.find_element(*AdLocators.PRICE)
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", price_input)
        wait.until(EC.visibility_of(price_input)).send_keys("45000")

        city_dropdown = wait.until(EC.element_to_be_clickable(AdLocators.DROPDOWN_CITY))
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", city_dropdown)
        city_dropdown.click()

        city_button = wait.until(EC.element_to_be_clickable(AdLocators.CITY_BUTTON))
        city_button.click()

        radiobutton = driver.find_element(*AdLocators.RADIOBUTTON)
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", radiobutton)
        wait.until(EC.element_to_be_clickable(radiobutton)).click()

        publish_button = driver.find_element(*AdLocators.PUBLISH_BUTTON)
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", publish_button)
        wait.until(EC.element_to_be_clickable(publish_button)).click()

        try:
            profile_button = wait.until(EC.element_to_be_clickable(ProfileLocators.PROFILE_BUTTON))
            driver.execute_script("arguments[0].scrollIntoView({block: 'start'});", profile_button)
            profile_button.click()
        except StaleElementReferenceException:
            profile_button = wait.until(EC.element_to_be_clickable(ProfileLocators.PROFILE_BUTTON))
            driver.execute_script("arguments[0].scrollIntoView({block: 'start'});", profile_button)
            profile_button.click()

        wait.until(EC.visibility_of_element_located(ProfileLocators.MY_ADS_HEADER))
        ads_titles = wait.until(EC.presence_of_all_elements_located(ProfileLocators.MY_AD_H2))
        assert any("Смартфон" in ad.text for ad in ads_titles), "Созданное объявление не найдено среди списка 'Мои объявления'"

    def test_create_ad_unauthorized_user(self, driver):
        driver.get("https://qa-desk.stand.praktikum-services.ru/")

        wait = WebDriverWait(driver, 10)

        wait.until(EC.element_to_be_clickable(MainLocators.PLACE_AD_BUTTON)).click()        

        auth_modal_header = wait.until(EC.visibility_of_element_located(AuthRequiredLocators.AUTH_REQUIRED_HEADER))
        assert auth_modal_header.is_displayed()
        assert "авторизуйтесь" in auth_modal_header.text.lower()
