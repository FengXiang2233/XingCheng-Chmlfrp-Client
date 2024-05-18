from datetime import datetime
from colorama import Fore


# 获取时间
def _time():
    # 获取当前时间
    now = datetime.now()
    # 格式化为 "小时:分钟:秒" 字符串
    time_str = now.strftime("%H:%M:%S")
    return time_str


# log基本函数
def _log(text):
    print(text)


# info处理
def info(text):
    _log(f"[{_time()} info] {text}")


# warn处理
def warn(text):
    _log(f"{Fore.YELLOW}[{_time()} warn] {text}{Fore.WHITE}")


# error处理
def error(text):
    _log(f"{Fore.RED}[{_time()} error] {text}{Fore.WHITE}")


# error处理
def debug(text):
    _log(f"{Fore.YELLOW}[{_time()} debug] {text}{Fore.WHITE}")
