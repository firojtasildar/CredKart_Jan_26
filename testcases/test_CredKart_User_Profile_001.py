"""
smoke testing-->verification of url
                -->You need to test add,edit,search,delete functionality on every page
                --> you need to test broken links,broken images,imp. links,imp. images
                -->you need to check,menu,submenus
                -->From Page title,credentials,on every page add,edit,search,delete
                    broken links,broken images menus,sub menus

                    this all comes under smoke testing part

Regression Testing-->Those testcases where most defects apper,critical defects appear and
                     which may impacting other functionalities also.

                     so we have to identify those kind of test cases and put those testcases under
                     regression suit.

                     and other imp. testcases which are discussed in team.
                     e.g.-->Any financial transaction is imp. testcase and have to check in every build.
                     e.g.-->whether money deducted from sender account.
                            and whether money deposited in receiver account.
"""


import pytest
from faker import Faker

from conftest import browser_setup
from pageObjects.Login_Page import Login_Page_Class
from pageObjects.Registration_Page import Registration_Page_class
from readConfig import ReadConfigClass
from utilities.Logger import log_generator_class


@pytest.mark.usefixtures("browser_setup")
class Test_User_Profile :
    driver=None
    email=ReadConfigClass.get_data_for_email()
    password=ReadConfigClass.get_data_for_password()
    login_url=ReadConfigClass.get_data_for_login_url()
    register_url=ReadConfigClass.get_data_for_register_url()
    homepage_url=ReadConfigClass.get_data_for_homepage_url()
    log=log_generator_class.log_gen_method()

    @pytest.mark.smoke
    @pytest.mark.flaky(reruns=2, reruns_delay=1)
    #@pytest.mark.dependency(name=["test_credkart_registration"])
    #@pytest.mark.order(1)
    def test_verify_credkart_url_001(self):
        # self.log.debug("This is debug log") #Log Levels
        # self.log.info("This is info log")
        # self.log.warning("This is warning log")
        # self.log.error("This is error log")
        # self.log.critical("This is critical log")
        self.log.info("Testcase test_verify_credkart_url_001 started ")
        self.log.info("Opening Brower")
        self.driver.get(self.register_url)
        self.log.info(f"Opening Browser and getting url->{self.register_url}")
        self.log.info("Checking Page Title")
        if self.driver.title == "CredKart":
            print(f"Page Title-->{self.driver.title}")
            self.log.info("Testcase test_verify_credkart_url_001 passed")
            self.log.info("Taking Screenshot")
            self.driver.save_screenshot(".\\Screenshot\\test_verify_credkart_url_001_pass.png")
        else:
            self.log.info("Testcase test_verify_credkart_url_001 failed")
            self.log.info("Taking Screenshot")
            self.driver.save_screenshot(".\\Screenshot\\test_verify_credkart_url_001_fail.png")
            assert False,"Url test fail"
        self.log.info("Testcase test_verify_credkart_url_001 completed")

    @pytest.mark.smoke
    @pytest.mark.flaky(reruns=2, reruns_delay=1)
    #@pytest.mark.dependency(depends=["test_credkart_registration"])
    #@pytest.mark.order(2)
    def test_credkart_login_002(self):
        self.log.info("Testcase test_Credkart_login_002 is started")

        self.driver.get(self.login_url)
        self.log.info(f"Opening browser and getting {self.login_url}")


        lp=Login_Page_Class(self.driver)

        ## Enter Username
        self.log.info(f"Entering the Email {self.email}")
        lp.enter_email(self.email)

        # Enter Password
        self.log.info(f"Entering the password")
        lp.enter_password(self.password)

        # Click on Login button
        self.log.info(f"Clicking on login button")
        lp.click_login_register_button()

        self.log.info(f"Checking the login status")
        if lp.verify_menu_button_visibility()=="pass":
            self.log.info(f"User login successful and taking screenshot")
            self.driver.save_screenshot(".\\Screenshot\\test_credkart_login_002_pass.png")
            self.log.info(f"Clicking on menu button")
            lp.click_menu_button()
            self.log.info(f"Clicking on logout button")
            lp.click_logout_button()
        else:
            self.log.info(f"User login fail and taking screenshot")
            self.driver.save_screenshot(".\\Screenshot\\test_credkart_login_002_fail.png")
            assert False,"User Login Fail"
        self.log.info(f"Testcase test_Credkart_login_002 is completed")

    @pytest.mark.smoke
    @pytest.mark.flaky(reruns=2, reruns_delay=1)
    #@pytest.mark.dependency(depends=["test_credkart_registration"])
    #@pytest.mark.order(3)
    def test_credkart_registration(self):
        self.log.info("Testcase test_Credkart_login_002 is started")
        self.driver.get(self.register_url)
        self.log.info(f"Opening browser and getting {self.register_url}")

        fake_username=Faker().user_name()
        fake_email=Faker().email()
        password_data = "Credence_user_101@123"
        self.log.info(f"Generated fake data for username--> {fake_username} and email --> {fake_email}")
        print(f"fake_username--> {fake_username}")  # New
        print(f"fake_email--> {fake_email}")  # New

        rp=Registration_Page_class(self.driver)

        # Enter username
        self.log.info(f"Entering the Username--> {fake_username}")
        rp.enter_name(fake_username)

        # Enter Email
        self.log.info(f"Entering the Email--> {fake_email}")
        rp.enter_email(fake_email)

        # Enter Password
        self.log.info("Entering the Password")
        rp.enter_password(password_data)

        #Enter Confirm password
        self.log.info("Entering the Confirm Password")
        rp.enter_confirm_password(password_data)

        #click on register button
        self.log.info("Clicking on register button")
        rp.click_login_register_button()

        if rp.verify_menu_button_visibility()=="pass":
            self.log.info(f"User registration successful and taking screenshot")
            self.driver.save_screenshot(".\\Screenshot\\test_credkart_registration_003_pass.png")
            self.log.info(f"Clicking on menu button")
            rp.click_menu_button()
            self.log.info(f"Clicking on logout button")
            rp.click_logout_button()
        else:
            self.log.info(f"User registration fail and taking screenshot")
            self.driver.save_screenshot(".\\Screenshot\\test_credkart_registration_003_fail.png")
            assert False,"User Registration Fail"

