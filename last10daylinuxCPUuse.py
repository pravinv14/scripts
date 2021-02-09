"""
This script requires sysstat package to be installed to get the historical data
yum install sysstat -- RHEL/centOS based system
Also this script get average of the day's CPU usage result
More edits to come.
"""

import os
from datetime import datetime, timedelta

data = []
for i in range(10):
    day = (datetime.now() - timedelta(i)).strftime('%d')
    cpudata = os.popen('sar -u -f /var/log/sa/sa'+str(day)+' | tail -1').read()[:-1].split(" ")
    if cpudata[-1] == '':
        empty = 0
    else:
        val = 100 - float(cpudata[-1])
    data.append(val)
    
for i in range(0,10):
    day = (datetime.now() - timedelta(i)).strftime('%d')
    print('CPU Usage for {} : '+ str(data[0])).format(day)
