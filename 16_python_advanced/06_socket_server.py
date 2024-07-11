"""
socket服務端
"""

import socket

# 創建Socket對象
socket_server = socket.socket()

# 綁定IP地址與端口
socket_server.bind(("localhost", 8888))

# 監聽端口
socket_server.listen(1)  # listen()方法內接收一個整數參數，表示接受的連接數量

# 等待客戶端連接
# accept()方法返回二元元組 (客戶端和服務端的連接對象, 客戶端的地址信息)
# accept()方法阻塞的方法，等待客戶端的連接，如果沒有連接，就卡在這一行不向下執行了
conn, address = socket_server.accept()

print(f"接收到了客戶端的連接，客戶端的信息是：{address}")

while True:
    # 接受客戶端信息，要使用客戶端和服務端的本次連接對象，而非socket_server對象
    # recv()接收的參數是緩衝區大小，一般給1024即可
    # recv()方法的返回值是一個字節數組也就是byte對象，不是字符串，可以通過decode方法通過UTF-8編碼，將字符串轉為字符串對象
    data: str = conn.recv(1024).decode("UTF-8")
    print(f"客戶端發來的消息：{data}")

    # 發送回復消息 encode可以把字符串編碼為字節數組對象
    msg = input("請輸入你要和客戶端回覆的消息：")
    if msg == 'exit':
        break
    conn.send(msg.encode("UTF-8"))

# 關閉連接
conn.close()
socket_server.close()