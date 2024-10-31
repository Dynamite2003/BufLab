def ascii_to_hex(ascii_string):
    hex_output = ' '.join(format(ord(char), '02x') for char in ascii_string)
    return hex_output

# 示例用法
input_string = input("请输入ASCII字符串: ")
hex_result = ascii_to_hex(input_string)
print("十六进制表示:", hex_result)
