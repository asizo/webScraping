import os
import time
import traceback
from dotenv import load_dotenv

from module.integer import interval
from module.logger import Logger
from module.browser import Browser

# .env 파일 로드
load_dotenv()

# 로그 인스턴스 생성
logger: Logger = Logger()

# 실행 횟수
loopCnt = 1

# 이벤트 처리
def main(loopCnt) -> any:

    print('MAIN HANDLE START ( 실행 횟수 : {} )'.format(loopCnt))
    logger.write('info', 'MAIN HANDLE START ( 실행 횟수 : {} )'.format(loopCnt))
    
    try:

        # 브라우저 인스턴스 생성
        driver: Browser = Browser(os.environ.get('IS_SHOW_BROWSER'))

        # keyword 검색 ( 검색엔진에서 조회하는 키워드를 .env 파일에 불러온다. ( 배열 데이터타입으로 사용하기 위해 문자열에 , 를 구분 )
        for keyword in os.environ.get('KEYWORDS').split(', '):

            # 브라우저에서 검색엔진 실행
            driver.open(os.environ.get('NAVER_SITE_DOMAIN'))
            time.sleep(interval())

            logger.write('info', '지역 정보 검색 :: {}'.format(str(keyword)))

            # 검색엔진에서 keyword를 검색
            driver.elementSendKey(driver.findElementId("query"), keyword, True)
            time.sleep(interval())

            for i in range(1, 1 + 5):
                try:
                    # 검색하는 매장을 linkText 기준으로 조회한 후, 클릭 이벤트 진행
                    logger.write('info', '매장 엘리먼트 조회 :: {} 페이지'.format(str(i)))
                    driver.findElementLinkText(os.environ.get('SEARCH_STORE')).click()
                    logger.write('info', '매장 엘리먼트 클릭 완료 :: {} 페이지'.format(str(i)))
                    break
                except:
                    try:
                        # 조회하는 매장의 linkText 가 없는 경우, except 로 넘어와 다음 페이지를 클릭하여 다시 검색을 진행한다.
                        logger.write('info', '다음 페이지 조회')
                        driver.findElementCssSelector("a.spnew_bf.cmm_pg_next.on").click()
                        time.sleep(interval())
                        pass
                    except Exception as e:
                        # 다음 페이지가 없는 경우, 예외처리 에러 로그 저
                        message = str(i) + " 페이지 조회 불가" + "\n" + str(e) + "\n" + str(traceback.format_exc())
                        logger.write('error', '[FAIL] {}'.format(message))

            
        driver.quit()  # 모든 브라우저 닫기

    except Exception as e:
        message = " Next Page Error" + "\n" + str(e) + "\n" + str(traceback.format_exc())
        logger.write('error', '[FAIL] {}'.format(message))
        pass

    driver = None
    time.sleep(interval())
    logger.write('info', 'MAIN HANDLE QUIT')



##########################################################################################

logger.write('info', '==== daemon start =====')
while (1):
    main(loopCnt)
    time.sleep(interval())
    loopCnt += 1
