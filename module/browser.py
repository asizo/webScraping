from str2bool import str2bool
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class Browser():

    driver: webdriver = dict()

    
    def __init__(self, isShowBrowser=False):
        """
        Browser 생성자
        :param self:
        :param isShowBrowser: 브라우저창을 띄어 처리 여부 ( True : 브라우저창을 띄움, False : headless 로 백단에서 처리 )
        :return:
        """

        chromedriver_version = "114.0.5735.16"
        options = webdriver.ChromeOptions()
        options.add_argument('--no-sandbox')
        options.add_argument("--disable-dev-shm-usage")
        options.add_experimental_option("excludeSwitches", ["enable-logging"])

        if bool(str2bool(isShowBrowser)) == False:
            print("headless mode")
            options.add_argument('--headless') # 헤드레스
            options.add_argument('--window-size=1890,1030') # 창 크기

        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options) # 크롬드라이버 위치

    def getDriver(self):
        """
        브라우저 인스턴스 리턴
        :return:
        """
        return self.driver

    def open(self, domain):
        """
        브라우저 실행
        :param domain:
        :return:
        """
        self.getDriver().get(domain)

    def findElementId(self, elementId):
        """
        html dom 에서 id 값을 조회하여 element 를 검색
        :param elementId: 찾고자 하는 elementID
        :return:
        """
        return self.getDriver().find_element(By.ID, elementId)

    def findElementLinkText(self, keyword):
        """
        html dom 에서 linkText 값을 조회하여 element 를 검색
        :param keyword:
        :return:
        """
        return self.getDriver().find_element(
            By.LINK_TEXT,
            keyword
        )

    def findElementCssSelector(self, selector):
        """
        html dom 에서 cssSelector 를 통해 element 를 검색
        :param selector:
        :return:
        """
        return self.getDriver().find_element(
            By.CSS_SELECTOR,
            selector
        )

    def elementSendKey(self, element, keyword, isEnter=False):
        """
        html dom 에서 element에 keyword를 입력
        :param element: element
        :param keyword: 입력 keyword 정보
        :param isEnter: 입력된 이후, enter 반영 여부
        :return:
        """
        element.send_keys(keyword)
        if isEnter == True:
            element.send_keys(Keys.ENTER)

    def quit(self):
        """
        모든 찾을 브라우저 찾을 닫는다.
        :return:
        """
        self.getDriver().quit()

    def __del__(self):
        """
        소멸자
        :return:
        """
        self.quit()
        self.driver = {}
