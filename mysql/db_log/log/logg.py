import os
import logging

class Logger:
    def __init__(self, file):
        self.logger = logging.getLogger("파일로그")
        self.file_name = os.path.basename(file)

        if len(self.logger.handlers) == 0:
            formatter = logging.Formatter(u'%(asctime)s [%(levelname)s] %(message)s')
            stream_handler = logging.FileHandler(self.file_name, encoding="utf-8")
            stream_handler.setFormatter(formatter)

            self.logger.addHandler(stream_handler)
            self.logger.setLevel(logging.INFO)

    def info(self, value):
        self.logger.info("%s (at %s)" % (str(value), self.file_name))

    def error(self, value):
        self.logger.error("%s (at %s)" % (str(value), self.file_name))
