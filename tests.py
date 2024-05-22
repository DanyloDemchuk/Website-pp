from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from Users.models import Member
from selenium.webdriver.support.select import Select


class TestForApp(LiveServerTestCase):

    def login(self):
        self.driver.get("{}{}".format(self.live_server_url, "/login/"))
        username = self.driver.find_element(By.NAME, "username")
        password = self.driver.find_element(By.NAME, "password")
        login_button = self.driver.find_element(By.CSS_SELECTOR, "input[type='submit'][value='Login']")
        username.send_keys(self.user.username)
        password.send_keys(self.password)
        login_button.click()

    def setUp(self):
        self.user = Member(first_name="Test", last_name="Test", username="Test", email="test@gmail.com",
                           password="1111")
        self.password = "1111"
        self.user.save()
        self.driver = webdriver.Chrome()

    def tearDown(self):
        self.driver.quit()

    def test_acces_not_logged_in(self):
        self.driver.get("{}{}".format(self.live_server_url, "/"))

        assert "User Login" in self.driver.title

    def test_login_valid_credentials(self):
        self.driver.get("{}{}".format(self.live_server_url, "/login/"))
        username = self.driver.find_element(By.NAME, "username")
        password = self.driver.find_element(By.NAME, "password")
        login = self.driver.find_element(By.CSS_SELECTOR, "input[type='submit'][value='Login']")

        username.send_keys(self.user.username)
        password.send_keys(self.password)
        login.click()

        assert "Our Company" in self.driver.title

    def test_login_invalid_credentials(self):
        self.driver.get("{}{}".format(self.live_server_url, "/login/"))
        username = self.driver.find_element(By.NAME, "username")
        password = self.driver.find_element(By.NAME, "password")
        login = self.driver.find_element(By.CSS_SELECTOR, "input[type='submit'][value='Login']")

        username.send_keys("invalidusername")
        password.send_keys("invalidpass")
        login.click()

        assert "Invalid email or password" in self.driver.page_source

    def test_logout(self):
        self.login()
        assert "Our Company" in self.driver.title

        logout = self.driver.find_element(By.CLASS_NAME, "logout-btn")
        logout.click()
        assert "User Login" in self.driver.title

    def test_go_to_usres_page_then_back_to_home_page(self):
        self.login()
        sleep(2)
        users = self.driver.find_element(By.CLASS_NAME, "users-btn")
        users.click()
        sleep(2)
        assert "Users List" in self.driver.title

        home = self.driver.find_element(By.CLASS_NAME, "home-btn")
        home.click()
        sleep(2)
        assert "Our Company" in self.driver.title

    def test_car_create(self):
        self.login()

        self.driver.get("{}{}".format(self.live_server_url, "/cars"))
        add = self.driver.find_element(By.CLASS_NAME, "add-btn")
        add.click()
        dropdown = Select(self.driver.find_element(By.NAME, "owner"))
        dropdown.select_by_visible_text("Test Test")
        plate = self.driver.find_element(By.NAME, "plate")
        car_name = self.driver.find_element(By.NAME, "car_name")
        max_speed = self.driver.find_element(By.NAME, "max_speed")
        plate.send_keys("BC 1234 BC")
        car_name.send_keys("KIA")
        max_speed.clear()
        max_speed.send_keys(150)
        add_save = self.driver.find_element(By.CSS_SELECTOR, "input[type='submit'][value='Add']")
        add_save.click()

        owner_table_sell = self.driver.find_element(By.CSS_SELECTOR,
                                                    "body > table > tbody > tr:nth-child(2) > td:nth-child(2)")
        plate_table_sell = self.driver.find_element(By.CSS_SELECTOR,
                                                    "body > table > tbody > tr:nth-child(2) > td:nth-child(3)")
        car_name_table_sell = self.driver.find_element(By.CSS_SELECTOR,
                                                       "body > table > tbody > tr:nth-child(2) > td:nth-child(4)")
        max_speed_table_sell = self.driver.find_element(By.CSS_SELECTOR,
                                                        "body > table > tbody > tr:nth-child(2) > td:nth-child(5)")

        assert "Test Test" == owner_table_sell.text
        assert "BC 1234 BC" == plate_table_sell.text
        assert "KIA" == car_name_table_sell.text
        assert "150" == max_speed_table_sell.text
