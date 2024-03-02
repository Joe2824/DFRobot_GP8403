'''Output square wave from channel 0

Keyword arguments:
amp - Set square wave amplitude Vp
freq - Set square wave frequency f
offset - Set square wave DC offset Voffset
duty_cycle - Set square wave duty cycle
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
DAC.set_DAC_outrange(DAC.OUTPUT_RANGE_5V)

while True:
    DAC.output_square(3430, 10, 2500, 50, DAC.CHANNEL0)
