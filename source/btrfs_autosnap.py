#!/usr/bin/env python
import time
import sys
time_s=time.strftime("%Y%m%d%H%M%S",time.localtime())
print('Create in time',time_s)
for i in sys.argv:
    print(i)

