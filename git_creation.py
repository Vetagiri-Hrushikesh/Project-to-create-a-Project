import sys
import os
from selenium import webdriver

path = '/Users/mac/Desktop/Testing'
broswer = webdriver.Chrome()
broswer.get('http://github.com/login')
uname = "Vetagiri-Hrushikesh" #Add github user name here
pw = "qaTtuw-qunzy4-saxmaw" #add the password here

def git_creation(browser):
    folder_name = str(sys.argv[1])
    os.chdir(path)
    os.makedirs(folder_name)
    browser.find_elements_by_xpath("//input[@name='login']")[0].send_keys(uname)
    browser.find_elements_by_xpath("//input[@name='password']")[0].send_keys(pw)
    browser.find_elements_by_xpath("//input[@name='commit']")[0].click()
    browser.get('https://github.com/new')
    browser.find_element_by_xpath('//*[@id="repository_name"]').send_keys(folder_name)
    browser.find_element_by_css_selector('button.first-in-line').submit()
    browser.quit()
    
if __name__ == "__main__":
    git_creation(broswer)