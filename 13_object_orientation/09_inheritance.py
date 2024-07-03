"""
繼承
"""


# 單繼承
class Phone:
    IMEI = None  # 序列號
    producer = "PHONE-P1"  # 廠商

    def call_by_4g(self):
        print("4g通話")


class Phone2024(Phone):
    face_id = "10001"  # 面部識別ID

    def call_by_5g(self):
        print("5g通話")


phone = Phone2024()
print(phone.producer)
phone.call_by_4g()
phone.call_by_5g()


# 多繼承
class NFCReader:
    nfc_type = "第5代"
    producer = "NFC-P1"

    def read_card(self):
        print("NFC讀卡")

    def write_card(self):
        print("NFC寫卡")


class RemoteControl:
    rc_type = "紅外線遙控"

    def control(self):
        print("紅外線遙控開啟了")


class MyPhone(Phone, NFCReader, RemoteControl):
    pass  # 語法補全，該類沒有其他新的功能，只有繼承過來的功能


phone = MyPhone()
phone.call_by_4g()
phone.read_card()
phone.write_card()
phone.control()

print(phone.producer)  # 使用同名屬性時(Phone和NFCReader都有這個屬性)，按照誰先繼承誰的優先級高(左側先)