import builtins
import logging
import traceback
import atexit
import os
from pathlib import Path
from datetime import datetime

def Init():
    __init_timestamp()
    __init_logger()
    HLOG.debug("LogManager Init function called !!!")

def __init_timestamp():
        """ 타임스탬프 초기화
        """
        global _TIMESTAMP
    
        _TIMESTAMP = datetime.now().strftime(f"%Y%m%d-%H%M%S")

def getTimeStamp() -> str:
    """ 시작 타임스탬프 반환

    Returns:
        str: 타임스탬프
    """
    return _TIMESTAMP

def __init_logger():
    """ 로거 초기화
    """
    
    global HLOG

    # Log 출력용 설정
    logger = logging.getLogger('DATA_LOG')
    formatter = logging.Formatter('[%(asctime)s.%(msecs)03d][%(levelname).1s][%(filename)s(%(funcName)s):%(lineno)d] %(message)s',
                datefmt='%Y-%m-%d %H:%M:%S')
    streamHandler = logging.StreamHandler()
    streamHandler.setFormatter(formatter)
    logger.addHandler(streamHandler)
    logfile = f"{getTimeStamp()}.log" # 저장할 로그 이름
    # logpath = f"{Path(__file__).parents[1]}\\log\\kraken" # 저장할 로그 경로
    logpath =  f"{Path(__file__).parent}\\log_files" # 저장할 로그 경로

    if os.path.isdir(logpath) != True:
        os.makedirs(logpath)

    fileHandler = logging.FileHandler(logpath + '\\' + logfile, encoding='utf-8')
    fileHandler.setFormatter(formatter)
    fileHandler.setLevel(logging.DEBUG)
    logger.addHandler(fileHandler)
    logger.propagate = False # 로그가 중복되어 출력되는 것을 방지하기 위함.

    HLOG = logger
    HLOG.setLevel(logging.DEBUG)

# Try Exception
class Interupt(Exception):

    @atexit.register
    def __init__(self):

        self.msg = traceback.format_exc()
        print(self.msg)

        if self.msg.count("RuntimeError") != 0:
            self.set_error()
        elif self.msg.count("RuntimeWarning") != 0:
            self.set_warning()
        else:
            self.set_warn()

    @atexit.register
    def set_error(self):
        """
        예외를 발생시키지 않고 에러의 억제를 보고 (가령 장기 실행 서버 프로세스의 에러 처리기)
        """
        HLOG.error(f': {self.msg}')

    @atexit.register
    def set_warn(self):
        """
        문제를 피할 수 있고 경고를 제거하기 위해 클라이언트 응용 프로그램이 수정되어야 하는 경우
        """
        HLOG.warn(f': {self.msg}')

    @atexit.register
    def set_warning(self):
        """
        클라이언트 응용 프로그램이 할 수 있는 일이 없는 상황이지만 이벤트를 계속 주목해야 하는 경우
        """
        HLOG.warning(f': {self.msg}')