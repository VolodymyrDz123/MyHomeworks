from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
import pytest


@pytest.fixture
def test_nav_button_learn_python():
    driver = webdriver.Chrome("chromedriver.exe")
    driver.get("https://www.w3schools.com/")
    tutorials_nav_button = driver.find_element(By.ID, "navbtn_tutorials")
    tutorials_nav_button.click()
    learn_python_nav_button = driver.find_element(By.XPATH, "//a[text()='Learn Python']")
    learn_python_nav_button.click()
    sleep(0.1)
    yield driver
    driver.close()


def test_learn_python_url(test_nav_button_learn_python):
    ulr_actual = test_nav_button_learn_python.current_url
    url_expected = "https://www.w3schools.com/python/default.asp"
    assert ulr_actual == url_expected


def test_learn_python_title(test_nav_button_learn_python):
    title_actual = test_nav_button_learn_python.title
    title_expected = "Python Tutorial"
    assert title_actual == title_expected


