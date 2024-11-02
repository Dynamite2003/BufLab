# create_hex_numeric_file.py

# 原始十六进制字符串
original_hex = "b8 1d da 62 4a 8d 6c 24 28 68 f3 8b 04 08 c3"

# 移除空格并转换为字节
original_bytes = bytes.fromhex(original_hex)

# 创建509个0x90
padding = bytes([0x90] * 509)

# 合并原始字节和填充字节
final_bytes = original_bytes + padding

# 将每个字节转换为两位十六进制数
hex_list = [f"{byte:02x}" for byte in final_bytes]

# 定义输出文件名
output_filename = "output_hex_numeric.txt"

# 将十六进制字符串写入文本文件，以空格分隔
with open(output_filename, "w") as file:
    file.write(' '.join(hex_list))

print(f"文件已保存为 {output_filename}，包含原始字节和509个90，以十六进制表示。")
