import pytest
from faker import Faker

from conftest import browser_setup
from pageObjects.Login_Page import Login_Page_Class
from pageObjects.Registration_Page import Registration_Page_class
from readConfig import ReadConfigClass
from utilities.Logger import log_generator_class
from utilities.XLUtils import Excel_Methods


@pytest.mark.usefixtures("browser_setup")
class Test_User_Profile :
    driver=None
    email=ReadConfigClass.get_data_for_email()
    password=ReadConfigClass.get_data_for_password()
    login_url=ReadConfigClass.get_data_for_login_url()
    register_url=ReadConfigClass.get_data_for_register_url()
    homepage_url=ReadConfigClass.get_data_for_homepage_url()
    log=log_generator_class.log_gen_method()
    excel_path=".\\Test_Data\\Credkart_Test_Data.xlsx"
    sheet_name="login_data"



    @pytest.mark.smoke
    @pytest.mark.flaky(reruns=2,reruns_delay=1)
    #@pytest.mark.dependency(depends=["test_credkart_registration"])
    #@pytest.mark.order(4)
    def test_credkart_login_excel_ddt_003(self):
        self.log.info("Testcase test_Credkart_login_002 is started")
        lp = Login_Page_Class(self.driver)  # object created
        self.log.info("Reading Data from Excel")
        max_rows = Excel_Methods.get_rows_count(self.excel_path, self.sheet_name)
        self.log.info(f"Number of rows in excel are-->{max_rows}")

        result_list=[]
        for i in range(2,max_rows+1):

            self.driver.get(self.login_url)
            self.log.info(f"Opening browser and getting url-->{self.login_url}")

            email=Excel_Methods.read_data_from_excel(self.excel_path,self.sheet_name,i,2)
            password=Excel_Methods.read_data_from_excel(self.excel_path,self.sheet_name,i,3)
            expected_result=Excel_Methods.read_data_from_excel(self.excel_path,self.sheet_name,i,4)

            #Enter email
            lp.enter_email(email)

            #Enter Password
            lp.enter_password(password)

            #click on login button
            lp.click_login_register_button()

            if lp.verify_menu_button_visibility()=="pass":
                self.log.info("User Login Successful and taking screenshot")
                self.driver.save_screenshot(f".\\Screenshot\\user login successful-->{self.email} .png")

                #click on menu button
                lp.click_menu_button()

                #click on logout button
                lp.click_logout_button()

                actual_result="login_pass"

                #writing data to excel sheet

                Excel_Methods.write_data_from_excel(self.excel_path,self.sheet_name,i,5,actual_result)

            else:
                self.log.info("User Login failed and taking screenshot")
                self.driver.save_screenshot(f".\\Screenshot\\User login failed {self.email} .png")
                actual_result="login_fail"
                Excel_Methods.write_data_from_excel(self.excel_path,self.sheet_name,i,5,actual_result)


            if expected_result==actual_result:
                test_status="Pass"
                Excel_Methods.write_data_from_excel(self.excel_path,self.sheet_name,i,6,test_status)

            else:
                test_status="Fail"
                Excel_Methods.write_data_from_excel(self.excel_path,self.sheet_name,i,6,test_status)

            result_list.append(test_status)

        print(f"result_list-->{result_list}")

        if "Fail" not in result_list:
            self.log.info("All Testcases Passed")
        else:
            self.log.info("Some Testcases failed")
            assert False,"Some Testcases Failed"

        self.log.info("Testcase test_credkart_login_excel_ddt_003 completed")







    