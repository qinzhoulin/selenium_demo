from selenium import webdriver
from time import sleep, ctime
import pytest
options = webdriver.ChromeOptions()
#chrome浏览器可执行文件的地址
options.binary_location = "C:/Users/Lenovo/AppData/Local/Google/Chrome/Application/chrome.exe"
#浏览器的驱动地址
chrome_driver_binary = "C:/Users/Lenovo/AppData/Local/Google/Chrome/Application/chromedriver.exe"
driver = webdriver.Chrome(chrome_driver_binary, chrome_options=options)
def setup_module():
    # 要测试的网页，打开网页
    driver.get("https://www.baidu.com/")
    sleep(3)
def teardown_function(): #每个不在类的用例执行后开始执行
    # 清除文本框
    try:
        driver.find_element_by_id("kw").clear()
        print('test pass: clean successful')
    except Exception as e:
        print("Exception found", format(e))
def test_one():
    # 找到id为“kw”的控件，输入测试文本Test Search
    driver.find_element_by_id("kw").send_keys("Test Search")
    # 找到id为“su”的控件，模拟鼠标点击
    driver.find_element_by_id("su").click()
    sleep(5)

def test_two():
    # 找到id为“kw”的控件，输入测试文本Test Search
    driver.find_element_by_id("kw").send_keys("电子科技大学成都学院教务系统")
    # 找到id为“su”的控件，模拟鼠标点击
    driver.find_element_by_id("su").click()
    sleep(5)
def test_three():
    # 找到id为“kw”的控件，输入测试文本Test Search
    driver.find_element_by_id("kw").send_keys("selenium")
    # 找到id为“su”的控件，模拟鼠标点击
    driver.find_element_by_id("su").click()
    sleep(5)
def teardown_module():
    # 退出
    driver.quit()