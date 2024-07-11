"""
Socket客戶端
"""

import socket

# 創建Socket對象
socket_client = socket.socket()

# 連接到服務端
socket_client.connect(("localhost", 8888))

while True:
    # 發送消息
    msg = input("請輸入要給服務端發送的消息：")
    if msg == 'exit':
        break
    socket_client.send(msg.encode("UTF-8"))

    # 接收返回消息  1024是緩衝區大小，recv()方法是阻塞的
    recv_data = socket_client.recv(1024)
    print(f"服務端回覆的消息是：{recv_data.decode('UTF-8')}")

# 關閉連接
socket_client.close()