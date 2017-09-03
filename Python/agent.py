from datetime import datetime
from datetime import timedelta
from LKM1638 import LKM1638

current_dt = datetime.now()
port = '/dev/cu.usbmodem3208451'
delta = timedelta(microseconds=100000)

module = LKM1638(port)

while True:
    dt = datetime.now()
    utc_dt = datetime.utcnow()

    time_diff = dt - current_dt

    if time_diff > delta:
        current_dt = dt
        print "Current Time: ", str(dt)
        print "Current UTC Time: ", str(utc_dt)

        # Display Time based on button states
        buttons = module.get_buttons()
        if buttons & 0x01:
            timeFormat = '%m%d%H%M'
        else:
            timeFormat = '%m%d%I%M'

        if buttons & 0x02:
            module.set_time(utc_dt, timeFormat)
        else:
            module.set_time(dt, timeFormat)
