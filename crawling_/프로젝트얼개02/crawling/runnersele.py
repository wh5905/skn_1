from helpers.db import MySQLDatabase
from helpers.db2 import *

# from helpers.ui import Ms
from helpers.crawling import 수집
from helpers.crawlingsele import User
import pandas as pd
from helpers.db2 import 테이블에레코드인서트할때

if __name__ == "__main__":

    # 버전 125.0.6422.113(공식 빌드) (64비트)
    # https://storage.googleapis.com/chrome-for-testing-public/125.0.6422.60/win64/chromedriver-win64.zip
    # https://storage.googleapis.com/chrome-for-testing-public/125.0.6422.113/win64/chromedriver-win64.zip

    user = User("n")
    user.페이지이동("https://www.danawa.com/")

    # 검색창인지
    # AKCSearch
    # //*[@id="AKCSearch"]
    user.객체선택값입히고('//*[@id="AKCSearch"]', "맥북")
    # //*[contains(concat( " ", @class, " " ), concat( " ", "search__submit", " " ))]
    user.일반딜레이()
    # 돋보기버튼누르기
    user.객체선택하고클릭(
        '//*[contains(concat( " ", @class, " " ), concat( " ", "search__submit", " " ))]'
    )
    user.일반딜레이()
    # //*[@id="saveDESC"]/a 인기상품순
    # //*[@id="opinionDESC"]/a 상품평많은순
    # //*[@id="dateDESC"]/a 신상품순
    # 상품평많은순누르기
    user.객체선택하고클릭('//*[@id="opinionDESC"]/a')
    user.일반딜레이(3)

    # 첫상품 선택은 되지만 이터안됨
    # //*[contains(concat( " ", @class, " " ), concat( " ", "click_log_product_standard_title_", " " ))]

    # 첫상품 이터됨
    # //*[@id="productItem12660491"]/div/div[2]/p/a
    # user.마우스이동하고클릭()
    user.객체선택하고클릭('//*[@id="productItem12660491"]/div/div[2]/p/a')
    user.일반딜레이(2)
    user.새창으로활성이동(1)
    # 쇼핑몰상품리뷰
    user.일반딜레이()
    # 안되면 페이지다운 다운
    user.객체선택하고클릭(
        '//*[(@id = "danawa-prodBlog-productOpinion-button-tab-companyReview")]//*[contains(concat( " ", @class, " " ), concat( " ", "txt", " " ))]'
    )
    # 첫번째리뷰타이틀

    상품명 = []
    리뷰타이틀 = []
    리뷰내용 = []
    별점 = []
    페이지넘 = []
    for i in range(0, 10):
        user.일반딜레이(2)
        for j in range(0, 9):
            상품명.append("맥북")
            try:
                리뷰타이틀.append(
                    user.객체선택하고객체의텍스트추출(
                        f'//*[@id="danawa-prodBlog-companyReview-content-wrap-0"]/div/div[{i+1}]/p'
                    )
                )
            except Exception as e:
                리뷰타이틀.append("리뷰타이안들어옴")
            try:
                리뷰내용.append(
                    user.객체선택하고객체의텍스트추출(
                        f'//*[@id="danawa-prodBlog-companyReview-content-wrap-0"]/div/div[{i+2}]'
                    )
                )
            except Exception as e:
                리뷰내용.append("리뷰내용안들어옴")
            try:
                별점.append(
                    user.객체선택하고객체의텍스트추출(
                        f'//*[@id="danawa-prodBlog-companyReview-content-list"]/ul/li[{i+1}]/div[]/span[{i+1}]'
                    )      
                )
            except Exception as e:
                별점.append("별점내용안들어옴")
        try:
            페이지넘.append(j + 1)
            # 다음페이징
            user.페이징(
                f"/html/body/div[2]/div[5]/div[2]/div[4]/div[4]/div/div[3]/div[2]/div[3]/div[2]/div[5]/div/div/div/a[{j+2}]"
            )   
        except Exception as e:
            print(f"문제있는 i j {i}  {j}")

    df = pd.DataFrame(
        data=zip(상품명, 리뷰타이틀, 리뷰내용, 별점, 페이지넘),
        columns=["상품명", "리뷰타이틀", "리뷰내용", "별점", "페이지넘"],
    )
    df.to_excel(
        r"C:\Users\USER\Desktop\workspace01\skn_1\crawling_\프로젝트얼개02\crawling\data\셀레니움다나와맥북상품후기.xlsx"
    )
    # 테이블에레코드인서트할때(
    #     r"C:\Users\USER\Desktop\workspace01\skn_1\crawling_\프로젝트얼개02\crawling\data\셀레니움다나와맥북상품후기.xlsx"
    # )


    import time

    time.sleep(5)
    # user.종료()

