import json

# 读取 rule.json 文件
with open('rule.json', 'r', encoding="utf-8") as json_file:
    data = json.load(json_file)

# 查看 data 的类型
print(type(data))
