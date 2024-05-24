from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import subprocess
from urllib.parse import quote_plus
import os

chrome_driver = r"C:\Users\USER\Downloads프록젝트얼개01\crawling\driver\chromedriver.exe"

class User:
    def __init__(self, mode = 'n'):
        # 작동시작
        # 작동중인 브라우저를 컨트롤 할건지
        # 새 브라우저를 컨트롤 할건지

        # self.options = webdriver.ChromeOptions()
        # browser = webdriver.Chrome(chrome_driver, options=self.option)
        # browser.get("https://www.naver.com"/)

        self.chrome_driver = chrome_driver
        self.chrome_options = Options()
        if mode == 'n':
            self.browser = webdriver.Chrome(options=self.chrome_options)
        cmd = [r"C:\Users\USER\Downloads프록젝트얼개01\crawling\driver\chromedriver.exe", r"--remote-debugging-port=9222", r"--user-data-dir=C:\chrometemp"]
        pro = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        pro.kill()
        self.chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
        # os.killpg(os.getpgid(pro.pid), signal.SIGTERM)

        self.browser = webdriver.Chrome(options=self.chrome_options)

        self.browser.maximize_window()


    def 페이지이동(self, page):
        self.browser.get(page)
    
    
    def 객체선택(self, User_xpath):
        return self.browser.find_element(By.XPATH, User_xpath)

    def 객체선택하고입히고(self, User_xpath):
        self.browser.find_element(By.XPATH, User_xpath).send_keys()
    
   
    def 객체선택하고클릭(self, User_xpath):
        self.browser.find_element(By.XPATH, User_xpath).click()
         
    def 돋보기버튼클릭(self, User_xpath):
        self.browser.find_element(By.CLASS_NAME, User_xpath).click()
    def 객체선택하고텍스트추출(self, User_xpath):
        self.browser.find_element(By.CLASS_NAME, User_xpath).click()
    
    def 페이징(self, user_full_xpath):
        self.browser.find_element(By.XPATH, user_full_xpath).click()

    def 일반딜레이(self, second=1):
        import time
        time.sleep(second)

    def 브라우저딜레이(self, second=1):
        self.browser.implicitly_wait(second)

    def 새창으로이동(self):
        self.browser.switch_to.window(self.browser.window_handles[1])
    
    def 마우스이동하고클릭(self, User_xpath):
        ac = ActionChains(self.browser)
        web_element = self.browser.find_element(By.XPATH, User_xpath)
        ac.click(web_element)
        ac.click()
        ac.perform()







    def 종료(self):
        self.browser.close()
        print("종료됨")

