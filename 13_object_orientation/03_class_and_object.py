"""
類和對象
"""


# 設計一個鬧鐘類
class Clock:
    id = None  # 序列號
    price = None  # 價格

    # def ring(self):
        # import winsound  # only for windows
        # winsound.Beep(2000, 3000)


# 構建2個鬧鐘對象並讓其工作
clock1 = Clock()
clock1.id = "003032"
clock1.price = 19.99
print(f"鬧鐘ID：{clock1.id}，價格：{clock1.price}")
# clock1.ring()

clock2 = Clock()
clock2.id = "003033"
clock2.price = 21.99
print(f"鬧鐘ID：{clock2.id}，價格：{clock2.price}")
# clock2.ring()