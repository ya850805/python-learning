"""
複寫父類成員
"""


class Phone:
    IMEI = None
    producer = "producer_A"

    def call_by_5g(self):
        print("使用5g網路進行通話")


class MyPhone(Phone):
    producer = "producer_B"  # 複寫父類的成員屬性

    def call_by_5g(self):
        print("開啟CPU單核模式，確保通話時省電")
        
        # 方式1
        # print(f"父類的廠商是：{Phone.producer}")
        # Phone.call_by_5g(self)
        
        # 方式2
        print(f"父類的廠商是：{super().producer}")
        super().call_by_5g()

        print("關閉CPU單核模式，確保性能")


phone = MyPhone()
phone.call_by_5g()
print(phone.producer)