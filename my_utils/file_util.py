"""
文件處理相關工具模塊
"""


def print_file_info(file_name):
    """
    將給定路徑的文件內容輸出到控制台中
    :param file_name: 即將讀取的文件路徑
    :return: None
    """
    f = None
    try:
        f = open(file_name, "r", encoding="UTF-8")
        content = f.read()
        print("文件的全部內容如下：")
        print(content)
    except Exception as e:
        print(f"程序出現異常了，原因是：{e}")
    finally:
        if f:  # 如果變量是None表示False，如果有任何內容就是True
            f.close()


def append_to_file(file_name, data):
    """
    將指定的數據追加到指定的文件中
    :param file_name: 指定的文件路徑
    :param data: 指定的數據
    :return:
    """
    f = open(file_name, "a", encoding="UTF-8")  # 文件不存在會創建
    f.write(data)
    f.write("\n")
    f.close()


if __name__ == '__main__':
    print_file_info("../09_python_error_module_package/1.txt")
    append_to_file("../09_python_error_module_package/2.txt", "Hello!!!")