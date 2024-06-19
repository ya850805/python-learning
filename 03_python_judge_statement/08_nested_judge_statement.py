"""
判斷語句的嵌套
"""

# if int(input("你的身高是多少：")) > 120:
#     print("身高超出限制，不可以免費")
#     print("但是如果VIP級別大於3，可以免費")
#
#     if int(input("你的VIP級別是多少：")) > 3:
#         print("恭喜你，VIP級別達標，可以免費")
#     else:
#         print("Sorry 你需要買票10元")
# else:
#     print("歡迎免費遊玩")

#############################################################

age = 11
year = 1
level = 1

if age >= 18:
    print("你是成年人")
    if age < 30:
        print("你的年齡達標了")
        if year > 2:
            print("恭喜你，年齡和入職時間都達標，可以領取禮物")
        elif level > 3:
            print("恭喜你，年齡和級別都達標，可以領取禮物")
        else:
            print("不好意思，儘管年齡達標，但是入職時間和級別都不達標")
    else:
        print("不好意思，年齡太大了")
else:
    print("不好意思，年齡太小了")