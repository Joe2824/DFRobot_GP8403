'''Output sine wave from channel 0

Keyword arguments:
amp - Set sine wave amplitude Vp
freq - Set sine wave frequency f
offset - Set sine wave DC offset Voffset
channel - Output channel.
'''

import time
from DFRobot.DAC import GP8403

DAC = GP8403(addr=0x58)
while DAC.begin() != 0:
    print("init error")
    time.sleep(1)
print("init succeed")

#Set output range
DAC.set_DAC_outrange(DAC.OUTPUT_RANGE_10V)

while True:
  DAC.output_sin(5800, 10, 2500, DAC.CHANNEL0)
