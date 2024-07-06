"""
文件相關的類定義
"""
import json

from data_define import Record


# 定義一個抽象類，用來做頂層設計，確定有哪些功能需要實現
class FileReader:
    def read_data(self) -> list[Record]:
        """讀取文件的數據，讀到的每一條數據都轉換為Record對象，將他們都封裝到list內返回即可"""
        pass


class TextFileReader(FileReader):
    def __init__(self, path):
        self.path = path  # 定義成員變量，紀錄文件的路徑

    # 實現父類的方法
    def read_data(self) -> list[Record]:
        f = open(self.path, "r", encoding="UTF-8")
        record_list: list[Record] = []
        for line in f.readlines():
            line = line.strip()  # 消除讀取到的每一行數據的\n
            data_list = line.split(",")
            record_list.append(Record(data_list[0], data_list[1], int(data_list[2]), data_list[3]))
        f.close()
        return record_list


class JsonFileReader(FileReader):
    def __init__(self, path):
        self.path = path  # 定義成員變量，紀錄文件的路徑

    def read_data(self) -> list[Record]:
        f = open(self.path, "r", encoding="UTF-8")
        record_list: list[Record] = []
        for line in f.readlines():
            data_dict = json.loads(line)
            record_list.append(Record(data_dict["date"], data_dict["order_id"], int(data_dict["money"]), data_dict["province"]))
        f.close()
        return record_list


if __name__ == '__main__':
    list1 = TextFileReader("2011年1月销售数据.txt").read_data()
    list2 = JsonFileReader("2011年2月销售数据JSON.txt").read_data()

    for l in list1:
        print(l)

    for l in list2:
        print(l)