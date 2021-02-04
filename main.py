from selenium import webdriver
from selenium.webdriver.chrome.options import Options


if __name__=='__main__':
    options=Options()
    options.add_argument('--headless')
    driver=webdriver.Chrome('/usr/bin/chromedriver',options=options)
    driver.get('https://ww.google.co.jp/')
    print(driver.page_source)