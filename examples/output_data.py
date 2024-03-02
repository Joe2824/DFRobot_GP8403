'''Output signal from channel 0

Keyword arguments:
data - Set ouput signal e.g. 4.2V = 4200
channel - Output channel.
'''

import time
from DFRobot.DAC import GP8403

DAC = GP8403(0x58)
while DAC.begin() != 0:
    print("init error")
    time.sleep(1)
print("init succeed")

#Set output range
DAC.set_DAC_outrange(DAC.OUTPUT_RANGE_10V)

#Output value from DAC channel 0
DAC.set_DAC_out_voltage(4200,DAC.CHANNEL0)
