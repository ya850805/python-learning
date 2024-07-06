"""
數據定義的類
"""


class Record:
    def __init__(self, date, order_id, money, province):
        self.date = date  # 訂單日期
        self.order_id = order_id  # 訂單ID
        self.money = money  # 訂單金額
        self.province = province  # 銷售省份

    def __str__(self):
        return f"{self.date}, {self.order_id}, {self.money}, {self.province}"