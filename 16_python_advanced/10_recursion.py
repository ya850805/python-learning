"""
遞歸
"""

import os


def test_os():
    print(os.listdir("test"))  # 列出路徑下的內容
    print(os.path.isdir("test/a"))  # 判斷指定路徑是不是文件夾
    print(os.path.exists("test"))  # 判斷指定路徑是否存在


def get_files_recursion_from_dir(path):
    """
    從指定的文件夾中使用遞歸的方式，獲取全部的文件夾
    :param path: 被判斷的文件夾
    :return: list，包含全部的文件，如果目錄不存在或者無文件就返回一個空list
    """
    file_list = []
    if os.path.exists(path):
        for f in os.listdir(path):
            new_path = path + "/" + f
            if os.path.isdir(new_path):  # 是文件夾
                file_list += get_files_recursion_from_dir(new_path)
            else:  # 是文件
                file_list.append(new_path)
    else:
        print(f"指定的目錄{path}不存在")
        return []
    return file_list


if __name__ == '__main__':
    # test_os()
    print(get_files_recursion_from_dir("test"))