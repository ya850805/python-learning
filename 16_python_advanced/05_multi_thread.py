"""
多線程編程的使用
"""
import time
from threading import Thread


def sing(msg):
    while True:
        print(msg)
        time.sleep(1)


def dance(msg):
    while True:
        print(msg)
        time.sleep(1)


if __name__ == '__main__':
    # 創建一個唱歌的線程
    sing_thread = Thread(target=sing, args=('我在唱歌', ))
    # 創建一個跳舞的線程
    dance_thread = Thread(target=dance, kwargs={"msg": "我在跳舞"})

    # 啟動線程
    sing_thread.start()
    dance_thread.start()