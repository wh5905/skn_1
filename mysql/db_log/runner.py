import os
import logging
from log.logg import DBLogger
import logging

if __name__ == '__main__':
    
    # logger = Logger("test.log")
    # logger.info("프로그램 시작")
    # try:
    #     import asdf
    # except Exception as e:
    #     logger.error(e)
    # logger.info("프로그램 종료")

    logger = logging.getLogger("db_log")
    logger.setLevel(logging.DEBUG)
    dblogger = DBLogger()
    logger.addHandler(dblogger)
    logger.info("프로그램 시작")

    # dblogger.emit("프로그램 시작")
    try:
        import asdf
    except Exception as e:
        logger.debug(e)
    logger.info("프로그램 종료")





