import pytest

from pageObjects.Login_Page import Login_Page_Class
from readConfig import ReadConfigClass
from utilities.Logger import log_generator_class

class Test_User_Login_By_Parameters:
    driver=None

    log=log_generator_class.log_gen_method()
    login_url = ReadConfigClass.get_data_for_login_url()

    @pytest.mark.sanity
    @pytest.mark.regression
    @pytest.mark.web
    @pytest.mark.parameters
    @pytest.mark.usefixtures("browser_setup")
    def test_credkart_login_params_004(self,credkart_login_data):
        self.email_id = credkart_login_data[0]
        self.password_data = credkart_login_data[1]
        self.expected_result = credkart_login_data[2]

        #Empty result list
        result_list=[]


        self.log.info(f"email_id-->{self.email_id}")
        self.log.info(f"password_data-->{self.password_data}")
        self.log.info(f"expected_result-->{self.expected_result}")

        #Opening Browser and opening url
        self.log.info(f"opening login_url-->{self.login_url}")
        self.driver.get("https://automation.credence.in/login")


        self.lp=Login_Page_Class(self.driver)  #  #login page class's object creation

        if self.driver.title=="CredKart":
            self.log.info(f"You're Landed on correct Page and its title is-->{self.driver.title}")

            #Enter Username
            self.lp.enter_email(self.email_id)

            #Enter Password
            self.lp.enter_password(self.password_data)

            #click on login button
            self.lp.click_login_register_button()

            if self.lp.verify_menu_button_visibility()=="pass":
                self.log.info("User Login Successful and Taking Screenshot")
                self.driver.save_screenshot(f".\\Screenshot\\user_login_successful_{self.email_id}.png")

                # click on menu button
                self.lp.click_menu_button()

                # click on logout button
                self.lp.click_logout_button()

                self.actual_result = "login_pass"


            else:
                self.log.info("User Login failed and taking screenshot")
                self.driver.save_screenshot(f".\\Screenshot\\User login failed {self.email_id} .png")
                self.actual_result = "login_fail"

            if self.actual_result == self.expected_result:
                test_status = "Pass"
                print("Testcase Pass")
                assert True
            else:
                print("Testcase Fail")
                test_status = "Fail"
                assert False

            result_list.append(test_status)

            print(f"result_list-->{result_list}")

            if "Fail" not in result_list:
                self.log.info("All Testcases Passed")
            else:
                self.log.info("Some Testcases failed")
                assert False, "Some Testcases Failed"

            self.log.info("Testcase test_credkart_login_excel_ddt_003 completed")



        else:
            print(f" You are landed on wrong page and its title is {self.driver.title}")









