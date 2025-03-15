import time
import pytest
from selenium.webdriver.common.by import By

from Pages.HomePage import HomePage
from test.BaseTest import BaseTest


class TestLogin(BaseTest):
    def test_login_with_valid_credentials(self):
        home_page = HomePage(self.driver)
        login_page = home_page.navigate_to_login_page()
        account_page = login_page.login_to_application("motooricap99@gmail.com","12345")
        assert account_page.display_status_of_edit_your_account_information_option()

    def test_login_without_entering_credentials(self):
        home_page = HomePage(self.driver)
        login_page = home_page.navigate_to_login_page()
        login_page.login_to_application("", "")
        expected_warning_message = "Warning: No match for E-Mail Address and/or Password."
        assert login_page.retrieve_warning_message().__contains__(expected_warning_message)

    def test_login_with_invalid_email_and_valid_password(self):
        home_page = HomePage(self.driver)
        login_page = home_page.navigate_to_login_page()
        login_page.login_to_application(self.generate_email_with_time_stamp(), "12345")
        expected_warning_message = "Warning: No match for E-Mail Address and/or Password."
        assert expected_warning_message in login_page.retrieve_warning_message()


    def test_login_with_valid_email_and_invalid_password(self):
        home_page = HomePage(self.driver)
        login_page = home_page.navigate_to_login_page()
        login_page.login_to_application("motooricap99@gmail.com", "12345ss")
        expected_warning_message = "Warning: No match for E-Mail Address and/or Password."
        assert expected_warning_message in login_page.retrieve_warning_message()
