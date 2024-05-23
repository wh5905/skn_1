from helpers.db import MySQLDatabase
# from helpers.ui import UI
from helpers.crawling_1 import crawling_newera as cn
from helpers.db2 import *

if __name__ == "__main__":
    # 01스트림릿

    # 02수집
    cn() 
    #03 DB에 저장
    try:
        user = "root"
        password = ""
        host = "localhost"
        port = 3306
        db = "test"

        db_url = f"mysql+pymysql://{user}:{password}@{host}:{port}/{db}"
        db = MySQLDatabase(db_url)
        print(db.__repr__)

        import sys
        sys.exit()
        db.to_sql()


        # db.add_user("john_doe", "john@example.com")
        # user =  db.get_user_by_username("john_doe")
        # print(user.username, user.email)
        # db.update_user_email("john_doe", "new_email@example.com")
        # user =  db.get_user_by_username("john_doe")
        # print(user.username, user.email)

        # db.delete_user("john_doe")

    except Exception as e:
        print("DB부분처리안됨")    
        print("e")


if __name__ == "__main__":
    

