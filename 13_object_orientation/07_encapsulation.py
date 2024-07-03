"""
封裝
"""


# 定義一個類，內含私有成員變量和私有成員方法
class Phone:
    __current_voltage = 0.5  # 當前手機運行電壓

    def __keep_single_core(self):
        print("讓CPU以單核模式運行")

    def call_by_5g(self):
        if self.__current_voltage >= 1:
            print("5G通話已開啟")
        else:
            self.__keep_single_core()
            print("電量不足，無法使用5G通話，並已設置為單核進行省電")


phone = Phone()
# phone.__keep_single_core()  # 非法，該方法是私有的
# print(phone.__current_voltage)  # 非法，該變量是私有的

phone.call_by_5g()