from gpiozero import MCP3208
import time

cds = MCP3208(channel=0)

try:
    while 1:
        cds_value = cds.value * 3.3
        print(cds_value)
        time.sleep(0.2)
        
except KeyboardInterrupt:
    pass