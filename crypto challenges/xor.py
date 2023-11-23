def hex_xor(hex_str1, hex_str2):
    # 将16进制字符串转换为整数
    int_val1 = int(hex_str1, 16)
    int_val2 = int(hex_str2, 16)

    # 执行异或运算
    result_int = int_val1 ^ int_val2

    # 将结果转换为16进制字符串，并去掉开头的'0x'
    result_hex = hex(result_int)[2:]
    result_hex=bytes.fromhex(result_hex)

    # # 补充前导零，保证输出长度与输入一致
    # result_hex = result_hex.zfill(len(hex_str1))

    return result_hex

