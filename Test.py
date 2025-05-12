import pandas as pd
import json

# 读取 Excel 文件
excel_file = "signals.xlsx"  # 替换为你的 Excel 文件路径
df = pd.read_excel(excel_file)

# 确保 Excel 包含正确的列
if not {"Name", "SignalName"}.issubset(df.columns):
    raise ValueError("Excel 文件必须包含 'Name' 和 'SignalName' 两列")

# 按 Name 分组，收集每个变量的信号名称
grouped = df.groupby("Name")["SignalName"].apply(list).to_dict()

# 验证每个变量有 16 个信号
for name, signals in grouped.items():
    if len(signals) != 16:
        raise ValueError(f"变量 {name} 的信号数量不为 16，实际为 {len(signals)}")

# 构造 JSON 数据
result = {"variables": []}
for name, signal_names in grouped.items():
    var_data = {
        "name": name,
        "signals": [
            {"index": i, "name": signal_name}
            for i, signal_name in enumerate(signal_names)
        ]
    }
    result["variables"].append(var_data)
# 保存到 JSON 文件
output_file = "signals2.json"
with open(output_file, "w", encoding="utf-8") as f:
    json.dump(result, f, indent=2, ensure_ascii=False)
print(f"JSON 已保存到 {output_file}")