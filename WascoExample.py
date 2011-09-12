#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# wasco/WascoExample.py
#
# (c) 2010 Konstantin Sering <konstantin.sering [aet] gmail.com>
# GPL 3.0+ or (cc) by-sa (http://creativecommons.org/licenses/by-sa/3.0/)

"""
WascoExample.py increases the first three analog outputs (DAOUT1_16 to 
DAOUT3_16) from -10 V to 10 V over time.
"""

try:    # normal import, if eyeone module is installed correctly 
    from wasco.wasco import wasco, boardId
    from wasco.WascoConstants import DAOUT1_16, DAOUT2_16, DAOUT3_16
except:     # if you run this in eyeone folder
    from wasco import wasco, boardId
    from WascoConstants import DAOUT1_16, DAOUT2_16, DAOUT3_16
import time

wasco.wasco_outportW(boardId, DAOUT1_16, 0x000)
wasco.wasco_outportW(boardId, DAOUT2_16, 0x000)
wasco.wasco_outportW(boardId, DAOUT3_16, 0x000)
time.sleep(1)     


for i in range(0xFF):
    wasco.wasco_outportW(boardId, DAOUT1_16, 0x010 * i)
    time.sleep(0.01)
time.sleep(1)
for i in range(0xFF):
    wasco.wasco_outportW(boardId, DAOUT1_16, 0xFFF - 0x010 * i)
    time.sleep(0.005)
wasco.wasco_outportW(boardId, DAOUT1_16, 0x000)

for i in range(0xFF):
    wasco.wasco_outportW(boardId, DAOUT2_16, 0x010 * i)
    time.sleep(0.01)
time.sleep(1)
for i in range(0xFF):
    wasco.wasco_outportW(boardId, DAOUT2_16, 0xFFF - 0x010 * i)
    time.sleep(0.005)
wasco.wasco_outportW(boardId, DAOUT2_16, 0x000)

for i in range(0xFF):
    wasco.wasco_outportW(boardId, DAOUT3_16, 0x010 * i)
    time.sleep(0.01)
time.sleep(1)
for i in range(0xFF):
    wasco.wasco_outportW(boardId, DAOUT3_16, 0xFFF - 0x010 * i)
    time.sleep(0.005)
wasco.wasco_outportW(boardId, DAOUT3_16, 0x000)

for i in range(0xFF):
    wasco.wasco_outportW(boardId, DAOUT1_16, 0x010 * i)
    wasco.wasco_outportW(boardId, DAOUT2_16, 0x010 * i)
    wasco.wasco_outportW(boardId, DAOUT3_16, 0x010 * i)
    time.sleep(0.01)
time.sleep(1)
for i in range(0xFF):
    wasco.wasco_outportW(boardId, DAOUT1_16, 0xFFF - 0x010 * i)
    wasco.wasco_outportW(boardId, DAOUT2_16, 0xFFF - 0x010 * i)
    wasco.wasco_outportW(boardId, DAOUT3_16, 0xFFF - 0x010 * i)
    time.sleep(0.005)
wasco.wasco_outportW(boardId, DAOUT1_16, 0x000)
wasco.wasco_outportW(boardId, DAOUT2_16, 0x000)
wasco.wasco_outportW(boardId, DAOUT3_16, 0x000)

#wasco.wasco_outportW(boardId, DAOUT1_16, 0xFFF)
#wasco.wasco_outportW(boardId, DAOUT2_16, 0xFFF)
#wasco.wasco_outportW(boardId, DAOUT3_16, 0xFFF)
#time.sleep(5)     
#
#wasco.wasco_outportW(boardId, DAOUT1_16, 0x000)
#wasco.wasco_outportW(boardId, DAOUT2_16, 0x000)
#wasco.wasco_outportW(boardId, DAOUT3_16, 0x000)
#time.sleep(5)     

