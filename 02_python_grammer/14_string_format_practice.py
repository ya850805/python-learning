"""
字符串格式化練習題
"""

# 定義需要的變量
name = "company1"
stock_price = 19.99
stock_code = "003032"
stock_price_daily_growth_factor = 1.2
growth_days = 7

finally_stock_price = stock_price * (stock_price_daily_growth_factor ** growth_days)

print(f"公司：{name}, 股票代碼：{stock_code}, 當前股價：{stock_price}")
print("每日增長系數是：%.1f, 經過%d天的增長後, 股價達到了：%.2f" % (stock_price_daily_growth_factor, growth_days, finally_stock_price))
