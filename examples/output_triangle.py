'''Output triangular wave from channel 0

Keyword arguments:
amp - Set triangle wave amplitude Vp
freq - Set triangle wave frequency f
offset - Set triangle wave DC offset Voffset
duty_cycle - Set triangle (sawtooth) wave duty cycle
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
    DAC.output_triangle(5000, 10, 0, 50, DAC.CHANNEL0)
