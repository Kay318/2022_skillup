from functools import wraps
from Log import LogManager

def AutomationFunctionDecorator(func):
    @wraps(func)
    def wrapper(self, *args):
        LogManager.HLOG.info(f"{func.__module__} : {func.__name__} 실행 시작")
        LogManager.HLOG.info(f"Parameter : {', '.join([str(arg) for arg in args])}")

        try:
            if False in args:
                args = ()
            func(self, *args)
            LogManager.HLOG.info(f"{func.__module__} : {func.__name__} 실행 종료")
        except Exception:
            LogManager.Interupt()

    return wrapper