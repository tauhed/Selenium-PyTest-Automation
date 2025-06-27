import pytest
from pages.login_page import LoginPage
from data.test_data import TestData

@pytest.mark.usefixtures("init_driver")
class TestLogin:

    def test_valid_login(self):
        self.driver.get(TestData.BASE_URL)
        login_page = LoginPage(self.driver)
        login_page.login(TestData.USERNAME, TestData.PASSWORD)
        assert login_page.get_success_message() == "Login Successful"