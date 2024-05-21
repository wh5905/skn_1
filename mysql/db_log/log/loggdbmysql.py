import logging, sqlite3, datetime
import pymysql
import pymysql.cursors


class DatabaseHandler(logging.Handler):
    def __init__(self):
        logging.Handler.__init__(self)
        self.conn = pymysql.connect(
            user="encore", password="1234", host="localhost", database="logdb"
        )
        # cur = conn.cursor(pymysql.cursors.DictCursor)
        self.cur = self.conn.cursor(pymysql.cursors.DictCursor)

        # self.database = 'test.db'
        # self.conn = sqlite3.connect(self.database)
        # self.cur = self.conn.cursor()

        mk_table_query = """
            CREATE TABLE IF NOT EXISTS log (
                id INTEGER PRIMARY KEY AUTO_INCREMENT,
                insertTime TEXT,
                logLv TEXT,
                filename TEXT,
                lineno INTEGER,
                message TEXT
                )
        """
        self.cur.execute(mk_table_query)
        self.conn.commit()

    def time_format(self, record):
        self.now = datetime.datetime.now()
        record.nowstr = self.now.strftime("%Y-%m-%d %H:%M:%S")

    def emit(self, record):
        self.format(record)
        self.time_format(record)
        insert_db_query = """
            INSERT INTO log (
            insertTime, logLv, filename, lineno, message) VALUES
            ('{}', '{}', '{}', {}, '{}')
        """.format(
            record.nowstr,
            record.levelname,
            record.filename,
            record.lineno,
            record.message,
        )

        self.cur.execute(insert_db_query)
        self.conn.commit()

    def __del__(self):
        try:
            self.conn.close()
        except:
            pass