from helpers.db import MySQLDatabase
from helpers.db2 import *
# from helpers.ui import Ms
# from helpers.crawling import 수집
from helpers.crawlingsele import User
import pandas as pd
# 125.0.6422.113(공식 빌드) (64비트)

if __name__ == "__main__":
    # 125.0.6422.113(공식 빌드) (64비트)

    user = User("n")
    user.페이지이동(r"https://www.danawa.com/")
    
    # 검색창인지
    #AKCSearch
    user.객체선택하고입히고('//*[@id="AKCSearch"]', '맥북')
    
    user.일반딜레이(3)  
    #//*[contains(concat( " ", @class, " " ), concat( " ", "search__submit", " " ))]
    user.객체선택하고클릭('//*[contains(concat( " ", @class, " " ), concat( " ", "search__submit", " " ))]')
    user.일반딜레이(3)
    # //*[@id="opinionDESC"]/a 싱품평많은순
    # //*[@id="saveDESC"]/a 인기상품순
    # //*[@id="dateDESC"]/a 신상품순
    user.객체선택하고클릭('//*[@id="opinionDESC"]/a')

    # //*[@id="productItem12660491"]/div/div[2]/p/a 첫상품선택
    # user.마우스이동하고클릭()

    user.객체선택하고클릭('//*[@id="productItem12660491"]/div/div[2]/p/a')
    user.일반딜레이(3)
    user.새창으로이동(2)
    user.일반딜레이()
    # 쇼핑몰상품리뷰
    #  //*[contains(concat( " ", @class, " " ), concat( " ", "txt", " " ))]
    user.객체선택하고클릭('//*[@id="danawa-prodBlog-companyReview-button-tab-companyReview"]/h4')
    
    # 쇼핑몰상품리뷰 첫번째
    # //*[@id="danawa-prodBlog-companyReview-content-wrap-0"]/div/div[2]
    상품명 = []
    리뷰타이틀 =[]
    리뷰내용=[]
    별점= []
    페이지넘 = []
    for i in range(0, 100):
        user.일반딜레이(3)
        for j in range(0, 9):
            try:
                상품명.append('맥북')
            except Exception as e:
                 print(f"상품명 추가 오류: {e}")

            try:
                리뷰타이틀.append(user.객체선택하고텍스트추출(f'//*[@id="danawa-prodBlog-companyReview-content-wrap-0"]/div/div[{i+1}]/p'))
            except Exception as e:
                print(f"리뷰타이틀 추가 오류: {e}")

            try:
                리뷰내용.append(user.객체선택하고텍스트추출(f'//*[@id="danawa-prodBlog-companyReview-content-wrap-0"]/div/div[{i+2}]'))
            except Exception as e:
                 print(f"리뷰내용 추가 오류: {e}")

            try:
                 별점.append(user.객체선택하고텍스트추출(f'//*[@id="danawa-prodBlog-companyReview-content-list"]/ul/li[1]/div[{i+1}]/span[1]'))
            except Exception as e:
                print(f"별점 추가 오류: {e}")
            페이지넘.append(j+1)
            user.페이징(f'/html/body/div[2]/div[5]/div[2]/div[4]/div[4]/div/div[3]/div[2]/div[3]/div[2]/div[5]/div/div/div/a[{j+1}]')



            # 상품명.append('맥북')
            # 리뷰타이틀.append(user.객체선택하고텍스트추출(f'//*[@id="danawa-prodBlog-companyReview-content-wrap-0"]/div/div[{i+1}]/p'))
            # 리뷰내용.append(user.객체선택하고텍스트추출(f'//*[@id="danawa-prodBlog-companyReview-content-wrap-0"]/div/div[{i+2}]') )
            # 별점.append(user.객체선택하고텍스트추출(f'//*[@id="danawa-prodBlog-companyReview-content-list"]/ul/li[1]/div[{i+1}]/span[1]'))
            # 다음페이지클릭 
            # /html/body/div[2]/div[5]/div[2]/div[4]/div[4]/div/div[3]/div[2]/div[3]/div[2]/div[5]/div/div/div/span
            # /html/body/div[2]/div[5]/div[2]/div[4]/div[4]/div/div[3]/div[2]/div[3]/div[2]/div[5]/div/div/div/a[1]

    df = pd.DataFrame(data=zip(상품명, 리뷰타이틀, 리뷰내용, 별점, 페이지넘), columns=['상품명', '리뷰타이틀', '리뷰내용', '별점', '페이지넘'])
    df.to_excel('C:\Users\USER\Desktop\workspace01\skn_1\crawling_\프록젝트얼개01\crawling\data\셀레니움다나와맥북m1리뷰.xlsx')
   
   
    # user.종료()





