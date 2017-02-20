#ADDR pin states
#Ground - 0x48
#VDD - 0x49
#SDA - 0x4A
#SCL - 0x4B
i2c_addr = 0x48

import smbus as smbus

i2c = smbus.SMBus(1)

i2c.write_quick(i2c_addr)
print("Sending byte to " + i2c_addr)
print "Received back: " + i2c.read_byte(i2c_addr)

