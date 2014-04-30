#!/usr/bin/env python 
#
from time import sleep 
from smbus import SMBus 



addr = 0x40

bus = SMBus(1); 

CMD_READ_TEMP_HOLD = 0xe3
CMD_READ_HUM_HOLD = 0xe5
CMD_READ_TEMP_NOHOLD = 0xf3
CMD_READ_HUM_NOHOLD = 0xf5
CMD_WRITE_USER_REG = 0xe6
CMD_READ_USER_REG = 0xe7
CMD_SOFT_RESET= 0xfe

# uses bits 7 and 0 of the user_register mapping
    # to the bit resolutions of (relative humidity, temperature)
RESOLUTIONS = {
	(0, 0) : (12, 14),
    (0, 1) : (8, 12),
    (1, 0) : (10, 13),
    (1, 1) : (11, 11),
}

MEASURE_TIMES = {
	(12, 14): (.018, .055),
    (8, 12): (.005, .015),
    (10, 13): (.006, .028),
    (11, 11): (.01, .009),
}

if reset_flag == 0:
	reset()
	
def get_h():
	bus.write_byte_data(addr, CMD_READ_TEMP_NOHOLD) 
	(msb, lsb, checksum) = bus.read_i2c_block_data(addr, CMD_READ_TEMP_HOLD, 3) 

def reset():
	bus.write_byte_data(addr, CMD_SOFT_RESET) 
	sleep (.02)
	reset_flag = 1
