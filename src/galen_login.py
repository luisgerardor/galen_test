from selenium import webdriver
import unittest
import time


class LoginGalen(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.username = "testuser@example.com"
        cls.password = "test123"
        cls.username_nok = "testusers"
        cls.password_nok = "test"
        cls.driver = webdriver.Chrome(executable_path="..\\web_drivers\\chromedriver.exe")
        cls.driver.maximize_window()

    def test_galen_app_login_ok(self):
        self.driver.get("http://testapp.galenframework.com/")
        self.driver.find_element_by_xpath('//*[@id="welcome-page"]/p[3]/button').click()
        self.driver.find_element_by_name("login.username").is_displayed()
        self.driver.find_element_by_name("login.username").is_displayed()
        self.driver.find_element_by_name("login.username").send_keys(self.username)
        self.driver.find_element_by_name("login.password").send_keys(self.password)
        self.driver.find_element_by_xpath('//*[@id="login-page"]/p[3]/button[1]').click()

    def test_galen_app_login_username_nok(self):
        self.driver.get("http://testapp.galenframework.com/")
        self.driver.find_element_by_xpath('//*[@id="welcome-page"]/p[3]/button').click()
        self.driver.find_element_by_name("login.username").is_displayed()
        self.driver.find_element_by_name("login.username").is_displayed()
        self.driver.find_element_by_name("login.username").send_keys(self.username_nok)
        self.driver.find_element_by_name("login.password").send_keys(self.password)
        self.driver.find_element_by_xpath('//*[@id="login-page"]/p[3]/button[1]').click()
        self.driver.find_element_by_id("login-error-message").is_displayed()

    def test_galen_app_login_password_nok(self):
        self.driver.get("http://testapp.galenframework.com/")
        self.driver.find_element_by_xpath('//*[@id="welcome-page"]/p[3]/button').click()
        self.driver.find_element_by_name("login.username").is_displayed()
        self.driver.find_element_by_name("login.username").is_displayed()
        self.driver.find_element_by_name("login.username").send_keys(self.username)
        self.driver.find_element_by_name("login.password").send_keys(self.password_nok)
        self.driver.find_element_by_xpath('//*[@id="login-page"]/p[3]/button[1]').click()
        self.driver.find_element_by_id("login-error-message").is_displayed()

    def test_galen_app_login_password_empty(self):
        self.driver.get("http://testapp.galenframework.com/")
        self.driver.find_element_by_xpath('//*[@id="welcome-page"]/p[3]/button').click()
        self.driver.find_element_by_name("login.username").is_displayed()
        self.driver.find_element_by_name("login.username").is_displayed()
        self.driver.find_element_by_name("login.username").send_keys(self.username)
        self.driver.find_element_by_xpath('//*[@id="login-page"]/p[3]/button[1]').click()
        self.driver.find_element_by_id("login-error-message").is_displayed()

    def test_galen_app_login_username_and_password_empty(self):
        self.driver.get("http://testapp.galenframework.com/")
        self.driver.find_element_by_xpath('//*[@id="welcome-page"]/p[3]/button').click()
        self.driver.find_element_by_name("login.username").is_displayed()
        self.driver.find_element_by_name("login.username").is_displayed()
        self.driver.find_element_by_xpath('//*[@id="login-page"]/p[3]/button[1]').click()
        self.driver.find_element_by_id("login-error-message").is_displayed()

    @classmethod
    def tearDown(cls):
        time.sleep(2)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("End of Test")


if __name__ == '__main__':
    unittest.main()
