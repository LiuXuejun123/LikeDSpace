import src.Xlsx.Xlsx as Xlsx
import src.DatabaseContainer.DatabaseContainer as DBC
import src.utils.utils as util
import re
import json
def remove_non_alphabet_chars(input_string):
    # 使用正则表达式过滤非英文字母字符，但保留空格
    return re.sub(r'[^a-zA-Z ]', '', input_string)

def extract_between_colon_semicolon(input_string):
    """
    提取字符串中 ':' 和 ';' 之间的字符。

    参数:
        input_string (str): 输入字符串，格式如 '键:值;键:值;'

    返回:
        list: 包含所有 ':' 和 ';' 之间的子字符串列表
    """
    # 检查输入是否为空
    if not input_string or input_string == "":
        return []

    result = []
    # 移除末尾的分号并按分号分割
    entries = input_string.rstrip(";").split(";")

    for entry in entries:
        # 确保条目不为空且包含冒号
        if entry and ":" in entry:
            # 按冒号分割，提取值部分（冒号后的部分）
            parts = entry.split(":", 1)  # 使用 split(":", 1) 确保只分割一次
            if len(parts) > 1:  # 确保有值部分
                value = parts[1].strip()  # 去除空白字符
                if value:  # 只添加非空值
                    value = remove_non_alphabet_chars(value)
                    result.append(value)

    return result
def parse_value_table(value_table):

    value_dict = {}
    for i in range(0,len(value_table)):
        value_dict[str(i)] = value_table[i]
    return value_dict

filename = Xlsx.SearchFilePath_Xlsx()
workbook,sheet = Xlsx.read_Xlsx(filename,"Sheet1")
result = []
message_groups = {}

for i in range(2,sheet.max_row+1):
    Result = []
    MessageName = str(sheet.cell(i, 1).value).replace('\n','')
    SignalName = str(sheet.cell(i, 2).value).replace('\n','')
    DataType = str(sheet.cell(i, 3).value).replace('\n','')
    TransPeriod = str(sheet.cell(i, 4).value).replace('\n', '')
    ValueTable = str(sheet.cell(i, 5).value)
    if MessageName not in message_groups:
        message_groups[MessageName] = []
    if DataType == "uint8":
        Result = extract_between_colon_semicolon(ValueTable)
        Value_Table = parse_value_table(Result)
        print(Value_Table)
        signal = {
            "signal_name": SignalName,
            "period_ms": TransPeriod,
            "data_type": DataType,  # Capitalize uint8 to Uint8
            "value_table": Value_Table
        }
    else:
        signal = {
            "signal_name": SignalName,
            "period_ms": TransPeriod,
            "data_type": DataType
        }

    message_groups[MessageName].append(signal)
for message_name, signals in message_groups.items():
    message = {
        "message_name": message_name,
        "signals": signals
    }
    result.append(message)
# Convert to JSON string with proper formatting
json_output = json.dumps(result, indent=2)

# Print the JSON output
print(json_output)

# Optionally, save to a file
with open("SignalMapping.json", "w") as f:
    json.dump(result, f, indent=2)