# https://www.youtube.com/watch?v=UenvOvag0B4
# 셀레니움(Selenium)을 활용해 네이버 자동 로그인 및 메일 정보 가져오기 - 동빈나

# 자동화 테스트를 위해 셀레니옴(Selenium)을 불러옵니다.
from time import sleep

# pip install selenium
from selenium import webdriver

# 크롬 웹 드라이버의 경로를 설정합니다.
driver = webdriver.Chrome('C:/Users/tpwls/PycharmProjects/mail_in_naver/chromedriver.exe')

# 크롬을 통해 네이버 로그인 화면에 접속
driver.get('https://nid.naver.com/nidlogin.login')

# 아이디와 비밀번호를 입력합니다. ( 0.5초씩 기다리기 )
sleep(0.5)
driver.find_element_by_name('id').send_keys('ID')
sleep(0.5)
driver.find_element_by_name('pw').send_keys('PASSWORD')

# XPath를 이용해 로그인을 시도합니다.
driver.find_element_by_xpath('//*[@id="frmNIDLogin"]/fieldset/input').click()

# 자동방지문자 입력 후, 로그인 완료 후 ENTER
input("ENTER IN 4: Run")

# pip install beautifulsoup4
# 웹 페이지의 소스코드를 파싱하기 위해 Beautiful Soup 라이브러리를 불러옵니다.
from bs4 import BeautifulSoup
driver.get("https://mail.naver.com/")
html = driver.page_source
soup = BeautifulSoup(html,'lxml') # pip install lxml

# 메일 제목을 하나씩 파싱합니다.
title_list = soup.find_all('strong','mail_title')

# 모든 메일 제목을 출력합니다.
for title in title_list:
    print(title.text)
