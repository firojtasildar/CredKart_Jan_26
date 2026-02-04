import pytest

from pageObjects.Registration_Page import Registration_Page_class
from readConfig import ReadConfigClass
from utilities.Logger import log_generator_class
from utilities.XLUtils import Excel_Methods


@pytest.mark.usefixtures("browser_setup")
class Test_User_Profile:
    driver= None
    log = log_generator_class.log_gen_method()
    register_url = ReadConfigClass.get_data_for_register_url()
    excel_path=".\\Test_Data\\Credkart_Test_Data.xlsx"
    sheet_name = "register_data"

    @pytest.mark.smoke
    #@pytest.mark.flaky(reruns=2, reruns_delay=1)
    #@pytest.mark.dependency(depends=["test_credkart_registration"])
    #@pytest.mark.order(5)

    def file_test_credkart_registration_excel_ddt_005(self):


        self.rp=Registration_Page_class(self.driver) #rp object created

        #Reading data from Excel
        max_rows=Excel_Methods.get_rows_count(self.excel_path,self.sheet_name)

        result_list=[]

        for i in range(2,max_rows+1):
            self.driver.get(self.register_url)

            self.name=Excel_Methods.read_data_from_excel(self.excel_path,self.sheet_name,i,2)
            self.email = Excel_Methods.read_data_from_excel(self.excel_path, self.sheet_name, i, 3)
            self.password = Excel_Methods.read_data_from_excel(self.excel_path, self.sheet_name, i, 4)
            self.confirm_password = Excel_Methods.read_data_from_excel(self.excel_path, self.sheet_name, i, 5)
            self.expected_result = Excel_Methods.read_data_from_excel(self.excel_path, self.sheet_name, i, 6)

            #Enter name
            self.rp.enter_name(self.name)

            #Enter email
            self.rp.enter_email(self.email)

            #Enter Password
            self.rp.enter_password(self.password)

            #Enter confirm Password
            self.rp.enter_confirm_password(self.confirm_password)

            # click on login button
            self.rp.click_login_register_button()

            if self.rp.verify_menu_button_visibility()=="pass":
                # self.log.info("User Login Successful and taking screenshot")
                self.driver.save_screenshot(f".\\Screenshot\\user login successful-->{self.email} .png")

                #click on menu button
                self.rp.click_menu_button()

                #click on logout button
                self.rp.click_logout_button()

                actual_result="registration_pass"

                #writing data to excel sheet

                Excel_Methods.write_data_from_excel(self.excel_path,self.sheet_name,i,7,actual_result)


            else:
                #self.log.info("User Login failed and taking screenshot")
                self.driver.save_screenshot(f".\\Screenshot\\User login failed {self.email}.png")
                actual_result="login_fail"
                Excel_Methods.write_data_from_excel(self.excel_path,self.sheet_name,i,7,actual_result)

            if self.expected_result==actual_result:
                test_status="Pass"
                Excel_Methods.write_data_from_excel(self.excel_path,self.sheet_name,i,8,test_status)

            else:
                test_status="Fail"
                Excel_Methods.write_data_from_excel(self.excel_path,self.sheet_name,i,8,test_status)


            result_list.append(test_status)

            # if "Fail" not in result_list:
            #     self.log.info("All Testcases Passed")
            # else:
            #     #self.log.info("Some Testcases failed")
            #     assert False, "Some Testcases Failed"

        self.log.info("Testcase test_credkart_login_excel_ddt_003 completed")