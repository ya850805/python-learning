"""
練習題：設計帶有私有成員的手機
"""


class Phone:
    __is_5g_enable = True

    def __check_5g(self):
        if self.__is_5g_enable:
            print("5g開啟")
        else:
            print("5g關閉，使用4g網路")

    def call_by_5g(self):
        self.__check_5g()
        print("正在通話中")


phone = Phone()
phone.call_by_5g()