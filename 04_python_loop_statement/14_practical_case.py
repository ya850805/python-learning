import random

balance = 10000

for i in range(1, 21):
    if balance == 0:
        print("工資發完了，下個月領取吧")
        break
    score = random.randint(1, 10)
    if score < 5:
        print(f"員工{i}，績效{score}分，不發工資，下一位")
        continue
    balance -= 1000
    print(f"向員工{i}發放工資1000元，帳戶餘額還剩餘{balance}元")
