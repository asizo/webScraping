import logging
from logging.handlers import TimedRotatingFileHandler
from logging import Formatter


class Logger():
    """
    로그 클래스
    """

    logger: dict()

    def __init__(self, fileName='run.log'):

        self.logger = logging.getLogger(__name__)
        # create handler
        handler = TimedRotatingFileHandler(
            filename=fileName,
            when='D',
            interval=1,
            backupCount=5,
            encoding='utf-8',
            delay=False)
        # create formatter and add to handler
        formatter = Formatter(fmt='[%(asctime)s|%(levelname)s|%(funcName)s|%(lineno)d] %(message)s')
        handler.setFormatter(formatter)
        # add the handler to named logger
        self.logger.addHandler(handler)
        # set the logging level
        self.logger.setLevel(logging.INFO)

    def getLogger(self):
        return self.logger

    def write(self, type, message):
        """
        로그 쓰기
        :param type: 현재 info, error 만 사용
        :param message: 로그 내역
        :return:
        """
        if type == 'info':
            self.getLogger().info(message)
        elif type == 'error':
            self.getLogger().error(message)
