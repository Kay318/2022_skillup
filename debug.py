import builtins
import logging
import traceback
import atexit

# create formatter
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')


def set_info(var): 
    """
    프로그램의 정상 작동 중에 발생하는 이벤트 보고 (가령 상태 모니터링이나 결함 조사
    """
    logging.info(f': {var}')

def set_debug(var):
    """
    프로그램의 정상 작동 중에 발생하는 이벤트 보고 (가령 상태 모니터링이나 결함 조사
    """
    logging.debug(f': {var}')

# Try Exception
class Interupt(Exception):

    def __init__(self):

        self.msg = traceback.format_exc()

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
        logging.error(f': {self.msg}')

    @atexit.register
    def set_warn(self):
        """
        문제를 피할 수 있고 경고를 제거하기 위해 클라이언트 응용 프로그램이 수정되어야 하는 경우
        """
        logging.warn(f': {self.msg}')

    @atexit.register
    def set_warning(self):
        """
        클라이언트 응용 프로그램이 할 수 있는 일이 없는 상황이지만 이벤트를 계속 주목해야 하는 경우
        """
        logging.warning(f': {self.msg}')