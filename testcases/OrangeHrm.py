import time

from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Test_num001():
    def test_001(self):
        driver=webdriver.Firefox()
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        wait=WebDriverWait(driver,10)
        wait.until(EC.presence_of_element_located((By.XPATH,"//img[@alt='company-branding']")))
        driver.find_element(By.XPATH,"//input[@placeholder='Username']").send_keys("Admin")
        driver.find_element(By.XPATH,"//input[@placeholder='Password']").send_keys("admin123")
        driver.find_element(By.XPATH,"//button[@type='submit']").click()
        try:
            time.sleep(2)
            driver.find_element(By.XPATH, "//span[@class='oxd-userdropdown-tab']")
            print("test_login_001 is Passed")
            driver.find_element(By.XPATH, "//span[@class='oxd-userdropdown-tab']").click()
            driver.find_element(By.XPATH, "//a[normalize-space()='Logout']").click()
            assert True
        except NoSuchElementException:
            print("test_login_001 is Failed")
            print("test_login_001 is completed")
            assert False
