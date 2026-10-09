modbus = int(input())
high_byte = (modbus >> 8) & 255
low_byte = (modbus & 255)

print("high byte: ")
print({0:08b}.format(high_byte))
print("low byte: ")
print(low_byte)
print("\n")