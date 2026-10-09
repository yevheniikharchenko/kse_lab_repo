print("input 16-bit number")

modbus = input()
high_byte = modbus[8:16]
low_byte = modbus[0:8]

print("high byte: ")
print(high_byte)
print("low byte: ")
print(low_byte)