import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


class Testnew():
    def test_kill(self):
        a = 89
        b = 76
        multi = a * b
        if multi >= 500:
            print('yes')
            assert True
        else:
            assert False

class Test_case001():
    def test_01(self):
        driver=webdriver.Firefox()
        driver.get("https://www.google.co.in/")
        logo = driver.find_element(By.XPATH,"//img[@alt='Google']").is_displayed()
        print(logo)
        if logo == True:
            assert True
        else:
            assert False