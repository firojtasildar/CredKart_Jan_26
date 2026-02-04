from asyncio import wait

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class Login_Page_Class:

    text_email_xpath="//input[@id='email']"
    text_password_xpath="//input[@id='password']"
    click_login_register_button_xpath="//button[@type='submit']"
    click_menu_button_xpath="//a[@role='button']"
    click_logout_button_xpath="//a[normalize-space()='Logout']"

    def __init__(self,driver):
        self.driver=driver
        driver.implicitly_wait(20)

    def enter_email(self,email):
        self.driver.find_element(By.XPATH,self.text_email_xpath).send_keys(email)

    def enter_password(self,password):
        self.driver.find_element(By.XPATH,self.text_password_xpath).send_keys(password)

    def click_login_register_button(self):
        self.driver.find_element(By.XPATH,self.click_login_register_button_xpath).click()

    def click_menu_button(self):
        self.driver.find_element(By.XPATH,self.click_menu_button_xpath).click()

    def click_logout_button(self):
        self.driver.find_element(By.XPATH,self.click_logout_button_xpath).click()

    def verify_menu_button_visibility(self):
        try:
            ex_wait =WebDriverWait(self.driver, 20)
            ex_wait.until(EC.visibility_of_element_located((By.XPATH, self.click_menu_button_xpath)))
            self.driver.find_element(By.XPATH,self.click_menu_button_xpath)
            return "pass"
        except:
            return "fail"



