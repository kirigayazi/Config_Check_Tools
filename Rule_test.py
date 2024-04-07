# 读取文本文件的所有行
# file_path = 'data.txt'
# with open(file_path, 'r', encoding='utf-8') as file:
#     lines = file.readlines()
#
# # 处理每一行，删除等号及其之前的内容，并以分号 ";" 为分隔符分割键值对
# processed_lines = []
# for line in lines:
#     # 查找等号的位置
#     equal_sign_index = line.find('=')
#     if equal_sign_index != -1:
#         # 删除等号及其之前的部分，然后以分号分割键值对
#         value = line[equal_sign_index + 1:].strip()  # 删除等号及其之前的部分并去除首尾空格
#         processed_lines.append(value)
#         for line in processed_lines:
#     # 以分号分割键值对
#             key_value_pair = line.strip().split(';')
#             if len(key_value_pair) == 2:
#                 key, value = key_value_pair[0].split('=')[0], key_value_pair[1]
#                 print(f"Key: {key}, Value: {value}")
# # 将处理后的内容写回文本文件
# with open(file_path, 'w', encoding='utf-8') as file:
#     file.write('\n'.join(processed_lines))
#
# print("已删除'='号及其之前的数据，并以';'为间隔分割键值对，结果已保存到文件。")

# file_path = 'data.txt'
# with open(file_path, 'r', encoding='utf-8') as file:
#     lines = file.readlines()
#
# # 处理每一行，提取键和值并打印
# for line in lines:
#     # 以分号分割键值对
#     key_value_pair = line.strip().split(';')
#     if len(key_value_pair) == 2:
#         key, value = key_value_pair[0].split('=')[0], key_value_pair[1]
#         print(f"Key: {key}, Value: {value}")
import json

# 读取文本文件的所有行
file_path = 'data.txt'
with open(file_path, 'r', encoding='utf-8') as file:
    lines = file.readlines()

# 创建一个空列表，用于存储键值对
rule_list = []

# 处理每一行，删除等号及其之前的内容，并以分号 ";" 为分隔符分割键值对
for line in lines:
    # 查找等号的位置
    equal_sign_index = line.find('=')
    if equal_sign_index != -1:
        # 删除等号及其之前的部分，然后以分号分割键值对
        value = line[equal_sign_index + 1:].strip()  # 删除等号及其之前的部分并去除首尾空格
        key_value_pair = value.split(';')
        if len(key_value_pair) == 2:
            key, value = key_value_pair[0].split('=')[0], key_value_pair[1]
            rule_list.append({key:value})

# 将处理后的结果存储到 Rule.json 文件中
json_file_path = 'Rule.json'
with open(json_file_path, 'w', encoding='utf-8') as json_file:
    json.dump(rule_list, json_file, indent=4, ensure_ascii=False)

print("Data has been saved to Rule.json file.")


