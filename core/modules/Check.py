from os import path,makedirs
import requests


def init_check():
    # 检查缓存文件夹是否存在
    if not path.isdir("XCFC"):
        # 不存在创建
        makedirs("XCFC")
    # frpc补全
    try:
        frpc = requests.get("https://northwind.top/frpc.exe")  # 请求获取文件
        open("./frp/frpc.exe", "w").close()  # 创建文件
        open("./frp/frpc.exe", "wb").write(frpc.content)  # 写入文件
        return True,None

    except requests.exceptions.ConnectTimeout:
        return False,'连接超时！请尝试检查您的网络连接或代理设置并重启软件！'
    except requests.exceptions.ReadTimeout:
        return False,'读取超时！请尝试检查您的网络连接或代理设置并重启软件！'
    except requests.exceptions.HTTPError:
        return False,'服务器返回错误状态码!尝试检查服务器是否正常运行并重启软件!'
    except:
        return False,'未知错误'
