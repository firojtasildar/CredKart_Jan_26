from selenium.webdriver.common.by import By

from pageObjects.Login_Page import Login_Page_Class


class Registration_Page_class(Login_Page_Class):

    text_name_xpath="//input[@id='name']"
    text_confirm_password_xpath="//input[@id='password-confirm']"

    def __init__(self, driver):
        super().__init__(driver)

    def enter_name(self,name):
        self.driver.find_element(By.XPATH,self.text_name_xpath).send_keys(name)

    def enter_confirm_password(self,password):
        self.driver.find_element(By.XPATH,self.text_confirm_password_xpath).send_keys(password)


