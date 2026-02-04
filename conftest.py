import pytest
from selenium import webdriver



def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture(scope="class")
def browser_setup(request):
    browser=request.config.getoption("--browser")
    if browser=="chrome":
        print("\Opening Chrome Browser")
        chrome_options=webdriver.ChromeOptions()
        chrome_options.add_experimental_option("prefs",{"credentials_enable_service":False,
                                               "profile.password_manager_enabled": False,
                                                "profile.password_manager_leak_detection": False})

        driver=webdriver.Chrome(options=chrome_options)

    elif browser == "firefox":
        print("\nOpening firefox browser")
        driver = webdriver.Firefox()
    elif browser == "edge":
        print("\nOpening edge browser")
        driver = webdriver.Edge()
    elif browser == "headless":
        print("\nOpening chrome headless browser")
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--headless")
        driver = webdriver.Chrome(options=chrome_options)
    else:
        chrome_options = webdriver.ChromeOptions()
        # Create an "options" object for Chrome.
        # We use it to control Chrome settings before the browser launches.

        chrome_options.add_experimental_option("prefs", {
            "credentials_enable_service": False,
            # This turns OFF Chrome's "credentials service"
            # Chrome will not offer to save usernames/passwords.
            "profile.password_manager_enabled": False,
            # This turns OFF Chrome's built-in Password Manager feature.
            # Password Manager related popups (Save password / breach warning) will not come.
            "profile.password_manager_leak_detection":False
        }
                                               )
        driver = webdriver.Chrome(options=chrome_options)
        # Launch Chrome using the above options.
        # So Chrome starts with password manager disabled and those popups are avoided.
    driver.maximize_window()
    driver.implicitly_wait(5)
    request.cls.driver = driver  # attaching the driver to main class
    yield driver
    print("\nBrowser Closed")
    driver.quit()



def pytest_metadata(metadata):    #To add/remove  metadata to your report
    metadata["Project Name"]="CredKart Test Automation"
    metadata["Enviornment"]="QA Enviornment"
    metadata["Tester"]="Firoz"
    #To delete metadata
    del metadata["Platform"]

#To change summury in html report
def pytest_html_report_title(report):
    report.title = "CredKart Pytest Automation Report"


def pytest_html_results_summary(prefix, summary, postfix):
    prefix.extend([
        "<p><b>Project:</b> CredKart Test Automation</p>",
        "<p><b>Tester:</b> QA Team</p>",
        "<p><b>Execution Type:</b> Regression</p>",
        "<p><b>Epic Name:</b> User_Profile</p>",
        "<p><b>Stories Names:</b> url,login,registration</p>"
        "<p><b>Priority:</b> Blocker,Major</p>",
        "<p><b>Severity:</b> High</p>"
    ])


#Login Test Data through Parameters

@pytest.fixture(params=[
    ("Credencetest@test.com","Credence@123","login_pass"),#all correct
    ("Credencetest@test.com12x","Credence@123","login_fail"), #Incorrect Username Correct password
    ("Credencetest@test.com","Credence@123xxx","login_fail"), #Incorrect Username Correct password
    ("Credencetest@test.com12x","Credence@123xxx","login_fail") #Incorrect Username & password
])

def credkart_login_data(request):
    return request.param


