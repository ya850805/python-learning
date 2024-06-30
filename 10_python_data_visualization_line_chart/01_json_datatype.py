"""
json數據格式
"""
import json

# 準備一個列表，列表內每一個元素都是字典，將其轉換為JSON
data = [{"name": "張三", "age": 11}, {"name": "李四", "age": 13}, {"name": "王五", "age": 16}]
json_str = json.dumps(data, ensure_ascii=False)  # 內容包含中文需要指定 ensure_ascii=False
print(type(json_str))
print(json_str)

# 字典轉換為JSON
d = {"name": "周杰倫", "addr": "台北"}
json_str = json.dumps(d, ensure_ascii=False)
print(type(json_str))
print(json_str)

# 將JSON字符串轉換為Python數據類型 [{k: v, k: v}, {k: v, k: v}]
s = '[{"name": "張三", "age": 11}, {"name": "李四", "age": 13}, {"name": "王五", "age": 16}]'
l = json.loads(s)
print(type(l))
print(l)

# 將JSON字符串轉換為Python數據類型 {k: v, k: v}
s = '{"name": "周杰倫", "addr": "台北"}'
d = json.loads(s)
print(type(d))
print(d)