from log.logg import Logger
from log.loggdbmysql import DatabaseHandler
import logging

if __name__ == "__main__":
    # logger = Logger("test.log")
    # logger.info("프로그램작동시작")
    
    # try:
    #     import asdf
    # except Exception as e:
    #     logger.error(e)


    # logger.info("프로그램작동종료")

    logger = logging.getLogger('testdb')     
    logger.setLevel(logging.DEBUG)              
    mysqlHandler = DatabaseHandler()           
    logger.addHandler(mysqlHandler)            

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    logger.debug("디버깅")         
    logger.info("잘됨")         
    logger.warning("경고")         
    logger.critical("심각")   