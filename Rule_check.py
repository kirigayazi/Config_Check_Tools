import pandas as pd
import json

# 读取 Excel 文件
file_path = 'skll_check.xlsx'
df = pd.read_excel(file_path)

# 读取 Rule.json 文件
with open('Rule.json', 'r', encoding='utf-8') as json_file:
    rule_list = json.load(json_file)

# 提取表格中的特定列作为key和value
key_column = 'effect'
value_column = 'remark6'

# 确保表格中的列名存在
if key_column in df.columns and value_column in df.columns:
    # 将表格转换为字典，key为effect列的值，value为remark6列的值
    data_dict = dict(zip(df[key_column], df[value_column]))

    # 遍历 Rule.json 中的每个规则，检查是否匹配
    # 读取 Rule.json 文件

    # 遍历每个字典
    # 读取 rule.json 文件
    with open('rule.json', 'r', encoding="utf-8") as json_file:
        rule_list = json.load(json_file)

    # 遍历规则字典列表
    # 假设 rule_list 是一个包含多个字典的列表
    for rule_dict in rule_list:
        print(rule_dict)
        # print(type(rule_dict))
        for key, value in rule_dict.items():
            if key in data_dict:
                actual_value = data_dict[key]
                if actual_value != value:
                    print(
                        f"Warning: Value mismatch for key '{key}': Actual value is '{actual_value}', expected value is '{value}'")
                else:
else:
                    print("警告，配置不符合设计")
    print("Error: One or more specified columns not found in the Excel file.")

print("配置检查通过，符合设计.")

